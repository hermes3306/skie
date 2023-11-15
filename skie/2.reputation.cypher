// before add reputation 
match (n:Apartment) return "BEFORE: number of Properties of Apartment: " + count(distinct keys(n));

// Merge Apartment with reputations
CALL apoc.load.json("http://1.229.96.163/skie/json/bt_apt_theme.json") YIELD value AS reputation_records
UNWIND reputation_records AS reputation
MATCH (a:Apartment {uuid: reputation.id})
SET a += reputation {.*, id: null}
WITH DISTINCT a
RETURN count(a);

// after add reputation 
match (n:Apartment) return "AFTER: number of Properties of Apartment: " + count(distinct keys(n));

