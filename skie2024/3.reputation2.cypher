// json 파일 처리 - 한계가 있음. 
Match(r:Reputation) detach delete (r);
CALL apoc.load.json("https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/bt_apt_theme.json") YIELD value AS reputation_records
WITH reputation_records
UNWIND reputation_records AS reputation
CREATE (r:Reputation {apartment_uuid: reputation.id})
SET r.uuid = "reputation_" + id(r), r += reputation {.*, id: null}
RETURN count(r);
match (r:Reputation) return count(r);

// Load CSV and update existing Reputation nodes
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/hermes3306/skie/main/skie_home/json/reputation.csv' AS reputation
MATCH (r:Reputation {apartment_uuid: reputation.apartment_uuid})
SET r.uuid = reputation.uuid
RETURN count(r);

// RELATION EVALUATE
match (n:Apartment), (r:Reputation) 
where n.uuid = r.apartment_uuid
create (n)-[:EVALUATE]->(r);



