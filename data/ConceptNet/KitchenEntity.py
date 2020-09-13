# Class that retrieves and organizes data from API.
import requests
import pandas as pd
import json
from preprocess import *
from stop_words import get_stop_words

class KitchenEntity:

    def __init__(self, api_node, entity_name):
        self.api_node = api_node
        self.entity_name = entity_name

    def output_requests_csv(self):
        entity = requests.get(self.api_node).json()

        entity_dict = dict()
        entity_dict['subject'] = []
        entity_dict['subject_id'] = []
        entity_dict['relation'] = []
        entity_dict['object'] = []
        entity_dict['object_id'] = []
        entity_dict['surface_text'] = []
        entity_dict['weight'] = []
        entity_edges = entity['edges']
        for data in entity_edges:
            subject = data['start']['label']
            subject_id = data['start']['@id']
            relation = data['rel']['label']
            object = data['end']['label']
            object_id = data['end']['@id']
            weight = data['weight']
            surface_text = data['surfaceText']
            data_tuple = (subject, subject_id, relation, object, object_id, weight, surface_text)
            entity_dict['subject'].append(subject)
            entity_dict['subject_id'].append(subject_id)
            entity_dict['relation'].append(relation)
            entity_dict['object'].append(object)
            entity_dict['object_id'].append(object_id)
            entity_dict['surface_text'].append(surface_text)
            entity_dict['weight'].append(weight)

        data_df = pd.DataFrame(entity_dict)
        data_df.to_csv(f'./cn_data/requests_output/{self.entity_name}.csv', index = False)


        ## print some stats ##
        print(f'....Getting data of {self.entity_name}....')

        print('Relations:', set(entity_dict['relation']), '\n\n')


    def filter_requests(self):
        """
        Preprocesses the concept net data requests and creates a filtered csv file of the data.
        """
        entity_df = pd.read_csv(f'./cn_data/requests_output/{self.entity_name}.csv')

        for index, row in entity_df.iterrows():
            if isEnglish(row['subject']) == False or isEnglish(row['object']) == False:
                entity_df.drop(index, inplace=True)

        entity_df['subject'] = entity_df['subject'].apply(lambda row : standardize_node_name(row, self.entity_name))
        entity_df['object'] = entity_df['object'].apply(lambda row : standardize_node_name(row, self.entity_name))

        filtered_entity_df = remove_irrelevant_relations(entity_df)
        filtered_entity_df.to_csv(f'./cn_data/filtered_data/{self.entity_name}_filtered.csv', index=False)
