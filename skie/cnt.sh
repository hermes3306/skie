#!/bin/bash

# Cypher query
QUERY="MATCH (b:Apartment)
WITH count(b) as sizeofa
MATCH (a:Apartment)
WITH a.uuid AS id, SPLIT(a.uuid, '_') AS parts,sizeofa
WITH HEAD(parts) AS a, TOINTEGER(LAST(parts)) AS b, sizeofa as sizeofa
WITH a, b, sizeofa
ORDER BY a, b
WITH a, b, COLLECT(a) AS rows,sizeofa
WITH a, b, range(1, size(rows)) AS rowNumber,sizeofa
RETURN a,b,rowNumber,sizeofa"

# Neo4j credentials
NEO4J_USER="neo4j"
NEO4J_PASSWORD="rPNgDfFeruVONoEH1Vc8JgsnukQLVKadEQJ5dtlCsaI"

# Neo4j server details
NEO4J_HOST="942801e8.databases.neo4j.io"
NEO4J_PORT="7687"

# Run Cypher query using cypher-shell
echo "$QUERY" | cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_HOST:$NEO4J_PORT -d neo4j

