# This script takes data from the RecipePuppy API and writes the data to csv files.
import requests
import pandas as pd
from Recipe import Recipe

instances = ['milk', 'apple', 'lemon', 'coffee', 'croissant', 'garnish', 'egg', 'orange_juice', 'apple_juice', 'butter']

def main():

    for instance in instances:
        recipe_node = f'http://api.conceptnet.io/c/en/{instance}?filter=/c/en?offset=0&limit=2500'
        node = Recipe(recipe_node, instance)
        node.output_requests_csv()
        node.filter_requests()


if __name__ == "__main__":
    main()
