from neo4j import GraphDatabase
import tempfile
import os

# Neo4j connection details
neo4j_uri = "bolt://localhost:7689"
username = "neo4j"
password = "re91na00"

# CSV data as a string
csv_data = """
name,age,phone,job,address
Alice,30,123456789,Engineer,123 Main St
Bob,25,987654321,Developer,456 Oak St
Charlie,35,555123456,Manager,789 Pine St
David,28,111222333,Designer,321 Cedar St
"""

temp_csv_file = "http://localhost/skie/test/employees.csv"

# Cypher query with a parameter
cypher_query = """
LOAD CSV WITH HEADERS FROM $temp_csv_file AS row
CREATE (:emp {
  name: row.name,
  age: toInteger(row.age),
  phone: row.phone,
  job: row.job,
  address: row.address
});
"""

# Function to execute Cypher query with parameters
def execute_query(query, parameters):
    with GraphDatabase.driver(neo4j_uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query, **parameters)
            # Fetch all records and store them in a list
            records = list(result)
            return records

# Example: Execute the Cypher query with parameters
parameters = {"temp_csv_file": temp_csv_file}
result = execute_query(cypher_query, parameters)
