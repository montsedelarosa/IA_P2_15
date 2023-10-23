# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install rdflib

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Crear un grafo RDF
g = Graph()

# Definir recursos y propiedades
persona = URIRef("http://example.org/persona")
nombre = URIRef("http://example.org/nombre")
edad = URIRef("http://example.org/edad")

# Agregar triples RDF a la ontología
g.add((persona, RDF.type, RDFS.Class))
g.add((nombre, RDF.type, RDF.Property))
g.add((edad, RDF.type, RDF.Property))
g.add((persona, RDFS.subClassOf, RDFS.Resource))
g.add((nombre, RDFS.domain, persona))
g.add((nombre, RDFS.range, RDFS.Literal))
g.add((edad, RDFS.domain, persona))
g.add((edad, RDFS.range, RDFS.Literal))

# Agregar datos a la ontología
juan = URIRef("http://example.org/juan")
g.add((juan, RDF.type, persona))
g.add((juan, nombre, Literal("Juan Pérez")))
g.add((juan, edad, Literal(30)))

# Consultar la ontología
consulta = g.query(
    """
    SELECT ?nombre ?edad
    WHERE {
        ?s rdf:type :persona ;
           :nombre ?nombre ;
           :edad ?edad .
    }
    """
)

for resultado in consulta:
    print(f"Nombre: {resultado.nombre}, Edad: {resultado.edad}")
