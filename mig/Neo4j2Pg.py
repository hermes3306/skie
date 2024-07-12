import csv
import psycopg2
from neo4j import GraphDatabase
from PostgreSQLManager import PostgreSQLManager
from Neo4jManager import Neo4jManager

def main():
    db_manager = PostgreSQLManager(
        dbname="postgres",
        user="postgres",
        password="re91na00",
        host="localhost",
        port="5432"
    )

    # neo4j_manager = Neo4jManager(
    #     uri="bolt://localhost:7687",
    #     user="neo4j",
    #     password="neo4jpassword"
    # )

    neo4j_manager = Neo4jManager(
        uri="neo4j+s://84a70536.databases.neo4j.io",
        user="neo4j",
        password="VOE78BcdKmy49Upzsl0_Dwb0IUfNdlEfwePszwlkB8g"
    )
   
    # Split the string into a list of lines (strings)
    label_list = lables.strip().split('\n')
    print(label_list)

    # Iterate over each label in the list
    for label_name in label_list:
        neo4j_manager.download_nodes_as_csv(label_name)
        # Upload the CSV file to pgsql
        db_manager.upload_csv_to_table(f'{label_name}.csv')
        #print(f"Data from nodes with the lable ('{label_name})' migrated to pgsql successfully!")
        

labels_back = """Reputaion"""

lables = """
Apartment
Academy
ApartmentType
BusStation
Contract
Convention
Daycare
Departmentstore
DistrictBoundaryDong
DistrictBoundaryGu
GoodWayToWalk
Highway
Hospital
Kinder
Mart
Park
School
SpecialPurposeArea
Subway
SubwayFuture
Theater
"""

if __name__ == "__main__":
    main()