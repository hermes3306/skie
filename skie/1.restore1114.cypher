MATCH (n) DETACH DELETE n;
// Apartment
CALL apoc.load.json("http://1.229.96.163/skie/json/Apartment.json") YIELD value AS records1
UNWIND records1 AS apartment
CREATE (a:Apartment)
WITH a, apartment.n.properties as apartmentProperties
SET a = apartmentProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(apartmentProperties.coord.y), longitude: toFloat(apartmentProperties.coord.x)})
RETURN count(a);

// ACADEMY
CALL apoc.load.json("http://1.229.96.163/skie/json/Academy.json") YIELD value AS records2
UNWIND records2 AS record
CREATE (a:Academy)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// ApartmentType
CALL apoc.load.json("http://1.229.96.163/skie/json/ApartmentType.json") YIELD value AS records3
UNWIND records3 AS record
CREATE (a:ApartmentType)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// BusStation
CALL apoc.load.json("http://1.229.96.163/skie/json/BusStation.json") YIELD value AS records4
UNWIND records4 AS record
CREATE (a:BusStation)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Contract
CALL apoc.load.json("http://1.229.96.163/skie/json/Contract.json") YIELD value AS records5
UNWIND records5 AS record
CREATE (a:Contract)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);


// Convention
CALL apoc.load.json("http://1.229.96.163/skie/json/Convention.json") YIELD value AS records6
UNWIND records6 AS record
CREATE (a:Convention)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Daycare
CALL apoc.load.json("http://1.229.96.163/skie/json/Daycare.json") YIELD value AS records7
UNWIND records7 AS record
CREATE (a:Daycare)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Departmentstore
CALL apoc.load.json("http://1.229.96.163/skie/json/Departmentstore.json") YIELD value AS records8
UNWIND records8 AS record
CREATE (a:Departmentstore)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// DistrictBoundaryDong
CALL apoc.load.json("http://1.229.96.163/skie/json/DistrictBoundaryDong.json") YIELD value AS records9
UNWIND records9 AS record
CREATE (a:DistrictBoundaryDong)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// DistrictBoundaryGu
CALL apoc.load.json("http://1.229.96.163/skie/json/DistrictBoundaryGu.json") YIELD value AS records10
UNWIND records10 AS record
CREATE (a:DistrictBoundaryGu)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// GoodWayToWalk
CALL apoc.load.json("http://1.229.96.163/skie/json/GoodWayToWalk.json") YIELD value AS records11
UNWIND records11 AS record
CREATE (a:GoodWayToWalk)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Highway
CALL apoc.load.json("http://1.229.96.163/skie/json/Highway.json") YIELD value AS records12
UNWIND records12 AS record
CREATE (a:Highway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Hospital
CALL apoc.load.json("http://1.229.96.163/skie/json/Hospital.json") YIELD value AS records13
UNWIND records13 AS record
CREATE (a:Hospital)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Kinder
CALL apoc.load.json("http://1.229.96.163/skie/json/Kinder.json") YIELD value AS records14
UNWIND records14 AS record
CREATE (a:Kinder)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Mart
CALL apoc.load.json("http://1.229.96.163/skie/json/Mart.json") YIELD value AS records15
UNWIND records15 AS record
CREATE (a:Mart)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Park
CALL apoc.load.json("http://1.229.96.163/skie/json/Park.json") YIELD value AS records16
UNWIND records16 AS record
CREATE (a:Park)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// School
CALL apoc.load.json("http://1.229.96.163/skie/json/School.json") YIELD value AS records17
UNWIND records17 AS record
CREATE (a:School)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Subway
CALL apoc.load.json("http://1.229.96.163/skie/json/Subway.json") YIELD value AS records18
UNWIND records18 AS record
CREATE (a:Subway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// SubwayFuture 
CALL apoc.load.json("http://1.229.96.163/skie/json/SubwayFuture.json") YIELD value AS records19
UNWIND records19 AS record
CREATE (a:SubwayFuture)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Theater 
CALL apoc.load.json("http://1.229.96.163/skie/json/Theater.json") YIELD value AS records20
UNWIND records20 AS record
CREATE (a:Theater)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
RETURN count(a);

// Relation_:IN
MATCH (n:Relations_IN) detach delete n;
CALL apoc.load.json("http://1.229.96.163/skie/json/Relations_IN.json") YIELD value AS records21
UNWIND records21 AS record
CREATE (a:Relations_IN)
SET a.src = record.`n.uuid`
SET a.tar = record.`d.uuid`
RETURN count(a);

// RELATION MAKING
match (n), (r:Relations_IN), (d:DistrictBoundaryDong)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:IN]->(d);

// Delete Relation_:IN 
MATCH (n:Relations_IN) detach delete n;

// Relation_:HAS_TYPE
MATCH (n:Relations_HAS) detach delete n;
CALL apoc.load.json("http://1.229.96.163/skie/json/Relations_HAS.json") YIELD value AS has_records
UNWIND has_records AS record
CREATE (a:Relations_HAS)
SET a.src = record.`a.uuid`
SET a.tar = record.`b.uuid`
RETURN count(a);

// RELATION MAKING
match (n:Apartment), (r:Relations_HAS), (d:ApartmentType)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:HAS_TYPE]->(d);

// Delete Relation_:IN 
MATCH (n:Relations_HAS) detach delete n;

// Relation_:TRADE
MATCH (n:Relations_TRADE) detach delete n;
CALL apoc.load.json("http://1.229.96.163/skie/json/Relations_TRADE.json") YIELD value AS trade_records
UNWIND trade_records AS record
CREATE (a:Relations_TRADE)
SET a.src = record.`a.uuid`
SET a.tar = record.`b.uuid`
RETURN count(a);

// RELATION MAKING
match (n:ApartmentType), (r:Relations_TRADE), (d:Contract)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:TRADE]->(d);

// Delete Relation_:IN 
MATCH (n:Relations_TRADE) detach delete n;

// counnt for each labels
MATCH (n)
RETURN labels(n) as label, COUNT(n) as count
ORDER by label;

// count for IN relationship
MATCH p=()-[r:IN]->() 
RETURN ":IN :" +count(r);
// count for IN relationship
MATCH p=()-[r:HAS_TYPE]->() 
RETURN ":HAS_TYPE :" +count(r);
// count for IN relationship
MATCH p=()-[r:TRADE]->() 
RETURN ":TRADE :" +count(r);

// counnt for each labels
MATCH (n)
RETURN labels(n) as label, COUNT(n) as count
ORDER by label;

// count for IN relationship
MATCH p=()-[r:IN]->() 
RETURN count(r);







