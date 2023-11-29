#!/bin/bash

# Set your Neo4j credentials
NEO4J_URI="bolt://localhost:7687"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="re91na00"

CSV_URI="http://1.229.96.163/skie/json"

# Define a function to store the Cypher query
function create_cypher_query_file {
cat <<EOF > imp.cypher

MATCH (n) DETACH DELETE n;
CALL apoc.load.json("$CSV_URI/Apartment.json") YIELD value AS records1
UNWIND records1 AS apartment
CREATE (a:Apartment)
WITH a, apartment.n.properties as apartmentProperties
SET a = apartmentProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(apartmentProperties.coord.y), longitude: toFloat(apartmentProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Academy.json") YIELD value AS records2
UNWIND records2 AS record
CREATE (a:Academy)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/ApartmentType.json") YIELD value AS records3
UNWIND records3 AS record
CREATE (a:ApartmentType)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/BusStation.json") YIELD value AS records4
UNWIND records4 AS record
CREATE (a:BusStation)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Contract.json") YIELD value AS records5
UNWIND records5 AS record
CREATE (a:Contract)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Convention.json") YIELD value AS records6
UNWIND records6 AS record
CREATE (a:Convention)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Daycare.json") YIELD value AS records7
UNWIND records7 AS record
CREATE (a:Daycare)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Departmentstore.json") YIELD value AS records8
UNWIND records8 AS record
CREATE (a:Departmentstore)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/DistrictBoundaryDong.json") YIELD value AS records9
UNWIND records9 AS record
CREATE (a:DistrictBoundaryDong)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/DistrictBoundaryGu.json") YIELD value AS records10
UNWIND records10 AS record
CREATE (a:DistrictBoundaryGu)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/GoodWayToWalk.json") YIELD value AS records11
UNWIND records11 AS record
CREATE (a:GoodWayToWalk)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Highway.json") YIELD value AS records12
UNWIND records12 AS record
CREATE (a:Highway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Hospital.json") YIELD value AS records13
UNWIND records13 AS record
CREATE (a:Hospital)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Kinder.json") YIELD value AS records14
UNWIND records14 AS record
CREATE (a:Kinder)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Mart.json") YIELD value AS records15
UNWIND records15 AS record
CREATE (a:Mart)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Park.json") YIELD value AS records16
UNWIND records16 AS record
CREATE (a:Park)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/School.json") YIELD value AS records17
UNWIND records17 AS record
CREATE (a:School)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Subway.json") YIELD value AS records18
UNWIND records18 AS record
CREATE (a:Subway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/SubwayFuture.json") YIELD value AS records19
UNWIND records19 AS record
CREATE (a:SubwayFuture)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

CALL apoc.load.json("$CSV_URI/Theater.json") YIELD value AS records20
UNWIND records20 AS record
CREATE (a:Theater)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

MATCH (n:Relations_IN) detach delete n;
CALL apoc.load.json("$CSV_URI/Relations_IN.json") YIELD value AS records21
UNWIND records21 AS record
CREATE (a:Relations_IN)
SET a.src = record.nuuid
SET a.tar = record.duuid
RETURN count(a);

match (n), (r:Relations_IN), (d:DistrictBoundaryDong)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:IN]->(d);

MATCH (n:Relations_IN) detach delete n;

MATCH (n:Relations_HAS) detach delete n;
CALL apoc.load.json("$CSV_URI/Relations_HAS.json") YIELD value AS has_records
UNWIND has_records AS record
CREATE (a:Relations_HAS)
SET a.src = record.auuid
SET a.tar = record.buuid
RETURN count(a);

match (n:Apartment), (r:Relations_HAS), (d:ApartmentType)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:HAS_TYPE]->(d);

MATCH (n:Relations_HAS) detach delete n;

MATCH (n:Relations_TRADE) detach delete n;
CALL apoc.load.json("$CSV_URI/Relations_TRADE.json") YIELD value AS trade_records
UNWIND trade_records AS record
CREATE (a:Relations_TRADE)
SET a.src = record.auuid
SET a.tar = record.buuid
RETURN count(a);

match (n:ApartmentType), (r:Relations_TRADE), (d:Contract)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:TRADE]->(d);

MATCH (n:Relations_TRADE) detach delete n;

MATCH (n)
RETURN labels(n) as label, COUNT(n) as count
ORDER by label;

MATCH p=()-[r:IN]->() 
RETURN ":IN :" +count(r);

MATCH p=()-[r:HAS_TYPE]->() 
RETURN ":HAS_TYPE :" +count(r);
// count for IN relationship
MATCH p=()-[r:TRADE]->() 
RETURN ":TRADE :" +count(r);

MATCH p=()-[r:IN]->() 
RETURN count(r);

Match(r:Reputation) detach delete (r);
CALL apoc.load.json("$CSV_URI/bt_apt_theme.json") YIELD value AS reputation_records
WITH reputation_records
UNWIND reputation_records AS reputation
CREATE (r:Reputation {apartment_uuid: reputation.id})
SET r.uuid = "reputation_" + id(r), r += reputation {.*, id: null}
RETURN count(r);

LOAD CSV WITH HEADERS FROM '$CSV_URI/reputation.csv' AS reputation
MATCH (r:Reputation {apartment_uuid: reputation.apartment_uuid})
SET r.uuid = reputation.uuid
RETURN count(r);

match (n:Apartment), (r:Reputation) 
where n.uuid = r.apartment_uuid
create (n)-[:EVALUATE]->(r);

MATCH (s:SpecialPurposeArea) detach delete s;
LOAD CSV WITH HEADERS FROM '$CSV_URI/specialpurposearea.csv' AS spa
CREATE (s:SpecialPurposeArea)
SET s += spa {.*, id: null}
RETURN count(s);

MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/FINAL_of_LEVEL1/districtboundarydong_with_specialpurposearea.csv' AS dws
CREATE (s:districtboundarydong_with_specialpurposearea) 
SET s += dws {.*, id: null}
RETURN count(s);

MATCH (s:SpecialPurposeArea)-[r]-(d:DistrictBoundaryDong) DELETE r;
MATCH (n:districtboundarydong_with_specialpurposearea), (s:SpecialPurposeArea), (d:DistrictBoundaryDong)
WHERE (n.uuid_specialpurposearea = s.uuid)
AND (n.uuid_districtboundarydong = d.uuid)
CREATE (s)-[:IN]->(d);

MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;


MATCH (n)
RETURN labels(n) as Label, count(*) as count;

MATCH (n)
RETURN count(*) as TOTAL_nodes;

MATCH ()-[r]->()
RETURN type(r) AS Relationship_type, count(*) AS count;


MATCH ()-[r]->()
RETURN count(r) AS TOTAL_relationship;


EOF
}


# Run the function to create the Cypher query file
create_cypher_query_file
cypher-shell -u $NEO4J_USER -p $NEO4J_PASSWORD -a $NEO4J_URI -f imp.cypher
