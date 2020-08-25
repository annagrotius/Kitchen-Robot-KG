from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF, XSD


def create_namespace(graph, namespace, prefix):

    ns = Namespace(namespace)
    graph.namespace_manager.bind(prefix, namespace)
    
    return ns


def create_graph(graph_file):
    g = Graph()
    g.parse(graph_file, format="turtle")
    
    return g