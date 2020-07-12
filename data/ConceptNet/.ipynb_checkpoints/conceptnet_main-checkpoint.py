# This script takes data from the ConceptNet API and writes the data to csv files.
import requests
import pandas as pd
import json
from KitchenEntity import KitchenEntity

instances = ['croissant', 'garnish', 'hardboiled_egg', 'scrambled_egg', 'fried_egg', 'orange_juice', 'apple_juice', 'butter', 'salt_shaker', 'pepper_shaker', 'bread_basket', 'egg_cup', 'milk_pitcher', 'fork', 'knife', 'spoon', 'butter_knife', 'glass', 'teacup', 'sauce_dish', 'butter_dish', 'bread_plate', 'teacup_plate', 'dining_table', 'dining_chair', 'cupboard']

def main():

    for instance in instances:
        cn_node = f'http://api.conceptnet.io/c/en/{instance}?filter=/c/en?offset=0&limit=2500'
        node = KitchenEntity(cn_node, instance)
        node.output_requests_csv()
        node.filter_requests()


if __name__ == "__main__":
    main()
