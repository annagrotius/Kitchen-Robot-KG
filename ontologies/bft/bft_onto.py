from owlready2 import *
from rdflib import Graph, Namespace, URIRef
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'


def onto_to_graph(ontology, ontology_namespace, ontology_prefix, filename):
    """
    Takes an ontology and saves it as an owl file and  ttl file.
    """
    ontology.save(file = f'{filename}.owl', format = "rdfxml")
    g = Graph()
    g.bind(ontology_prefix, ontology_namespace)
    g.parse(f'{filename}.owl')
    g.serialize(f'{filename}.ttl', format='turtle')
    g.serialize(f'{filename}.nt', format='ntriples')


def main():

    # initialize ontology
    bft_uri = "http://test.org/bft.owl#"
    bft = get_ontology(bft_uri)
    bft_namespace = Namespace(bft_uri)

    # classes
    with bft:

        # primary class concepts
        class Furniture(Thing): pass
        class Kitchenware(Thing) : pass
        class Drink(Thing): pass
        class Food(Thing): pass
        class Storage(Thing): pass

        # subclasses
        class Tableware(Kitchenware): pass

        class Glassware(Tableware): pass
        class Plate(Tableware): pass
        class Cutlery(Tableware): pass

        class Fork(Cutlery): pass
        class Knife(Cutlery): pass
        class Spoon(Cutlery): pass

        class Juice(Drink): pass
        class Coffee(Drink): pass
        class Milk(Drink): pass
        class Tea(Drink): pass

        class Bread(Food): pass
        class Egg(Food): pass
        class Condiment(Food): pass
        class Spread(Condiment): pass


        class Table(Furniture): pass
        class Chair(Furniture): pass

        # defining disjointness among all classes
        AllDisjoint([Food, Drink, Storage, Kitchenware, Furniture])
        AllDisjoint([bft.Glassware, bft.Plate, bft.Fork, bft.Knife, bft.Spoon])
        AllDisjoint((bft.search(subclass_of=bft.Drink))[1:])
        AllDisjoint([bft.Bread, bft.Egg, bft.Condiment])  # all food subclasses are disjoint. should this be? since some foods can be together?
        AllDisjoint((bft.search(subclass_of=bft.Furniture))[1:])


    # Object properties
    with bft:

        class is_edible(DataProperty):
            range = [bool]
        class served_with(ObjectProperty, SymmetricProperty):
            domain = [Condiment]
            range = [Food]
        class can_cut(ObjectProperty, Cutlery >> Food):
            pass
        class spread_on(ObjectProperty, Spread >> Food):
            pass

        class can_spread(ObjectProperty, Cutlery >> Food):
            pass
        class used_with(ObjectProperty, SymmetricProperty):
            domain = [Cutlery, Plate]
            range = [Food]
        class primary_usage(DataProperty):
            range = [str]
        class storage_location():
            range = [Storage]


    # defining instances (individuals)
    croissant = Bread("croissant")
    garnish = Food("garnish")
    hardboiled_egg = Egg("hardboiled")
    scrambled_eggs = Egg("scrambled")
    fried_egg = Egg("fried")
    Egg.is_a.append(OneOf([hardboiled_egg, scrambled_eggs, fried_egg]))
    AllDifferent([hardboiled_egg, scrambled_eggs, fried_egg])

    oj = Juice("orange_juice")
    apple_juice = Juice("apple_juice")

    butter = Spread("butter")

    salt_shaker = Tableware("salt_shaker")
    pepper_shaker = Tableware("pepper_shaker")
    bread_basket = Tableware("bread_basket")
    egg_cup = Tableware("egg_cup")

    milk_pitcher = Kitchenware("milk_pitcher", can_contain=[Milk])

    butter_knife = Knife("butter_knife", can_spread=[butter]) # a type of knife

    glass = Glassware("glass")
    teacup = Glassware("teacup", can_contain=[Tea])

    sauce_dish = Plate("sauce_dish")
    butter_dish = Plate("butter_dish")
    bread_plate = Plate("bread_plate")
    teacup_plate = Plate("teacup_plate")
    AllDifferent([sauce_dish, bread_plate, butter_dish, teacup_plate])

    dining_table = Table("table")
    dining_chair = Chair("dining_chair")

    cupboard = Storage("cupboard")


    # classes with restrictions
    Food.is_edible = [True]
    Kitchenware.is_edible = [False]
    Furniture.is_edible = [False]
    Storage.is_edible = [False]

    # save ontology not closing the world
    onto_to_graph(bft, bft_namespace, 'bft', 'bft_onto_not_closed')

    # closing world and save this version
    classes = [Furniture,Kitchenware, Drink, Food, Storage]
    for c in classes:
        close_world(c)
    onto_to_graph(bft, bft_namespace, 'bft', 'bft_onto_closed')


if __name__ == "__main__":
    main()
