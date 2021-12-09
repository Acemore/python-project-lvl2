import json
import yaml


def parse_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as json_file:
            return json.load(json_file)
    if file_path.endswith(('.yml', '.yaml')):
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
