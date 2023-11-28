
from neo4j import GraphDatabase

# Connect to Neo4j, replace <uri>, <username>, and <password> with your credentials
uri = "neo4j+s://942801e8.databases.neo4j.io:7687"
username = "neo4j"
password = "neo4j2022"

# Establish a connection
driver = GraphDatabase.driver(uri, auth=(username, password))

# Define a function to create a node
def create_node(tx, name):
    tx.run("CREATE (:Person {name: $name})", name=name)

def change_password(tx, pwd):
    tx.run("ALTER USER neo4j set password $pwd", pwd=pwd)

# Run the function within a Neo4j session
with driver.session() as session:
    session.execute_write(create_node, "Alice")
    #session.execute_write(change_password, "neo4j2022")

# Define a function to read nodes
def read_nodes(tx):
    result = tx.run("MATCH (p:Person) RETURN p.name AS name")
    return [record["name"] for record in result]

# Run the function within a Neo4j session
with driver.session() as session:
    names = session.execute_read(read_nodes)
    print("Names of people in the database:", names)

# Close the connection
driver.close()

