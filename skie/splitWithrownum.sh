#!/bin/bash

# Cypher query
QUERY="MATCH (a:Apartment)
WITH a.uuid AS id, SPLIT(a.uuid, '_') AS parts
WITH HEAD(parts) AS a, TOINTEGER(LAST(parts)) AS b
RETURN a, b, COLLECT(a) AS rows
WITH rows, range(1, size(rows)) AS rowNumber
UNWIND rowNumber AS rowNum
WITH rows[rowNum-1] AS row
RETURN row.a AS a, row.b AS b, rowNum AS rowNumber;"


# Neo4j credentials
NEO4J_USER="neo4j"
NEO4J_PASSWORD="rPNgDfFeruVONoEH1Vc8JgsnukQLVKadEQJ5dtlCsaI"

# Neo4j server details
NEO4J_HOST="942801e8.databases.neo4j.io"
NEO4J_PORT="7687"

# Run Cypher query using cypher-shell
echo "$QUERY" | cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_HOST:$NEO4J_PORT -d neo4j

