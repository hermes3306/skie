package jhpark;
import org.neo4j.procedure.*;

import java.util.List;
import java.util.Map;

public class myfunc {
    @UserFunction
    @Description("myfunc.do([...]) - Process CSV data.")
    public List<Map<String, Object>> doit(@Name("data") List<Map<String, Object>> data) {
        if (data == null) {
           return null;
        }

        // Process each record in the list
        for (Map<String, Object> record : data) {
            // Iterate over the keys in the map
            for (String key : record.keySet()) {
                // Get the value associated with the key
                Object value = record.get(key);

                // Customize your processing logic here
                if (value instanceof String) {
                    String processedValue = key + ": " + value;
                    record.put(key, processedValue);
                } else {
                }
            }
        }

        // You can return the modified list or extract specific values
        return data;
    }
}


