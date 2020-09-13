"""
This script takes two ontologies, parses them into graphs, and then merges these graphs. The ontologies used in this script are
the bft and affordance ontologies.
"""
from rdflib import Graph, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import OWL


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


def get_graph(ontology_file, onto_namespace, onto_prefix):
    """
    Creates a graph from a given ontology.
    Args:
        - ontology_file: file with triples to be parsed into graph object
        - onto_namespace: the ontology's namespace
        - onto_prefix: the ontology's given prefix
    Output: a graph object with ontology axioms
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
    classes = ['Drink', 'Food', 'Furniture', 'Kitchenware', 'Storage']
    for c in classes:
        uri_string = f'http://test.org/bft.owl#{c}'
        merged_g.add( (URIRef(uri_string), RDFS.subClassOf, URIRef('http://test.org/affordance.owl#KitchenEntity')) )
        # merged_g.add( (URIRef(f'http://test.org/bft.owl#KitchenEntity'), OWL.equivalentClass, URIRef('http://test.org/affordance.owl#KitchenEntity')) )

    # remove the ontology declarations
    merged_g.remove( (None, RDF.type, OWL.Ontology) )
    # merged_g.remove( (URIRef('http://test.org/affordance.owl'), RDF.type, OWL.Ontology) )
    # merged_g.remove( (URIRef('http://test.org/bft.owl'), RDF.type, OWL.Ontology) )
    # bft_aff_ns = create_namespace(merged_g,'http://test.org/kchn.owl#', 'kchn')
    kchn_ns = create_namespace(merged_g, 'http://test.org/kitchen.owl#', 'kchn')
    merged_g.add( (URIRef('http://test.org/kitchen.owl'), RDF.type, OWL.Ontology) )
    print("Merged graphs have {} triples".format(len(merged_g)))
    file_format = output_filename[3:].split('.')[1]

    if file_format == 'owl':
        file_format = 'xml'

    merged_g.serialize(destination= f'{output_filename}', format=file_format)

    return


def main():

    open_aff_onto_file = "../ontologies/affordance/aff_onto_not_closed.ttl"
    open_bft_onto_file = "../ontologies/bft/bft_onto_not_closed.ttl"

    aff_open_g = get_graph(open_aff_onto_file, "http://test.org/affordance.owl#", 'aff')
    bft_open_g = get_graph(open_bft_onto_file, "http://test.org/bft.owl#", 'bft')
    merge_graphs(aff_open_g, bft_open_g, output_filename='./graphs/aff_bft_open_graph.ttl')


    return


if __name__ == "__main__":
    main()
