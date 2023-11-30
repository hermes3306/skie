from neo4j import GraphDatabase
import os
import csv

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "re91na00"

driver = GraphDatabase.driver(uri, auth=(username, password))

# List of labels
labels = [
    "Apartment", "Region", "ApartmentType", "Contract", "Daycare", "Hospital",
    "Kinder", "Mart", "Park", "School", "BusStation", "GoodWayToWalk",
    "Highway", "Subway", "BusRoute", "SubwayFuture", "Convention",
    "Theater", "Academy", "Departmentstore", "DistrictBoundaryDong",
    "DistrictBoundaryGu", "SpecialPurposeArea", "Reputation"
]

# Function to export relationships of a specific type to a CSV file
def export_relationships_to_csv(driver, relationship_type, csv_file):
    with driver.session() as session:
        cypher_query = f"MATCH (a)-[:{relationship_type}]->(b) RETURN a.uuid as src, b.uuid as tar"
        result = session.run(cypher_query)
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(result.keys())  # Write header
            for record in result:
                csv_writer.writerow(record)
        print(f"CSV file '{csv_file}' has been exported.")

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

# Export relationships to separate CSV files
export_relationships_to_csv(driver, "IN", "IN.csv")
export_relationships_to_csv(driver, "TRADE", "TRADE.csv")
export_relationships_to_csv(driver, "EVALUATE", "EVALUATE.csv")
export_relationships_to_csv(driver, "HAS_TYPE", "HAS_TYPE.csv")

driver.close()


