import rdflib

g = rdflib.Graph()
g.parse("Car.ttl", format='ttl')

qres = g.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX base: <http://www.example.org/owl/TypeOfMoterVehicle.owl#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace>
    SELECT  *  WHERE {
         ?x :Use :Personal.	
    }""")
for row in qres:
    print("  %s" % row)
