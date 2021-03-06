"""
This script creates the affordance ontology and saves a non closed world
version of the ontology as an owl file format and different graph file formats (.ttl, .nt).
"""

from owlready2 import *
from rdflib import Graph, Literal, Namespace, RDF, URIRef, OWL, RDFS
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'  # for reasoning


def onto_to_graph(ontology, ontology_namespace, ontology_prefix, filename):
    """
    Args:
        - ontology: ontology to be parsed
        - ontology_namespace: namespace of the ontology
        - ontology_prefix: prefix of the ontology
        - filename: filename under which to name the ontology
    Output: An ontology saved as an ntriple file and  ttl file.
    """
    ontology.save(file = f'{filename}.owl', format = "rdfxml")
    g = Graph()
    g.bind(ontology_prefix, ontology_namespace)
    g.parse(f'{filename}.owl')
    g.serialize(f'{filename}.ttl', format='turtle')
    g.serialize(f'{filename}.nt', format='ntriples')


def main():
    # define ontology namespace
    aff_uri = URIRef("http://test.org/affordance.owl#")
    aff = get_ontology(aff_uri)
    aff_namespace = Namespace(aff_uri)

    # classes
    with aff:
        class KitchenEntity(Thing): pass

        class Quality(Thing): pass

        class Affordance(Thing): pass

        class Action(Thing): pass

    # properties
    with aff:
        class potential_action(ObjectProperty, KitchenEntity>>Action): pass

        class quality(ObjectProperty, KitchenEntity>>Quality): pass

        class action_affordance(ObjectProperty, Action>>Affordance): pass

        class affords(KitchenEntity>>Affordance, ObjectProperty):  pass

    # save ontology not closing the world
    onto_to_graph(aff, aff_namespace, 'aff', 'aff_onto_not_closed')


if __name__ == "__main__":
    main()
