from owlready2 import *
import csv
import glob
import os
from rdflib import URIRef, Namespace, Graph
from rdflib.namespace import RDF, RDFS
from utils import create_namespace


# create Ontology to organize RecipePuppy data
rp_uri = "http://test.org/recipe.owl#"
rp = get_ontology(rp_uri)
    
with rp:
    
    class Ingredient(Thing): pass
    class Recipe(Thing): pass
    class has_ingredient:
        domain=[Recipe]
        range=[Ingredient]
#         class_property_type = ["min"]
        
#     Recipe.is_a.append(has_ingredient.min(1,Ingredient))
        
rp.save(file = 'rp.owl', format = "rdfxml")


# initialize graph and load ontology
recipe_graph = Graph()
recipe_graph.parse('rp.owl')

# define namespaces
rp_owl = create_namespace(recipe_graph, rp_uri, 'rcp')
rp_ns = create_namespace(recipe_graph, "http://test.org/recipe_puppy#", 'rp')
bft_ns = create_namespace(recipe_graph, "http://test.org/bft.owl#", 'bft')

# read csv files with concept net data and add the triples to a graph
for file in glob.glob(f'./requests_output/*.csv'):
    instance = os.path.basename(file).split('.')[0]
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
            recipe_graph.add( (bft_ns[instance], rp_ns['has_recipe'], rp_ns[recipe]) )
            recipe_graph.add( (rp_ns[recipe], RDF.type, rp_owl.Recipe) )
            for i in range(len(ingredients)):
                if len(ingredients) == 1:
                    break
                if i == len(ingredients)-1:
                    break
                else:
                    recipe_graph.add( (rp_ns[ingredients[0].strip().replace(' ','_').strip()], bft_ns.used_with, rp_ns[ingredients[i+1].strip().replace(' ','_').strip()]) ) 
            recipe_graph.add( (rp_ns[recipe], rp_ns['recipe_URL'], URIRef(recipe_url)) )
            for i in ingredients:
                i_clean = i.strip().replace(' ','_').strip()
                recipe_graph.add( (rp_ns[recipe], rp_ns['ingredient'], rp_ns[i_clean]) )
                recipe_graph.add( (rp_ns[i_clean], RDF.type, rp_owl.Ingredient) )
    
        rownum += 1
    ifile.close()

print(len(recipe_graph))
complete_recipe_graph = recipe_graph.serialize('recipe_graph.ttl', format='turtle')
