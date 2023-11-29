package jhpark;

import org.neo4j.driver.AuthTokens;
import org.neo4j.driver.Driver;
import org.neo4j.driver.GraphDatabase;
import org.neo4j.driver.Query;

import static org.neo4j.driver.Values.parameters;

public class ex1 implements AutoCloseable {
    private final Driver driver;

    public ex1(String uri, String user, String password) {
        driver = GraphDatabase.driver(uri, AuthTokens.basic(user, password));
    }

    @Override
    public void close() throws RuntimeException {
        driver.close();
    }

    public void printGreeting(final String message) {
        try (var session = driver.session()) {
            var greeting = session.executeWrite(tx -> {
                var query = new Query("CREATE (a:Greeting) SET a.message = $message RETURN a.message + ', from node ' + id(a)", parameters("message", message));
                var result = tx.run(query);
                return result.single().get(0).asString();
            });
            System.out.println(greeting);
        }
    }



    public static void main(String... args) {
    	String NEO4J_URI="neo4j+s://fa216ca0.databases.neo4j.io";
	String NEO4J_USER="neo4j";
	String NEO4J_PASSWORD="1ASLEej5ggsCPSJnqXDHl21FrQCT3b05s0JJQPBx5vY";
        try (var greeter = new ex1(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)) {

            greeter.printGreeting("hello, world");
        }
    }
}
