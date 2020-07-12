import pandas as pd
from stop_words import get_stop_words

stopwords = get_stop_words('english')


def get_size(dataframe):
    """
    Takes a dataframe and returns the size of the dataset.
    """
    size = dataframe.shape[0]

    return size


def standardize_node_name(node_name, desired_name):
    """
    Input is a string that represents the node.
    Output is a uniform version of the node.
    eg. changes instances of 'an egg' into 'egg'
    """
    node_name = node_name.lower()
    if desired_name in node_name:
        node_name_list = node_name.split()
        clean_node_name = ''
        for node in node_name_list:
            if node not in stopwords:
                clean_node_name += ' ' + node
        return clean_node_name
    else:
        return node_name


def remove_irrelevant_relations(dataframe):
    """
    Input is a dataframe that drops all rows with certain relations from concept net.
    """
    irrelevant_relations = ['RelatedTo', 'Causes', 'HasSubevent', 'HasFirstSubevent', 'HasLastSubevent', 'MotivatedByGoal', 'ObstructedBy', 'Desires', 'CreatedBy', 'Synonym', 'Antonym', 'DistinctFrom', 'DerivedFrom', 'SymbolOf', 'MannerOf', 'HasContext', 'EtymologicallyRelatedTo', 'EtymologicallyDerivedFrom', 'CausesDesire', 'FormOf', 'Entails', 'NotHasProperty']

    for rel in irrelevant_relations:
        dataframe.drop(dataframe.loc[dataframe['relation']==rel].index, inplace=True)
        dataframe.drop(dataframe.loc[dataframe['weight']<1].index, inplace=True)

    return dataframe


def isEnglish(word):
    """
    Function to remove words that are not English.
    """
    try:
        word.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
