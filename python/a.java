import java.sql.Driver;

import org.neo4j.driver.*;
public class a {
    public static void main(String[] args) {
        System.out.println("Hello World   !");

         // Connect to Neo4j
        try (Driver driver = GraphDatabase.driver("bolt://localhost:7687", AuthTokens.basic("username", "password"));
             Session session = driver.session()) {

            // Run a simple query
            String greeting = session.writeTransaction(tx -> {
                StatementResult result = tx.run("CREATE (n:Greeting) SET n.message = $message RETURN n.message",
                        Values.parameters("message", "Hello, Neo4j!"));
                return result.single().get(0).asString();
            });

            // Output the result
            System.out.println(greeting);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }

        
    }
}