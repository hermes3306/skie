// 우선 모든 노드를 다운 받아서 json 저장한다.
//  match (n) return n; 이후  json 저장
//  해당 파일을 웹에 올리고 url 확인
//  1) ALL 라벨 생성
CALL apoc.load.json("http://1.229.96.163/skie/backup/sandbox1.json") YIELD value AS records
UNWIND records AS r
CREATE (a:ALL)
WITH a, r.n.properties AS props, r.n.labels AS labels
SET a = props {.*, coord: null}
SET a.coord = point({latitude: toFloat(props.coord.y), longitude: toFloat(props.coord.x)})
// Add labels to the node based on n.labels[]
RETURN count(a);

// ALL 노드를 제외한 다른 노드 삭제
MATCH (n)
WHERE NOT n:ALL
DETACH DELETE n;

// 2) 각 레이블 별로 규칙을 확인하여 노드 생성
MATCH (n:ALL)   WHERE
n.areaCode IS NOT NULL
CREATE (a:Area) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.last_outcome IS NOT NULL AND
n.date IS NOT NULL
CREATE (a:Crime) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.email_address is not null
CREATE (a:Email) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.postcode is not null
CREATE (a:Location) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.surname is not null
AND n.rank is not null
CREATE (a:Officer) SET a = n RETURN a;

MATCH (n:ALL)   WHERE
n.nhs_no is not null
CREATE (a:Person) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.phoneNo is not null
CREATE (a:Phone) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.call_time is not null
CREATE (a:PhoneCall) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.code is not null
CREATE (a:PostCode) SET a = n RETURN a;

MATCH (n:ALL)	WHERE 
n.model is not null
CREATE (a:Vehicle) SET a = n RETURN a;


// RELATION SETUP -HAS_TYPE
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/backup/sandbox1_rel.csv' AS row
CALL
{
	WITH row
	MATCH (p {uuid: row.src})
	MATCH (q:ApartmentType  {uuid: row.tar})
	WHERE row.rel="HAS_TYPE"
	MERGE (p)-[r:HAS_TYPE]->(q)
} IN TRANSACTIONS OF 500 ROWS;


// id값을 연결해야 한다.


// RELATION SETUP - EVALUATE
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/backup/backup_20231118_2.csv' AS row
CALL
{
	WITH row
	MATCH (p {uuid: row.src})
	MATCH (q:Reputation {uuid: row.tar})
	WHERE row.rel="EVALUATE"
	MERGE (p)-[r:EVALUATE]->(q)
} IN TRANSACTIONS OF 500 ROWS;

// RELATION SETUP - IN
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/backup/backup_20231118_2.csv' AS row
CALL
{
	WITH row
	MATCH (p {uuid: row.src})
	MATCH (q:DistrictBoundaryDong  {uuid: row.tar})
	WHERE row.rel="IN"
	MERGE (p)-[r:IN]->(q)
} IN TRANSACTIONS OF 500 ROWS;


// RELATION SETUP - TRADE
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/backup/backup_20231118_2.csv' AS row
CALL
{
	WITH row
	MATCH (p {uuid: row.src})
	MATCH (q:Contract  {uuid: row.tar})
	WHERE row.rel="TRADE"
	MERGE (p)-[r:TRADE]->(q)
} IN TRANSACTIONS OF 500 ROWS;
