from owlready2 import *
import owlready2
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'
from rdflib import Graph, Namespace, RDF, URIRef, RDFS

# get ontologies to use OWLReady reasoner
aff_onto = get_ontology("../ontologies/affordance/affordance.owl").load()
bft_onto = get_ontology("../ontologies/bft/bft.owl").load()

# print(list(aff_onto.classes()))
# print(list(aff_onto.individuals()))
#
# print(list(bft_onto.classes()))
# print(list(bft_onto.individuals()))

# onto = bft_onto.imported_ontologies.append(aff_onto) # did not work

# print(list(onto.classes()))
bft_aff_inferred = get_ontology("http://test.org/bft_aff_inferred.owl")
with bft_aff_inferred:
    sync_reasoner([bft_onto, aff_onto], infer_property_values = True)

bft_aff_inferred.save('test.owl')

# print(bft_aff_inferred.get_children_of(bft.KitchenEntity))
# print(list(bft_aff_inferred.individuals()))
