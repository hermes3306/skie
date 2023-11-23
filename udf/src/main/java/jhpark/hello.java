package jhpark;

public class hello {
    
    public String world(String data) {
        return "Hello " + data;
    }

    public static void main(String[] args) {
        if (args.length == 1) {
            String input = args[0];
            hello h = new hello();
            String result = h.world(input);
            System.out.println(result);
        } else {
            System.out.println("Usage: java jhpark.hello <data>");
        }
    }
}


