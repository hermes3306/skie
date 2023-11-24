
MATCH (a:Apartment), (s:School) 
WITH 	a, s, a.coord as p1, s.coord as p2 
WHERE 	point.distance(p1,p2) < 100 return a.name, s.name;

