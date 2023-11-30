from neo4j import GraphDatabase
import os
import csv

# Connect to the Neo4j database
uri = "bolt://localhost:7689"
username = "neo4j"
password = "re91na00"

driver = GraphDatabase.driver(uri, auth=(username, password))

# List of labels and their corresponding CSV files
labels_files = {
    "Apartment": "apartment.csv",
    "Academy": "academy.csv",
    "Contract": "contract.csv",
    "DistrictBoundaryDong": "districtboundarydong.csv",
    "Hospital": "hospital.csv",
    "Region": "region.csv",
    "Subway": "subway.csv",
    "ApartmentType": "apartmenttype.csv",
    "Convention": "convention.csv",
    "DistrictBoundaryGu": "districtboundarygu.csv",
    "Kinder": "kinder.csv",
    "Reputation": "reputation.csv",
    "SubwayFuture": "subwayfuture.csv",
    "BusRoute": "busroute.csv",
    "Daycare": "daycare.csv",
    "GoodWayToWalk": "goodwaytowalk.csv",
    "Mart": "mart.csv",
    "School": "school.csv",
    "Theater": "theater.csv",
    "BusStation": "busstation.csv",
    "Departmentstore": "departmentstore.csv",
    "Highway": "highway.csv",
    "Park": "park.csv",
    "SpecialPurposeArea": "specialpurposearea.csv"
}

# File paths and relationship names
files_and_relationships = [
    ("IN.csv", "IN"),
    ("TRADE.csv", "TRADE"),
    ("HAS_TYPE.csv", "HAS_TYPE"),
    ("EVALUATE.csv", "EVALUATE")
]

# Function to import CSV file into Neo4j
def import_csv(label, file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            query = f"""
            MERGE (n:`{label}` {{ {", ".join([f"`{key}`: '{value}'" for key, value in row.items()])} }})
            """
            with driver.session() as session:
                session.run(query)

# Function to create relationships based on CSV data
def create_relationships_from_csv(driver, csv_file, relationship_name):
    with driver.session() as session:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                src = row.get('src')
                tar = row.get('tar')
                if src and tar:  # Check if 'src' and 'tar' exist in the row
                    # Create relationship between nodes
                    cypher_query = (
                        f"MATCH (source {{uuid: '{src}'}}), (target {{uuid: '{tar}'}}) "
                        f"MERGE (source)-[:{relationship_name}]->(target)"
                    )
                    session.run(cypher_query)
                else:
                    print(f".Skipping row in {csv_file}. Missing 'src' or 'tar' data.")

# Import nodes for each label
for label, file_name in labels_files.items():
    file_path = os.path.abspath(file_name)
    print(f"Importing CSV file '{file_name}' for label '{label}'...")
    import_csv(label, file_path)

# Create relationships from CSV files
for file_name, relationship_name in files_and_relationships:
    csv_file_path = os.path.abspath(file_name)
    print(f"file:{csv_file_path}");
    create_relationships_from_csv(driver, csv_file_path, relationship_name)

driver.close()
