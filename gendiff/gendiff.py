import argparse


def display_help():
    gendiff_args_parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
    gendiff_args_parser.add_argument('-f', '--format', help='set format of output')
    gendiff_args_parser.add_argument('first_file')
    gendiff_args_parser.add_argument('second_file')
    gendiff_args_parser.parse_args()
