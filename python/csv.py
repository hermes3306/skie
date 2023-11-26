
import GraphDatabase
import os

# Neo4j connection details
uri = "neo4j+s://942801e8.databases.neo4j.io:7687"
username = "neo4j"
password = "re91na00"


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

                                                # Download the CSV file
                                                # This is a simple example, the method can vary based on your specific needs (e.g., web download)
                                                # Here's an example using the local path
                                                if os.path.exists(output_csv_file):
                                                        # For local file download
                                                            print(f"CSV file '{output_csv_file}' downloaded successfully.")
                                                        else:
                                                                print("CSV file download failed.")

