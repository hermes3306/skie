from neo4j import GraphDatabase

# Replace these with your actual Neo4j connection details
neo4j_uri = "bolt://localhost:7689"
username = "neo4j"
password = "re91na00"

# Cypher query to execute
cypher_query = "MATCH (n) RETURN n LIMIT 5"

# Function to execute Cypher query
def execute_query(query):
    with GraphDatabase.driver(neo4j_uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query)
            # Fetch all records and store them in a list
            records = list(result)
            return records

# Example: Execute the Cypher query
result = execute_query(cypher_query)

# Process the result
for record in result:
    print(record)

