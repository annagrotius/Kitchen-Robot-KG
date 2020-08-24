# Code Based On: https://github.com/r4isstatic/csv-to-ttl/blob/master/uber.py
import csv
import glob
from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF, XSD, RDFS
from utils import create_namespace


# initialize graph
cn_graph = Graph()

# define namespaces
# cn = create_namespace(cn_graph, "http://api.conceptnet.io/", 'cn')
cnc = create_namespace(cn_graph, "http://api.conceptnet.io/c/", 'cnc')
cnr = create_namespace(cn_graph, "http://api.conceptnet.io/r/", 'cnr')
# wi = create_namespace(cn_graph, "http://purl.org/ontology/wi/core#", 'wi')

# read csv files with concept net data and add the triples to a graph
for file in glob.glob(f'../cn_data/filtered_data/*.csv'):
    ifile = open(file, 'rt', encoding="utf8")
    reader = csv.reader(ifile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            pass
        else:
            # concept1 = URIRef(cnc[uri_encode(row[1][3:])])
            concept1_str = row[1][3:]
            # print(concept1_str)
            concept1 = URIRef(cnc[concept1_str])
            # print('CONCEPT1', row[1][3:])
            # print('c1:', concept1)
            # concept2 = URIRef(cnc[uri_encode(row[4][3:])])
            concept2_str = row[4][3:]
            concept2 = URIRef(cnc[concept2_str])
            # print('c2:', concept2)
            relation = URIRef(cnr[row[2]])
            # assertion = URIRef(cn + 'a/[/r/' + row[2] + '/,' + row[1] + '/,' + row[4] + '/]')
            # if 'ExternalURL' in assertion:
            if 'ExternalURL' in relation:
                # print(concept2)
                # assertion = URIRef(cn + 'a/[/r/' + row[2] + '/,' + row[1] + '/,/' + row[4] + '/]')
                concept2 = URIRef(row[4])

                # print("NEW", concept2)
            # surface_text = row[5]
            # weight = row[6]
            # cn_graph.add( (assertion, RDF.type, RDF.Statement) )
            # cn_graph.add( (assertion, RDF.subject, concept1) )
            # cn_graph.add( (assertion, RDF.object, concept2) )
            # cn_graph.add( (assertion, RDF.predicate, relation) )
            # cn_graph.add( (concept1, RDF.type, RDFS.Resource) )
            # cn_graph.add( (concept2, RDF.type, RDFS.Resource) )
            # cn_graph.add( (assertion, RDF.value, Literal(surface_text)) )
            # cn_graph.add( (assertion, wi.evidence, Literal(weight, datatype=XSD.decimal)) )
            cn_graph.add( (concept1, relation, concept2) )
        rownum += 1
    ifile.close()


print(len(cn_graph))
complete_cn_graph = cn_graph.serialize('cn_graph.ttl', format='turtle')
