import os
from neo4j import GraphDatabase


# Neo4j connection details
uri = "neo4j+s://942801e8.databases.neo4j.io:7687"
username = "neo4j"
password = "neo4j2022"

# Cypher query to load data from CSV to Neo4j
cypher_query = """
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///$csv_file' AS row
CREATE (:Node {node: row.node})
"""

# Output CSV file path
output_csv_file = "output.csv"

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Run Cypher query to upload data from CSV to Neo4j
with driver.session() as session:
    result = session.run(cypher_query)
    print("CSV data uploaded to Neo4j.")

# Close the connection
driver.close()
