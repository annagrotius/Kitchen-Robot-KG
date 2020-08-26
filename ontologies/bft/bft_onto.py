"""
This script creates the breakfast table ontology and saves a close world and non closed world
version of the ontology as a owl file format and different graph file formats (.ttl, .nt).
"""
from owlready2 import *
from rdflib import Graph, Namespace, URIRef
owlready2.JAVA_EXE ='C:\\Program Files\\Java\\jre1.8.0_191\\bin\\java.exe'


def onto_to_graph(ontology, ontology_namespace, ontology_prefix, filename):
    """
    Args:
        - ontology: ontology to be parsed
        - ontology_namespace: namespace of the ontology
        - ontology_prefix: prefix of the ontology
        - filename: filename under which to name the ontology
    Output: An ontology saves as an ntriple file and  ttl file.
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
        class Tea(Drink): pass
        class Milk(Drink): pass


        class Bread(Food): pass
        class Egg(Food): pass
        class Condiment(Food): pass
        class Spread(Condiment): pass
        class Fruit(Food): pass


        class Table(Furniture): pass
        class Chair(Furniture): pass

        # defining disjointness among all classes
        AllDisjoint([Food, Drink, Storage, Kitchenware, Furniture])
        AllDisjoint([bft.Glassware, bft.Plate, bft.Fork, bft.Knife, bft.Spoon])
        AllDisjoint((bft.search(subclass_of=bft.Drink))[1:])
        AllDisjoint([bft.Bread, bft.Egg, bft.Condiment])
        AllDisjoint((bft.search(subclass_of=bft.Furniture))[1:])


    # Object properties
    with bft:

        class is_edible(DataProperty):
            range = [bool]
        class served_with(ObjectProperty, SymmetricProperty):
            pass
            # domain = [Condiment]
            # range = [Food]
        class can_cut(ObjectProperty, Cutlery >> Food):
            pass
        class spread_on(ObjectProperty, Spread >> Food):
            pass
        class can_spread(ObjectProperty, Cutlery >> Spread):
            pass
        class used_with(ObjectProperty, SymmetricProperty):
            pass
            # domain = [Tableware]
            # range = [Food]
        class storage_location(ObjectProperty):
            range = [Storage]


    # defining instances (individuals)
    croissant = Bread("croissant")
    garnish = Food("garnish")
    hardboiled_egg = Egg("hardboiled_egg")
    scrambled_egg = Egg("scrambled_egg")
    fried_egg = Egg("fried_egg")
    Egg.is_a.append(OneOf([hardboiled_egg, scrambled_egg, fried_egg]))
    AllDifferent([hardboiled_egg, scrambled_egg, fried_egg])

    refrigerator = Kitchenware("refrigerator")

    oj = Juice("orange_juice", storage_location=[refrigerator])
    apple_juice = Juice("apple_juice", storage_location=[refrigerator])

    green_tea = Tea("green_tea")

    milk = Milk("milk", storage_location=[refrigerator])

    black_coffee = Coffee("black_coffee", served_with=[milk])

    butter = Spread("butter", spread_on=[croissant], storage_location=[refrigerator])

    apple = Fruit("apple")
    watermelon = Fruit("watermelon")
    lemon = Fruit("lemon")

    salt_shaker = Tableware("salt_shaker")
    pepper_shaker = Tableware("pepper_shaker", used_with=[salt_shaker])
    bread_basket = Tableware("bread_basket")
    egg_cup = Tableware("egg_cup", used_with=[hardboiled_egg])

    milk_pitcher = Kitchenware("milk_pitcher", used_with=[milk])

    butter_knife = Knife("butter_knife", can_spread=[butter]) # a type of knife
    fork = Fork("fork")
    knife = Knife("knife", can_spread=[butter], used_with=[fork])
    spoon = Spoon("spoon")

    cupboard = Storage("cupboard")

    glass = Glassware("glass", storage_location=[cupboard])
    teacup = Glassware("teacup", storage_location=[cupboard])

    sauce_dish = Plate("sauce_dish", storage_location=[cupboard])
    butter_dish = Plate("butter_dish", storage_location=[cupboard])
    bread_plate = Plate("bread_plate", storage_location=[cupboard])
    teacup_plate = Plate("teacup_plate", storage_location=[cupboard])
    AllDifferent([sauce_dish, bread_plate, butter_dish, teacup_plate])

    dining_table = Table("table")
    dining_chair = Chair("dining_chair")

    # classes with restrictions
    Food.is_edible = [True]
    Drink.is_edible = [True]
    Kitchenware.is_edible = [False]
    Furniture.is_edible = [False]
    Storage.is_edible = [False]

    # save ontology not closing the world
    onto_to_graph(bft, bft_namespace, 'bft', 'bft_onto_not_closed')



if __name__ == "__main__":
    main()
