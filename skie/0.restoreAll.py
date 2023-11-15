from neo4j import GraphDatabase

# Replace these with your actual Neo4j connection details
neo4j_uri = "bolt://localhost:7689"
username = "neo4j"
password = "re91na00"

# URL of the JSON data
json_url = "http://1.229.96.163/skie/backup/backup231115.json"

# Cypher query template
cypher_template = (
    "MERGE (a:`{label}` {uuid: $uuid}) "
    "SET a += $properties"
)

# Function to execute Cypher query
def execute_query(query, params):
    with GraphDatabase.driver(neo4j_uri, auth=(username, password)) as driver:
        with driver.session() as session:
            session.run(query, params)

# Fetch JSON data
# Note: This assumes the JSON structure is a list of records, each containing 'n.labels' and 'n.properties'
json_data = [
    {"n": {"labels": ["Label1"], "properties": {"uuid": "123", "other_prop": "value"}}},
    {"n": {"labels": ["Label2"], "properties": {"uuid": "456", "other_prop": "value"}}},
    # Add more records as needed
]

# Process each record in the JSON data
for record in json_data:
    label = record["n"]["labels"][0]  # Assuming there is only one label in the list
    uuid = record["n"]["properties"]["uuid"]
    properties = record["n"]["properties"]

    # Execute the Cypher query
    execute_query(cypher_template, {"label": label, "uuid": uuid, "properties": properties})

