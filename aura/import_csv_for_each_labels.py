from neo4j import GraphDatabase
import os
import csv

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "re91na00"

driver = GraphDatabase.driver(uri, auth=(username, password))

# List of labels and their corresponding CSV files
labels_files = {
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

# Function to import CSV file into Neo4j
def import_csv(label, file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            query = f"""
            MERGE (n:`{label}` {{ {", ".join([f"`{key}`: '{value}'" for key, value in row.items()])} }})
            """
            with driver.session() as session:
                print(f"'{query}'")
                session.run(query)

# Import nodes for each label
for label, file_name in labels_files.items():
    file_path = os.path.abspath(file_name)
    print(f"Importing CSV file '{file_name}' for label '{label}'...")
    import_csv(label, file_path)

driver.close()
