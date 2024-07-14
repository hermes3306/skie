from flask import Flask, render_template, request, jsonify
import psycopg2
from neo4j import GraphDatabase

app = Flask(__name__)

# PostgreSQL connection details
PG_URL = 'postgresql://localhost:5432/postgres'
PG_USER = 'postgres'
PG_PASSWORD = 'postgres'

# Neo4j connection details
NEO4J_URL = 'bolt://localhost:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'neo4j_password'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_pg_connection', methods=['POST'])
def test_pg_connection():
    try:
        conn = psycopg2.connect(PG_URL, user=PG_USER, password=PG_PASSWORD)
        cur = conn.cursor()

        cur.execute("""
            SELECT table_name, COUNT(column_name) as column_count
            FROM information_schema.columns
            WHERE table_schema = 'public'
            GROUP BY table_name
        """)
        tables_info = cur.fetchall()

        table_data = []
        for table_name, column_count in tables_info:
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cur.fetchone()[0]
            table_data.append({
                'name': table_name,
                'columns': column_count,
                'rows': row_count
            })

        conn.close()
        return jsonify({'success': True, 'tables': table_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/test_neo_connection', methods=['POST'])
def test_neo_connection():
    try:
        driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            result = session.run("""
                CALL db.labels() YIELD label
                CALL apoc.cypher.run('MATCH (n:`' + label + '`) 
                                    WITH count(n) as nodeCount, 
                                        reduce(s = [], k IN keys(n) | s + k) AS allProps
                                    RETURN nodeCount, size(apoc.coll.toSet(allProps)) as propCount', 
                                    {}) YIELD value
                RETURN label, value.nodeCount AS count, value.propCount AS propCount
            """)
            labels = list(result)
            
        driver.close()
        return jsonify({'success': True, 'labels': [dict(record) for record in labels]})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/execute_sql', methods=['POST'])
def execute_sql():
    query = request.json['query']
    try:
        conn = psycopg2.connect(PG_URL, user=PG_USER, password=PG_PASSWORD)
        cur = conn.cursor()
        
        is_select = query.strip().upper().startswith("SELECT")
        
        cur.execute(query)
        
        if is_select:
            result = cur.fetchall()
            conn.close()
            return jsonify({'success': True, 'result': result})
        else:
            conn.commit()
            affected_rows = cur.rowcount
            conn.close()
            return jsonify({'success': True, 'affected_rows': affected_rows})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/execute_cypher', methods=['POST'])
def execute_cypher():
    query = request.json['query']
    try:
        driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            result = session.run(query)
            summary = result.consume()
            
            if summary.counters.contains_updates:
                return jsonify({
                    'success': True,
                    'updates': {
                        'nodes_created': summary.counters.nodes_created,
                        'nodes_deleted': summary.counters.nodes_deleted,
                        'relationships_created': summary.counters.relationships_created,
                        'relationships_deleted': summary.counters.relationships_deleted,
                        'properties_set': summary.counters.properties_set
                    }
                })
            else:
                records = [dict(record) for record in result]
                return jsonify({'success': True, 'result': records})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/migrate', methods=['POST'])
def migrate_data():
    try:
        pg_conn = psycopg2.connect(PG_URL, user=PG_USER, password=PG_PASSWORD)
        pg_cur = pg_conn.cursor()

        neo4j_driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))

        pg_cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = pg_cur.fetchall()

        migration_results = []

        with neo4j_driver.session() as neo4j_session:
            for table in tables:
                table_name = table[0]
                
                pg_cur.execute(f"SELECT * FROM {table_name}")
                rows = pg_cur.fetchall()

                pg_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                columns = [col[0] for col in pg_cur.fetchall()]

                for row in rows:
                    properties = dict(zip(columns, row))
                    cypher_query = (
                        f"CREATE (n:{table_name} $properties)"
                    )
                    neo4j_session.run(cypher_query, properties=properties)

                migration_results.append({
                    'table': table_name,
                    'rows_migrated': len(rows)
                })

        pg_conn.close()
        neo4j_driver.close()
        return jsonify({'success': True, 'results': migration_results})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

