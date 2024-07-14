
import csv
import psycopg2
from neo4j import GraphDatabase
from PostgreSQLManager import PostgreSQLManager
from Neo4jManager import Neo4jManager

def main():
    db_manager = PostgreSQLManager(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    neo4j_manager = Neo4jManager(
        uri="bolt://localhost:7687",
        user="neo4j",
        password="neo4j_password"
    )

    # neo4j_manager = Neo4jManager(
    #     uri="neo4j+s://84a70536.databases.neo4j.io",
    #     user="neo4j",
    #     password="VOE78BcdKmy49Upzsl0_Dwb0IUfNdlEfwePszwlkB8g"
    # )
   
    table_names = db_manager.get_table_names()
    for table_name in table_names:
        db_manager.download_table_as_csv(table_name)
        neo4j_manager.upload_csv_to_nodes(f'{table_name}.csv')

if __name__ == "__main__":
    main()