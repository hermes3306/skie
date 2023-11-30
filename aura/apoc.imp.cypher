MATCH (n) detach delete n;
CALL apoc.schema.assert({}, {});

CREATE CONSTRAINT FOR (a:Apartment) REQUIRE a.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (r:Region) REQUIRE r.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (at:ApartmentType) REQUIRE at.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (c:Contract) REQUIRE c.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (d:Daycare) REQUIRE d.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (h:Hospital) REQUIRE h.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (k:Kinder) REQUIRE k.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (m:Mart) REQUIRE m.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (p:Park) REQUIRE p.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (s:School) REQUIRE s.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (bs:BusStation) REQUIRE bs.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (gwtw:GoodWayToWalk) REQUIRE gwtw.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (hw:Highway) REQUIRE hw.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (sub:Subway) REQUIRE sub.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (br:BusRoute) REQUIRE br.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (sf:SubwayFuture) REQUIRE sf.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (conv:Convention) REQUIRE conv.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (theater:Theater) REQUIRE theater.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (academy:Academy) REQUIRE academy.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (ds:Departmentstore) REQUIRE ds.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (dbd:DistrictBoundaryDong) REQUIRE dbd.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (dbg:DistrictBoundaryGu) REQUIRE dbg.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (spa:SpecialPurposeArea) REQUIRE spa.neo4jImportId IS UNIQUE;
CREATE CONSTRAINT FOR (rep:Reputation) REQUIRE rep.neo4jImportId IS UNIQUE;


CALL apoc.import.json("alldata.json");
