"""
This script creates the affordance ontology and saves a closed world and non closed world
version of the ontology as a owl file format and different graph file formats (.ttl, .nt).
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
    Output: An ontology saves as an ntriple file and  ttl file.
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

        # class Cut(Action): pass

        # class Soft(Quality): pass

        # class SoftAffordance(Affordance): pass

    # properties
    with aff:
        class potential_action(ObjectProperty, KitchenEntity>>Action): pass

        class quality(ObjectProperty, KitchenEntity>>Quality): pass

        # class implies(ObjectProperty, Quality>>Affordance): pass
        # problem i have with this is once I create instances of Quality, will all of those be inferred with Affordance. How would
        # specific qualities be inferred with the respective affordance?

        class superAction(ObjectProperty, Action>>Affordance): pass

        # class affords(ObjectProperty):
        #     equivalent_to = PropertyChain([quality, implies, defines])

        class affords(KitchenEntity>>Affordance, TransitiveProperty):
            # equivalent_to= [superAction]
            equivalent_to= [potential_action, superAction]

    # apple = KitchenEntity("apple")
    # cut = Action("cut")
    # eat = Action("eat")
    # soft = Quality("soft")
    # hard = Quality("hard")
    # eating = Affordance("eating")

    # apple.quality = [hard]
    # apple.potential_action = [eat]
    # eat.superAction = [eating]

    # print(apple.INDIRECT_affords)
    #
    # with aff:
    #     sync_reasoner(infer_property_values = True)
    #
    # print(apple.INDIRECT_affords)

    # save ontology not closing the world
    onto_to_graph(aff, aff_namespace, 'aff', 'aff_onto_not_closed')

    # # closing world and save this version
    # classes = [KitchenEntity, Quality, Affordance, Action, quality, color, location, form, implies, affords]
    # for c in classes:
    #     close_world(c)
    # onto_to_graph(aff, aff_namespace, 'aff', 'aff_onto_closed')


if __name__ == "__main__":
    main()
