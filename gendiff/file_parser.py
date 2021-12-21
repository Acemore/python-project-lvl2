import json
import yaml


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()


def parse_json_file(file_raw_content):
    return json.loads(file_raw_content)


def parse_yaml_file(file_raw_content):
    return yaml.safe_load(file_raw_content)


def parse_file(file_raw_content, file_path):
    if file_path.endswith('.json'):
        return parse_json_file(file_raw_content)
    if file_path.endswith(('.yml', '.yaml')):
        return parse_yaml_file(file_raw_content)
