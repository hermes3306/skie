#!/bin/bash

# Set your Neo4j credentials
NEO4J_URI="bolt://localhost:7689"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="re91na00"
CYPHER_FILE="apoc.exp.csv.cypher"

CSV_URI="http://1.229.96.163/skie/json"

# Define a function to store the Cypher query
function create_cypher_query_file {
cat <<EOF > "$CYPHER_FILE"
CALL apoc.export.csv.all("alldata.csv",{});
EOF
}


# Run the function to create the Cypher query file
create_cypher_query_file
echo cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f $CYPHER_FILE
cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f $CYPHER_FILE
