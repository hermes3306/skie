from neo4j import GraphDatabase
import os

# Connect to the Neo4j database
uri = "bolt://localhost:7689"
username = "neo4j"
password = "re91na00"

driver = GraphDatabase.driver(uri, auth=(username, password))

# List of labels
labels = [
    "Region", "ApartmentType", "Contract", "Daycare", "Hospital",
    "Kinder", "Mart", "Park", "School", "BusStation", "GoodWayToWalk",
    "Highway", "Subway", "BusRoute", "SubwayFuture", "Convention",
    "Theater", "Academy", "Departmentstore", "DistrictBoundaryDong",
    "DistrictBoundaryGu", "SpecialPurposeArea", "Reputation"
]

# Export nodes for each label
for label in labels:
    query = f"MATCH (n:{label}) RETURN n"
    file_name = f"{label.lower()}.csv"
    file_path = os.path.abspath(file_name)  # Getting the absolute path
    with driver.session() as session:
        result = session.run(query)
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            if result.peek():
                # Write header with property names
                node = result.peek()["n"]
                properties = list(node.keys())
                file.write(",".join(properties) + "\n")
                # Write node data
                for record in result:
                    node_props = record["n"]
                    values = [f'"{str(node_props.get(prop, ""))}"' for prop in properties]
                    file.write(",".join(values) + "\n")
        print(f"CSV file '{file_name}' has been exported to: {file_path}")

driver.close()


