
from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import OWL


def create_namespace(graph, namespace, prefix):
    """
    Args:
        - graph: graph object
        - namespace: uri of the namespace to be bound to the graph
        - prefix: the prefix of the given namespace
    Input: a graph Object, namespace URI, prefix for the namespace
    Output: namespace instance bound to a specified graph
    """
    ns = Namespace(namespace)
    graph.namespace_manager.bind(prefix, namespace)

    return ns


def get_graph(ontology_file, onto_namespace, onto_prefix):
    """
    Args:
        - ontology_file: file with triples to be parsed into graph object
        - onto_namespace: the ontology's namespace
        - onto_prefix: the ontology's given prefix
    """
    g = Graph()
    g_ns = create_namespace(g, onto_namespace, onto_prefix)
    file_format = ontology_file[3:].split('.')[1]
    g.parse(ontology_file, format=file_format)
    print(f'{ontology_file} graph has {len(g)} triples')

    return g


def merge_graphs(graph1, graph2, output_filename='merged_graph.ttl'):
    """
    Args:
        - graph1: a graph object to be merged with another graph
        - graph2: a graph object to be merged with another graph
        - output_filename: (default 'merged_graph.ttl') filename of merged graph file output
    Input: two graph objects.
    Ouput: one merged graph.
    """
    merged_g = graph1 + graph2
    classes = ['Condiment', 'Cutlery', 'Drink', 'Food', 'Furniture', 'Kitchenware', 'Tableware']
    for c in classes:
        uri_string = f'http://test.org/bft.owl#{c}'
        merged_g.add( (URIRef(f'http://test.org/bft.owl#KitchenEntity'), OWL.equivalentClass, URIRef('http://test.org/affordance.owl#KitchenEntity')) )
    print("Merged graphs have {} triples".format(len(merged_g)))
    file_format = output_filename[3:].split('.')[1]
    merged_g.serialize(destination= f'{output_filename}', format=file_format)

    return


def main():

    # closed ontologies
    closed_aff_onto_file = "../ontologies/affordance/aff_onto_closed.ttl"
    closed_bft_onto_file = "../ontologies/bft/bft_onto_closed.ttl"

    aff_closed_g = get_graph(closed_aff_onto_file, "http://test.org/affordance.owl#", 'aff')
    bft_closed_g = get_graph(closed_bft_onto_file, "http://test.org/bft.owl#", 'bft')
    merge_graphs(aff_closed_g, bft_closed_g, output_filename='./graphs/aff_bft_closed_graph.ttl')
    merge_graphs(aff_closed_g, bft_closed_g, output_filename='./graphs/aff_bft_closed_graph.nt')

    # non-closed ontologies
    open_aff_onto_file = "../ontologies/affordance/aff_onto_not_closed.ttl"
    open_bft_onto_file = "../ontologies/bft/bft_onto_not_closed.ttl"

    aff_open_g = get_graph(open_aff_onto_file, "http://test.org/affordance.owl#", 'aff')
    bft_open_g = get_graph(open_bft_onto_file, "http://test.org/bft.owl#", 'bft')
    merge_graphs(aff_open_g, bft_open_g, output_filename='./graphs/aff_bft_open_graph.ttl')
    merge_graphs(aff_open_g, bft_open_g, output_filename='./graphs/aff_bft_open_graph.nt')


    return


if __name__ == "__main__":
    main()
