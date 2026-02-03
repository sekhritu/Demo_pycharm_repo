import json
import os


def get_parent_folder_path():
    current_path = os.getcwd()
    get_parent = os.path.dirname(current_path)
    return get_parent

def get_data_from_input_file(key):
    file_path = os.path.join(get_parent_folder_path(), "data", "input.json")
    with open(file_path , 'r') as file:
        data = json.load(file)
    return data[key]