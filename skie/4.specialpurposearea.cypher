// Load CSV and update existing Reputation nodes
MATCH (s:SpecialPurposeArea) detach delete s;
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/json/specialpurposearea.csv' AS spa
CREATE (s:SpecialPurposeArea)
SET s += spa {.*, id: null}
RETURN count(s);

MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;
LOAD CSV WITH HEADERS FROM 'http://1.229.96.163/skie/FINAL_of_Level1/districtboundarydong_with_specialpurposearea.csv' AS dws
CREATE (s:districtboundarydong_with_specialpurposearea) 
SET s += dws {.*, id: null}
RETURN count(s);

MATCH (s:`SpecialPurposeArea`)-[r]-(d:`DistrictBoundaryDong`) DELETE r;
MATCH (n:`districtboundarydong_with_specialpurposearea`), (s:`SpecialPurposeArea`), (d:`DistrictBoundaryDong`)
WHERE (n.`uuid_specialpurposearea` = s.`uuid`)
AND (n.`uuid_districtboundarydong` = d.`uuid`)
CREATE (s)-[:IN]->(d);

MATCH (s:districtboundarydong_with_specialpurposearea) detach delete s;
MATCH (s:`SpecialPurposeArea`)-[r]-(d:`DistrictBoundaryDong`) return s,d;





