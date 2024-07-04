package main

import (
	"fmt"
	"github.com/neo4j/neo4j-go-driver/neo4j"
	"log"
)

func main() {
	// Neo4j connection URL
	uri := "bolt://localhost:7687"
	username := "your_username"
	password := "your_password"

	// Create a Neo4j driver instance
	driver, err := neo4j.NewDriver(uri, neo4j.BasicAuth(username, password, ""))
	if err != nil {
		log.Fatal("Failed to create Neo4j driver:", err)
	}
	defer driver.Close()

	// Create a Neo4j session
	session, err := driver.Session(neo4j.AccessModeWrite)
	if err != nil {
		log.Fatal("Failed to open Neo4j session:", err)
	}
	defer session.Close()

	// Run a Cypher query to create a node
	result, err := session.Run(
		"CREATE (n:Person {name: $name, age: $age}) RETURN n",
		map[string]interface{}{
			"name": "Alice",
			"age":  30,
		})
	if err != nil {
		log.Fatal("Failed to run Cypher query:", err)
	}

	// Process the query result
	for result.Next() {
		record := result.Record()
		node := record.GetByIndex(0) // Get the first item in the record
		fmt.Printf("Created node: %v\n", node)
	}

	if err = result.Err(); err != nil {
		log.Fatal("Query result error:", err)
	}
}
