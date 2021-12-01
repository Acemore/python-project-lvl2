import json
import yaml


def get_file_content(file_path):
    opened_file = open(file_path)

    if file_path.endswith('.json'):
        return json.load(opened_file)
    if file_path.endswith(('.yml', '.yaml')):
        return yaml.safe_load(opened_file)
