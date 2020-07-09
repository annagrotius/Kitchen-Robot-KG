from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import OWL
from owlrl import DeductiveClosure, RDFS_Semantics


def create_namespace(graph, namespace, prefix):
    """
    Input: a graph Object, namespace URI, prefix for the namespace
    Output: namespace instance bound to a specified graph
    """
    ns = Namespace(namespace)
    graph.namespace_manager.bind(prefix, namespace)

    return ns


def reasoner(g, filename):
    """
    Input: a graph Object, filename for output
    Output: a file saved in specified destination
    """
    DeductiveClosure(RDFS_Semantics).expand(g)
    print("RDFS closure of the graph has {} triples".format(len(g)))
    g.serialize(destination=filename, format='turtle')

    return


def main():

    affordance_g = Graph()
    aff_ns = create_namespace(affordance_g,"http://test.org/affordance.owl#", 'aff')
    bft_g = Graph()
    bft_ns = create_namespace(bft_g,"http://test.org/bft.owl#", 'bft')

    affordance_g.parse("../ontologies/affordance/aff_graph.ttl", format="ttl")
    bft_g.parse("../ontologies/bft/bft_graph.ttl", format="ttl")

    merged_g = bft_g + affordance_g
    classes = ['Condiment', 'Cutlery', 'Drink', 'Food', 'Furniture', 'Kitchenware', 'Tableware']
    for bft_class in classes:
        uri_string = f'http://test.org/bft.owl#{bft_class}'
        merged_g.add( (URIRef(f'http://test.org/bft.owl#KitchenEntity'), OWL.sameAs, URIRef('http://test.org/affordance.owl#KitchenEntity')) )


    print("Affordance graph has {} triples".format(len(affordance_g)))
    print("Bft graph has {} triples".format(len(bft_g)))
    print("Merged graphs have {} triples".format(len(merged_g)))
    print("\n")

    merged_g.serialize(destination='./graphs/bft_aff_kg.ttl', format='turtle')

    reasoner(merged_g)


if __name__ == "__main__":
    main()
