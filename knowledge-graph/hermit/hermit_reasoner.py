from owlready2 import *
import owlready2
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'
from rdflib import Graph, Namespace, URIRef



def create_namespace(graph, namespace, prefix):
    """
    Binds a namespace to a given graph.
    Args:
        - graph: graph object
        - namespace: uri of the namespace to be bound to the graph
        - prefix: the prefix of the given namespace
    Output: namespace instance bound to a specified graph
    """
    ns = Namespace(namespace)
    graph.namespace_manager.bind(prefix, namespace)

    return ns

# # get CLOSED ontology to use OWLReady reasoner
# bft_aff_onto = get_ontology("../graphs/aff_bft_closed_graph.nt").load()
#
# # print(list(bft_aff_onto.classes()))
# # print(list(bft_aff_onto.individuals()))
#
# with bft_aff_onto:
#     sync_reasoner(infer_property_values = True)
# bft_aff_onto.save('bft_aff_closed_inferred_hermit.owl')
#
# print('---------------------CLOSED WORLD---------------------')
# print("INCONSISTENT CLASSES: ", list(default_world.inconsistent_classes()))
# print(bft_aff_onto.get_parents_of(bft_aff_onto.Egg))
#
# # get OPEN ontology to use OWLReady reasoner
# bft_aff_onto = get_ontology("../graphs/aff_bft_open_graph.nt").load()
#
# # print(list(bft_aff_onto.classes()))
# # print(list(bft_aff_onto.individuals()))
#
# with bft_aff_onto:
#     sync_reasoner(infer_property_values = True)
# bft_aff_onto.save('bft_aff_open_inferred_hermit.owl')
#
# print('---------------------OPEN WORLD---------------------')
# print("INCONSISTENT CLASSES: ", list(default_world.inconsistent_classes()))
# print()
#
# # save ontology as a graph (i.e. turtle file)
# graph_closed = Graph()
# bft_namespace = create_namespace(graph_closed, "http://test.org/bft.owl#", 'bft')
# aff_namespace = create_namespace(graph_closed, "http://test.org/affordance.owl#", 'aff')
# # comment next line so that the graph has no namespace
# kitchen_kg_namespace = create_namespace(graph_closed, "../graphs/aff_bft_closed_graph.nt#", 'kitchen_kg')
# graph_closed.parse("bft_aff_closed_inferred_hermit.owl")
# # graph.serialize("bft_aff_inferred_hermit_NO_NS.ttl", format = 'turtle')
# print("Hermit reasoner over closed graph has {} triples".format(len(graph_closed)))
# graph_closed.serialize("bft_aff_closed_inferred_hermit.ttl", format = 'turtle')
#
#
# graph_open = Graph()
# bft_namespace = create_namespace(graph_open, "http://test.org/bft.owl#", 'bft')
# aff_namespace = create_namespace(graph_open, "http://test.org/affordance.owl#", 'aff')
# # comment next line so that the graph has no namespace
# kitchen_kg_namespace = create_namespace(graph_open, "../graphs/aff_bft_open_graph.nt#", 'kitchen_kg')
# graph_open.parse("bft_aff_open_inferred_hermit.owl")
# print("Hermit reasoner over open graph has {} triples".format(len(graph_open)))
# # graph.serialize("bft_aff_inferred_hermit_NO_NS.ttl", format = 'turtle')
# graph_open.serialize("bft_aff_open_inferred_hermit.ttl", format = 'turtle')


def hermit_reasoner(onto_file, inferred_onto_filename):
    """
    Runs the Hermit reasoner on a given ontology.
    Args:
        - onto_file: ontology file to be used
        - inferred_onto_filename: name of output file that includes asserted and inferred triples
    Returns: file with asserted and inferred triples
    """
    onto = get_ontology(onto_file).load()
    with onto:
        # print some stuff to demonstrate the daat before bft_aff_inferred
        sync_reasoner(infer_property_values = True)
    onto.save(f'{inferred_filename}'.owl)

    # print stuff to prove inferred info

def main():

    # CLOSED ONTO
    hermit_reasoner(....)
    # save ontology as a graph (i.e. turtle file)
    graph_closed = Graph()
    bft_namespace = create_namespace(graph_closed, "http://test.org/bft.owl#", 'bft')
    aff_namespace = create_namespace(graph_closed, "http://test.org/affordance.owl#", 'aff')
    # comment next line so that the graph has no namespace
    kitchen_kg_namespace = create_namespace(graph_closed, "../graphs/aff_bft_closed_graph.nt#", 'kitchen_kg')
    graph_closed.parse("bft_aff_closed_inferred_hermit.owl")
    # graph.serialize("bft_aff_inferred_hermit_NO_NS.ttl", format = 'turtle')
    print("Hermit reasoner over closed graph has {} triples".format(len(graph_closed)))
    graph_closed.serialize("bft_aff_closed_inferred_hermit.ttl", format = 'turtle')


    # OPEN ONTO
    hermit_reasoner(....)
    # save ontology as a graph (i.e. turtle file)
    graph_open = Graph()
    bft_namespace = create_namespace(graph_open, "http://test.org/bft.owl#", 'bft')
    aff_namespace = create_namespace(graph_open, "http://test.org/affordance.owl#", 'aff')
    # comment next line so that the graph has no namespace
    kitchen_kg_namespace = create_namespace(graph_open, "../graphs/aff_bft_open_graph.nt#", 'kitchen_kg')
    graph_open.parse("bft_aff_open_inferred_hermit.owl")
    print("Hermit reasoner over open graph has {} triples".format(len(graph_open)))
    # graph.serialize("bft_aff_inferred_hermit_NO_NS.ttl", format = 'turtle')
    graph_open.serialize("bft_aff_open_inferred_hermit.ttl", format = 'turtle')
