package jhpark;
import org.neo4j.driver.*;

public class ex1 {

    public static void main(String[] args) {
	String greeting;

        // Connect to Neo4j
        try (Driver driver = GraphDatabase.driver("neo4j+s://2648b64e.databases.neo4j.io", AuthTokens.basic("neo4j", "neo4j2023"));
             Session session = driver.session()) {


            // Run a simple query
            greeting = session.executeWrite(tx -> {
                tx.run("CREATE (n:Greeting) SET n.message = $message RETURN n.message",
                        Values.parameters("message", "Hello, Neo4j!"));
                return "OK";
            });


            // Output the result
            System.out.println(greeting);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}

