#!/bin/bash

# Set your Neo4j credentials
NEO4J_URI="neo4j+s://fa216ca0.databases.neo4j.io"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="1ASLEej5ggsCPSJnqXDHl21FrQCT3b05s0JJQPBx5vY"

echo cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f all.cypher
cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f all.cypher
