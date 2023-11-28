package jhpark;
import org.neo4j.driver.*;

public class ex1 {

    public static void main(String[] args) {

        // Connect to Neo4j
        try (Driver driver = GraphDatabase.driver("neo4j+s://942801e8.databases.neo4j.io", AuthTokens.basic("neo4j", "neo4j2022"));
             Session session = driver.session()) {

            // Run a simple query
            String greeting = session.executeWrite(tx -> {
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

