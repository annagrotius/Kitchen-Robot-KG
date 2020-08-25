import csv
import glob
from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF, XSD, RDFS
from utils import create_namespace
import uuid


# initialize graph
recipe_graph = Graph()
recipe_puppy_uri = "http://test.org/recipe_puppy"

# define namespaces
rp_ns = create_namespace(recipe_graph, "http://test.org/recipe_puppy#", 'rp')
bft_ns = create_namespace(recipe_graph, "http://test.org/bft.owl#", 'bft')

# read csv files with concept net data and add the triples to a graph
for file in glob.glob(f'./requests_output/*.csv'):
    ifile = open(file, 'rt', encoding="utf8")
    reader = csv.reader(ifile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            pass
        else:
            recipe = row[0]
            recipe_url = row[1]
            ingredients = row[2].split(',')
            for i in range(len(ingredients)):
                if len(ingredients) == 1:
                    break
                if i == len(ingredients)-1:
                    break
                else:
                    recipe_graph.add( (rp_ns[ingredients[0].replace(' ','_').strip()], bft_ns.used_with, rp_ns[ingredients[i+1].replace(' ','_').strip()]) ) 
            recipe_graph.add( (rp_ns[recipe], rp_ns['recipe_URL'], URIRef(recipe_url)) )
            for i in ingredients:
                i_clean = i.strip().replace(' ','_').strip()
                recipe_graph.add( (rp_ns[recipe], rp_ns['ingredient'], rp_ns[i_clean]) )
    
        rownum += 1
    ifile.close()

print(len(recipe_graph))
complete_recipe_graph = recipe_graph.serialize('recipe_graph.ttl', format='turtle')
