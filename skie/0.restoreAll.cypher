// label외 upload 됨
match (a:ALL) detach delete a;
CALL apoc.load.json("http://1.229.96.163/skie/backup/backup231115.json") YIELD value AS records
UNWIND records AS r
CREATE (a:ALL)
WITH a, r.n.properties AS props, r.n.labels AS labels
SET a = props {.*, coord: null}
SET a.coord = point({latitude: toFloat(props.coord.y), longitude: toFloat(props.coord.x)})
// Add labels to the node based on n.labels[]
FOREACH (label IN labels | SET a:`{$label}`)
RETURN count(a);

// coord 문제 생김
CALL apoc.load.json("http://1.229.96.163/skie/backup/backup231115.json") YIELD value AS records
UNWIND records AS r
// Assuming r.n.labels is an array of labels and r.n.properties is an object with node properties
FOREACH (label IN r.n.labels | 
    MERGE (a:`${label}` {uuid: r.n.properties.uuid})
    SET a += r.n.properties
)

// error 
CALL apoc.load.json("http://1.229.96.163/skie/backup/backup231115.json") YIELD value AS records
UNWIND records AS r
// Exclude 'coord' property from each record
WITH apoc.map.removeKey(r, 'coord') AS cleanedRecord
FOREACH (label IN cleanedRecord.n.labels | 
    MERGE (a:`${label}` {uuid: cleanedRecord.n.properties.uuid})
    SET a += cleanedRecord.n.properties
)

