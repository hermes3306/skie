mvn package
java -cp target/jhpark-1.0.jar jhpark.hello jason
sudo cp target/jhpark*jar ~/plugins/
sudo chown neo4j:adm ~/plugins/jhpark*jar 
sudo chmod 755 ~/plugins/jhpark*jar 
