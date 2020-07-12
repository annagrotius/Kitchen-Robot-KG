from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import OWL
from owlrl import DeductiveClosure, RDFS_Semantics,OWLRL_Semantics, OWLRL_Extension


# RDFS_Semantics
g = Graph()
g.parse('./graphs/bft_aff_kg.ttl', format='turtle')
DeductiveClosure(RDFS_Semantics).expand(g)
print("RDFS closure of the graph has {} triples".format(len(g))) # RDFS closure of the graph has 491 triples
g.serialize(destination='bft_aff_inferred.ttl', format='turtle')


# OWLRL_Semantics
g1 = Graph()
g1.parse('./graphs/bft_aff_kg.ttl', format='turtle')
DeductiveClosure(OWLRL_Semantics).expand(g1)
print("OWLRL_Semantics closure of the graph has {} triples".format(len(g1))) # OWLRL_Semantics closure of the graph has 845 triples

g1.serialize(destination='bft_aff_inferred_1.ttl', format='turtle')


# OWLRL_Extension
g2 = Graph()
g2.parse('./graphs/bft_aff_kg.ttl', format='turtle')
DeductiveClosure(OWLRL_Extension, rdfs_closure = True, axiomatic_triples = True, datatype_axioms = True).expand(g2)
print("OWLRL_Extension closure of the graph has {} triples".format(len(g2))) # OWLRL_Extension closure of the graph has 2788 triples
g2.serialize(destination='bft_aff_inferred_2.ttl', format='turtle')
