"""
A script to load our maps into our mongo database
"""
from mongoengine import *
import os
import json

connect('gambitPLO', host='localhost', port=27017)

root_directory = '../gambitFormatted'
action_directory = 'rfi'
legends_file = 'legends.json'


class Post(Document):
    initial_action = StringField(required=True)
    stack_size = StringField(required=True, max_length=3)
    rake_structure = StringField(required=True)
    players = StringField(required=True, max_length=1)
    position = StringField(required=True, max_length=2)
    simple_suit = StringField(required=True, max_length=2)
    detailed_suit = StringField(required=True, max_length=4)
    showdown_cards = StringField(required=True, max_length=2)
    map = StringField(required=True)
    legend = StringField(required=True)


def files_to_load(path):
    """
    List of all the files that are to be loaded into the database
    :param path:
    :return: List
    """
    files_to_return = []
    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            for file in files:
                files_to_return.append(os.path.join(root, file))

    return files_to_return


json_files = files_to_load(os.path.join(root_directory, action_directory))


def read_legend_to_string():
    path = os.path.join(root_directory, legends_file)
    with open(path, "r") as f:
        leg_string = f.read()

        return leg_string


legend_string = read_legend_to_string()

def split_all(path):
    """
    I took this function from stackoverflow.
    It uses os.path.split and a while loop to return all parts of a path in a list.
    :param path: string
    :return: list
    """
    all_parts_list = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            all_parts_list.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            all_parts_list.insert(0, parts[1])
            break
        else:
            path = parts[0]
            all_parts_list.insert(0, parts[1])

    return all_parts_list

for json_file in json_files:

    parts_list = split_all(json_file)
    initial_action = parts_list[2]
    stack_size = parts_list[3]
    rake_structure = parts_list[4]
    players = parts_list[5]
    position = parts_list[7]
    simple_suit = parts_list[9]
    detailed_suit = parts_list[-1].strip('.json')

    with open(json_file, 'r') as f:
        f = f.read()
        json_data = json.loads(f)
        for sd_combo, sc_map in json_data.items():
            map_to_store = json.dumps(sc_map)
            doc_to_save = Post(
                initial_action=initial_action,
                stack_size=stack_size,
                rake_structure=rake_structure,
                players=players,
                position=position,
                simple_suit=simple_suit,
                detailed_suit=detailed_suit,
                showdown_cards=sd_combo,
                map=map_to_store,
                legend=legend_string
            )

            doc_to_save.save()
