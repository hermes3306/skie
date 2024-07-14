from neo4j import GraphDatabase

# Neo4j connection details
neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_password = "neo4jpassword"

neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

q1="""
MATCH (n) DETACH DELETE n
"""

q2="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Apartment.json") YIELD value AS records1
UNWIND records1 AS apartment
CREATE (a:Apartment)
WITH a, apartment.n.properties as apartmentProperties
SET a = apartmentProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(apartmentProperties.coord.y), longitude: toFloat(apartmentProperties.coord.x)})
"""

q3="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Academy.json") YIELD value AS records2
UNWIND records2 AS record
CREATE (a:Academy)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q4="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/ApartmentType.json") YIELD value AS records3
UNWIND records3 AS record
CREATE (a:ApartmentType)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q5="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/BusStation.json") YIELD value AS records4
UNWIND records4 AS record
CREATE (a:BusStation)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q6="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Contract.json") YIELD value AS records5
UNWIND records5 AS record
CREATE (a:Contract)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q7="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Convention.json") YIELD value AS records6
UNWIND records6 AS record
CREATE (a:Convention)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q8="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Daycare.json") YIELD value AS records7
UNWIND records7 AS record
CREATE (a:Daycare)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q9="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Departmentstore.json") YIELD value AS records8
UNWIND records8 AS record
CREATE (a:Departmentstore)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q10="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/DistrictBoundaryDong.json") YIELD value AS records9
UNWIND records9 AS record
CREATE (a:DistrictBoundaryDong)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q11="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/DistrictBoundaryGu.json") YIELD value AS records10
UNWIND records10 AS record
CREATE (a:DistrictBoundaryGu)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q12="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/GoodWayToWalk.json") YIELD value AS records11
UNWIND records11 AS record
CREATE (a:GoodWayToWalk)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q13="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Highway.json") YIELD value AS records12
UNWIND records12 AS record
CREATE (a:Highway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q14="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Hospital.json") YIELD value AS records13
UNWIND records13 AS record
CREATE (a:Hospital)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q15="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Kinder.json") YIELD value AS records14
UNWIND records14 AS record
CREATE (a:Kinder)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q16="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Mart.json") YIELD value AS records15
UNWIND records15 AS record
CREATE (a:Mart)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q17="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Park.json") YIELD value AS records16
UNWIND records16 AS record
CREATE (a:Park)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q18="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/School.json") YIELD value AS records17
UNWIND records17 AS record
CREATE (a:School)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q19="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Subway.json") YIELD value AS records18
UNWIND records18 AS record
CREATE (a:Subway)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q20=""" CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/SubwayFuture.json") YIELD value AS records19
UNWIND records19 AS record
CREATE (a:SubwayFuture)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q21="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Theater.json") YIELD value AS records20
UNWIND records20 AS record
CREATE (a:Theater)
WITH a, record.n.properties as myProperties
SET a = myProperties {.*, coord: null}
SET a.coord = point({latitude: toFloat(myProperties.coord.y), longitude: toFloat(myProperties.coord.x)})
"""

q22="""MATCH (n:Relations_IN) detach delete n;"""

q22_1="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Relations_IN.json") YIELD value AS records21
UNWIND records21 AS record
CREATE (a:Relations_IN)
SET a.src = record.`n.uuid`
SET a.tar = record.`d.uuid`
"""

q23="""match (n), (r:Relations_IN), (d:DistrictBoundaryDong)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:IN]->(d)
"""

q24="""MATCH (n:Relations_IN) detach delete n"""

q25="""MATCH (n:Relations_HAS) detach delete n"""

q26="""CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Relations_HAS.json") YIELD value AS has_records
UNWIND has_records AS record
CREATE (a:Relations_HAS)
SET a.src = record.auuid
SET a.tar = record.buuid
"""

q27="""
match (n:Apartment), (r:Relations_HAS), (d:ApartmentType)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:HAS_TYPE]->(d)
"""

q28="""
MATCH (n:Relations_HAS) detach delete n
"""

q29="""
MATCH (n:Relations_TRADE) detach delete n;"""

q29_1="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/Relations_TRADE.json") YIELD value AS trade_records
UNWIND trade_records AS record
CREATE (a:Relations_TRADE)
SET a.src = record.auuid
SET a.tar = record.buuid
"""

q30="""
match (n:ApartmentType), (r:Relations_TRADE), (d:Contract)
where n.uuid = r.src and d.uuid= r.tar
create (n)-[:TRADE]->(d)
"""

q31="""
MATCH (n:Relations_TRADE) detach delete n
"""

q40="""
Match(r:Reputation) detach delete (r);
"""

q41="""
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/bt_apt_theme.json") YIELD value AS reputation_records
WITH reputation_records
UNWIND reputation_records AS reputation
CREATE (r:Reputation {apartment_uuid: reputation.id})
SET r.uuid = "reputation_" + id(r), r += reputation {.*, id: null}
"""

q42="""
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/reputation.csv' AS reputation
MATCH (r:Reputation {apartment_uuid: reputation.apartment_uuid})
SET r.uuid = reputation.uuid
"""

q43="""
match (n:Apartment), (r:Reputation) 
where n.uuid = r.apartment_uuid
create (n)-[:EVALUATE]->(r);
"""

q50="""
MATCH (s:SpecialPurposeArea) detach delete s;
"""

q51="""
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/specialpurposearea.csv' AS spa
CREATE (s:SpecialPurposeArea)
SET s += spa {.*, id: null}
"""

q52="""
MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;"""

q52_1="""
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/FINAL_of_Level1/districtboundarydong_with_specialpurposearea.csv' AS dws
CREATE (s:districtboundarydong_with_specialpurposearea) 
SET s += dws {.*, id: null}
"""

q53="""
MATCH (s:`SpecialPurposeArea`)-[r]-(d:`DistrictBoundaryDong`) DELETE r;
"""

q54="""
MATCH (n:`districtboundarydong_with_specialpurposearea`), (s:`SpecialPurposeArea`), (d:`DistrictBoundaryDong`)
WHERE (n.`uuid_specialpurposearea` = s.`uuid`)
AND (n.`uuid_districtboundarydong` = d.`uuid`)
CREATE (s)-[:IN]->(d)
"""

q55="""
MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;
"""


queries = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,
           q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,
           q21,q22,q22_1,q23,q24,q25,q26,q27,q28,q29,q29_1,q30,q31,
           q40,q41,q42,q43,
           q50,q51,q52_1,q52,q53,q54,q55]


def data(tx):
    for query in queries:
      tx.run(query)
      print(query)
       
with neo4j_driver.session() as session:
    session.write_transaction(data)

neo4j_driver.close()