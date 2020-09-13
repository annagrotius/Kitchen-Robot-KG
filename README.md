# Kitchen Robot Knowledge Graph
> Knowledge graph enabled vritual reality for a kitchen domain robot


## Introduction
This is the Masters thesis project of Anna de Groot as a part of the MSc AI program at the Vrije Universiteit, Amsterdam. The project investigates the use of structured sources from the web to create a knowledge graph that can provide kitchen-related commonsense information to a kitchen domain robot. Specifically, information is extracted from [ConceptNet](http://conceptnet.io/) and the [RecipePuppy API](http://www.recipepuppy.com/about/api/). After a knowledge graph prototype is built, it is implemented in a virtual reality game application (see images below). The project was completed in collaboration with the Institute of Artificial Intelligence at the University of Bremen (<https://ai.uni-bremen.de/>). 

<p float="left">
  <img src="./MR-App/screen_shots/game_scene.PNG" width="400">
  <img src="/MR-App/screen_shots/milk_qua.PNG" width="400" /> 
</p>

## Implementation Details
Python 3.7 was used for building the knowledge graph. The main Python libraries used are [RDFLib](https://rdflib.readthedocs.io/en/stable/) and [Owlready2](https://owlready2.readthedocs.io/en/latest/). [SpaCy](https://spacy.io/) was also used for some natural language preprocessing.
The VR application was built using the Unity game engine (version 2018.4.26) with the programming language C\#. The knowledge graph's data is stored in the linked data host by [TriplyDB](https://triplydb.com/) and data is retrieved through REST API calls. Through Triply's query service, RDFS and OWL reasoning are applied over the graphs for certain queries.  

## Content

* MR-App/ contains: C# scripts for the game and the Unity game scene file.  
* ontologies/ contains: 
	* aff/ : script that creates the Affordance Ontology. Ontology is saved as a .nt, .ttl, and .owl file.
	* bft/ : This is the ontology about kitchen concepts. Script that creates the Affordance Ontology. Ontology is saved as a .nt, .ttl, and .owl file.
* data/ contains:
	* ConceptNet/ :
		* cn_data/ : 
			* filtered_data/ : Csv data files that were preprocessed.
			* requests_output/ : Raw data files extracted from API.
		* parse/ : 
			* Scripts that set up the ontology (organization) of the CN data extracted.
		* scripts that retrieve data from API.

	* RecipePuppy/ :
