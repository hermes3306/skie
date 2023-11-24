
match (a:Apartment), (s:School)
with a,s,point.distance(a.coord, s.coord) as d 
where d < 100 
return a.name , s.name, d

