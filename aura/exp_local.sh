#!/bin/bash

# Set your Neo4j credentials
NEO4J_URI="bolt://localhost:7687"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="re91na00"

CSV_URI="http://1.229.96.163/skie/json"

# Define a function to store the Cypher query
function create_cypher_query_file {
cat <<EOF > exp.cypher

// apoc.export.csv
call apoc.export.csv.all("all.csv",{});
call apoc.export.json.all("all.json",{});
call apoc.export.cypher.all("all.cypher",{});


EOF
}


# Run the function to create the Cypher query file
create_cypher_query_file
echo cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f exp.cypher
cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f exp.cypher
