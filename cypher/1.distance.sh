#!/bin/bash

# Set your Neo4j credentials
NEO4J_USER="neo4j"
NEO4J_PASSWORD="re91na00"
NEO4J_URI="neo4j+s://942801e8.databases.neo4j.io:7687"

# Define a function to store the Cypher query
function create_cypher_query_file {
  cat <<EOF > distance.cypher

MATCH (a:Apartment), (s:School) 
WITH 	a, s, a.coord as p1, s.coord as p2 
WHERE 	point.distance(p1,p2) < 100 return a.name, s.name;

EOF
}

# Run the function to create the Cypher query file
create_cypher_query_file

# Run cypher-shell with the query file
cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f distance.cypher

