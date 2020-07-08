from owlready2 import *
from rdflib import Graph, Literal, Namespace, RDF, URIRef, OWL, RDFS
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'  # for reasoning

# define ontology namespace
aff_uri = URIRef("http://test.org/affordance.owl#")
aff_namespace = Namespace(aff_uri)
aff = get_ontology(aff_uri)

# classes
with aff:
    class KitchenEntity(Thing): pass

    class Quality(Thing): pass

    class Affordance(Thing): pass

    class Action(Thing): pass

#qualities
with aff:
    class quality(KitchenEntity>>Quality): pass

    class color(quality):
        range = [str]

    class location(quality):
        range = [str]

    class form(quality):
        range = [str]

    class implies(Quality>>Affordance): pass

# save ontology
aff.save(file = "affordance.owl", format = "rdfxml")

# create graph to store the ontology
aff_g = Graph()
aff_g.bind('aff', aff_namespace)
aff_g.parse("affordance.owl")
# add necessary triples
aff_g.add ( (aff_namespace.Affordance, RDFS.isDefinedBy, aff_namespace.Action) )
# serialize the final affordance ontology graph
aff_g.serialize("aff_graph.ttl", format='turtle')
