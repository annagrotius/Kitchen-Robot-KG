from owlready2 import *
import owlready2
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'
# from rdflib import Graph, Namespace, RDF, URIRef, RDFS

# get ontology to use OWLReady reasoner
bft_aff_onto = get_ontology("../graphs/aff_bft_closed_graph.nt").load()

print(list(bft_aff_onto.classes()))
print(list(bft_aff_onto.individuals()))

with bft_aff_onto:
    sync_reasoner(infer_property_values = True)

bft_aff_onto.save('bft_aff_inferred.owl')


# * Owlready2 * Warning: optimized Cython parser module 'owlready2_optimized' is not available, defaulting to slower Python implementation
# [aff_bft_closed_graph.nt.Tableware, aff_bft_closed_graph.nt.Chair, affordance.Action, aff_bft_closed_graph.nt.Plate, aff_bft_closed_graph.nt.Condiment, aff_bft_closed_graph.nt.Food, aff_bft_closed_graph.nt.Spread, aff_bft_closed_graph.nt.Kitchenware, aff_bft_closed_graph.nt.Coffee, aff_bft_closed_graph.nt.Drink, aff_bft_closed_graph.nt.Milk, affordance.Quality, affordance.KitchenEntity, aff_bft_closed_graph.nt.Cutlery, aff_bft_closed_graph.nt.Storage, aff_bft_closed_graph.nt.Egg, aff_bft_closed_graph.nt.Glassware, aff_bft_closed_graph.nt.Knife, aff_bft_closed_graph.nt.Furniture, aff_bft_closed_graph.nt.Fork, affordance.Affordance, aff_bft_closed_graph.nt.Spoon, aff_bft_closed_graph.nt.Juice, aff_bft_closed_graph.nt.Bread, aff_bft_closed_graph.nt.Tea, aff_bft_closed_graph.nt.Table]
# [aff_bft_closed_graph.nt.teacup_plate, aff_bft_closed_graph.nt.fried, aff_bft_closed_graph.nt.milk_pitcher, aff_bft_closed_graph.nt.butter, aff_bft_closed_graph.nt.scrambled, aff_bft_closed_graph.nt.croissant, aff_bft_closed_graph.nt.egg_cup, aff_bft_closed_graph.nt.glass, aff_bft_closed_graph.nt.table, aff_bft_closed_graph.nt.orange_juice, aff_bft_closed_graph.nt.dining_chair, aff_bft_closed_graph.nt.pepper_shaker, aff_bft_closed_graph.nt.sauce_dish, aff_bft_closed_graph.nt.bread_basket, aff_bft_closed_graph.nt.hardboiled, aff_bft_closed_graph.nt.garnish, aff_bft_closed_graph.nt.butter_knife, aff_bft_closed_graph.nt.cupboard, aff_bft_closed_graph.nt.teacup, aff_bft_closed_graph.nt.salt_shaker, aff_bft_closed_graph.nt.apple_juice, aff_bft_closed_graph.nt.butter_dish, aff_bft_closed_graph.nt.bread_plate]
# * Owlready2 * Running HermiT...
#     C:\Program Files\Java\jre1.8.0_191\bin\java.exe -Xmx2000M -cp C:\Users\annag\AppData\Roaming\Python\Python37\site-packages\owlready2\hermit;C:\Users\annag\AppData\Roaming\Python\Python37\site-packages\owlready2\hermit\HermiT.jar org.semanticweb.HermiT.cli.CommandLine -c -O -D -I file:///C:/Users/annag/AppData/Local/Temp/tmpyid6w7is -Y
# * Owlready2 * HermiT took 1.9949958324432373 seconds
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Drink aff_bft_closed_graph.nt.Juice
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Juice aff_bft_closed_graph.nt.Drink
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Condiment aff_bft_closed_graph.nt.Spread
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Spread aff_bft_closed_graph.nt.Condiment
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Cutlery aff_bft_closed_graph.nt.Knife
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Knife aff_bft_closed_graph.nt.Cutlery
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Coffee owl.Nothing
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Fork owl.Nothing
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Milk owl.Nothing
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Spoon owl.Nothing
# * Owlready * Equivalenting: aff_bft_closed_graph.nt.Tea owl.Nothing
# * Owlready * Equivalenting: affordance.KitchenEntity bft.KitchenEntity
# * Owlready * Equivalenting: bft.KitchenEntity affordance.KitchenEntity
# * Owlready * Reparenting aff_bft_closed_graph.nt.Spread: {aff_bft_closed_graph.nt.Condiment} => {aff_bft_closed_graph.nt.Food}
# * Owlready * Reparenting aff_bft_closed_graph.nt.butter: {aff_bft_closed_graph.nt.Spread} => {aff_bft_closed_graph.nt.Condiment, aff_bft_closed_graph.nt.Spread}
# * Owlready * (NB: only changes on entities loaded in Python are shown, other changes are done but not listed)
