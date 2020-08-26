# Code Based On: https://github.com/r4isstatic/csv-to-ttl/blob/master/uber.py
from owlready2 import *
import csv
import glob
from rdflib import URIRef, Namespace, Graph
from rdflib.namespace import RDF
from utils import create_namespace


# create Ontology to organize CN data
cn_uri = "http://test.org/cn.owl#"
cn = get_ontology(cn_uri)
    
with cn:
    
    class Concept(Thing): pass
    class Relation(Thing): pass
    
cn.save(file = 'cn.owl', format = "rdfxml")

# initialize graph and load ontology
cn_graph = Graph()
cn_graph.parse('cn.owl')

# define namespaces
cn_owl = create_namespace(cn_graph, cn_uri, 'cn')
cnc = create_namespace(cn_graph, "http://api.conceptnet.io/c/", 'cnc')
cnr = create_namespace(cn_graph, "http://api.conceptnet.io/r/", 'cnr')

# read csv files with concept net data and add the triples to a graph
for file in glob.glob(f'../cn_data/filtered_data/*.csv'):
    ifile = open(file, 'rt', encoding="utf8")
    reader = csv.reader(ifile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            pass
        else:
            concept1_str = row[1][3:]
            concept1 = URIRef(cnc[concept1_str])
            concept2_str = row[4][3:]
            concept2 = URIRef(cnc[concept2_str])
            relation = URIRef(cnr[row[2]])
            if 'ExternalURL' in relation:
                concept2 = URIRef(row[4])
            cn_graph.add( (concept1, relation, concept2) )
            cn_graph.add( (concept1, RDF.type, cn_owl.Concept) )
            cn_graph.add( (concept2, RDF.type, cn_owl.Concept) )
            cn_graph.add( (relation, RDF.type, cn_owl.Relation) )
        rownum += 1
    ifile.close()


print(len(cn_graph))
complete_cn_graph = cn_graph.serialize('cn_graph.ttl', format='turtle')
