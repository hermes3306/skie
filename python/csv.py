import os
from neo4j import GraphDatabase


# Neo4j connection details
uri = "neo4j+s://942801e8.databases.neo4j.io:7687"
username = "neo4j"
password = "neo4j2012"

# Cypher query to export data to CSV, change the query as needed
cypher_query = "MATCH (n) RETURN n"

# Output CSV file path
output_csv_file = "output.csv"

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Run Cypher query to export data to CSV
with driver.session() as session:
    result = session.run(cypher_query)
    with open(output_csv_file, "w", newline="", encoding="utf-8") as csvfile:
        csvfile.write("node\n")  # Writing header if needed
        for record in result:
            csvfile.write(f"{record['n']}\n")  # Writing data to CSV

# Close the connection
driver.close()

if os.path.exists(output_csv_file):
    print(f"CSV file '{output_csv_file}' downloaded successfully.")
else:
    print("CSV file download failed.")
