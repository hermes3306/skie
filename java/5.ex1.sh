#!/bin/bash
cp *.java jhpark/src/main/java/jhpark/
cd jhpark
mvn clean install
java -cp jhpark/target/jhpark-1.0.jar jhpark.ex1
