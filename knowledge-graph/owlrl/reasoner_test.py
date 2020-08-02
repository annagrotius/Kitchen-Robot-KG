from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import OWL
from owlrl import *
# DeductiveClosure, RDFS_Semantics,OWLRL_Semantics, OWLRL_Extension


def reasoner(graph_file, output_filename, RDFS_Semantics=True, OWLRL_Semantics=False,
OWLRL_Extension=False):
    """
    Args:
        - graph_file: file with triples to be parsed into graph object and run reasoner over
        - output_filename: output filename
        - RDFS_Semantics: (default True; one of owlrl reasoners)
        - OWLRL_Semantics: (default False; one of owlrl reasoners)
        - OWLRL_Extension: (default False; one of owlrl reasoners)
    Input: a graph file, filename for output
    Output: a file saved in specified destination
    """
    g = Graph()
    file_format = graph_file[3:].split('.')[1]
    g.parse(graph_file, format=file_format)

    if RDFS_Semantics:
        DeductiveClosure(RDFSClosure.RDFS_Semantics).expand(g)
        # print("RDFS closure of the graph has {} triples".format(len(g)))
    elif OWLRL_Semantics:
        DeductiveClosure(OWLRL.OWLRL_Semantics).expand(g)
        # print("RDFS closure of the graph has {} triples".format(len(g)))
    # elif OWLRL_Extension:
    #     DeductiveClosure(OWLRL_Extension, rdfs_closure = True,
    #     axiomatic_triples = True, datatype_axioms = True).expand(g)

    print("RDFS closure of the graph has {} triples".format(len(g)))
    g.serialize(destination=f'{output_filename}.ttl', format='turtle')

    return


def main():

    # closed_graph = "../graphs/aff_bft_closed_graph.ttl"
    open_graph = "../graphs/aff_bft_open_graph2.ttl"
    # reasoner(closed_graph, "./closed_rdfs_semantics")
    # reasoner(closed_graph, "./closed_owlrl_semantics", RDFS_Semantics=False, OWLRL_Semantics=True)
    reasoner(open_graph, "./open_rdfs_semantics2")
    reasoner(open_graph, "./open_owlrl_semantics2", RDFS_Semantics=False, OWLRL_Semantics=True)
    # reasoner(closed_graph, "./closed_owlrl_extension.ttl", RDFS_Semantics=False, OWLRL_Semantics=False,
    # OWLRL_Extension=True)

    # open_graph = "../graphs/aff_bft_open_graph.ttl"
    # reasoner(open_graph, "./open_rdfs_semantics.ttl")
    # reasoner(open_graph, "./open_owlrl_semantics.ttl", RDFS_Semantics=False, OWLRL_Semantics=True)
    # reasoner(open_graph, "./open_owlrl_extension.ttl", RDFS_Semantics=False, OWLRL_Semantics=False,
    # OWLRL_Extension=True)


if __name__ == "__main__":
    main()
# # RDFS_Semantics
# g = Graph()
# g.parse('./graphs/bft_aff_kg.ttl', format='turtle')
# DeductiveClosure(RDFS_Semantics).expand(g)
# print("RDFS closure of the graph has {} triples".format(len(g))) # RDFS closure of the graph has 491 triples
# g.serialize(destination='bft_aff_inferred.ttl', format='turtle')
#
#
# # OWLRL_Semantics
# g1 = Graph()
# g1.parse('./graphs/bft_aff_kg.ttl', format='turtle')
# DeductiveClosure(OWLRL_Semantics).expand(g1)
# print("OWLRL_Semantics closure of the graph has {} triples".format(len(g1))) # OWLRL_Semantics closure of the graph has 845 triples
#
# g1.serialize(destination='bft_aff_inferred_1.ttl', format='turtle')
#
#
# # OWLRL_Extension
# g2 = Graph()
# g2.parse('./graphs/bft_aff_kg.ttl', format='turtle')
# DeductiveClosure(OWLRL_Extension, rdfs_closure = True, axiomatic_triples = True, datatype_axioms = True).expand(g2)
# print("OWLRL_Extension closure of the graph has {} triples".format(len(g2))) # OWLRL_Extension closure of the graph has 2788 triples
# g2.serialize(destination='bft_aff_inferred_2.ttl', format='turtle')
