#!/usr/bin/env python3

import argparse
from gendiff import generate_diff


def main():
    gendiff_args_parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff'
    )
    gendiff_args_parser.add_argument('first_file')
    gendiff_args_parser.add_argument('second_file')
    gendiff_args_parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    gendiff_args = gendiff_args_parser.parse_args()

    print(
        generate_diff(
            gendiff_args.first_file,
            gendiff_args.second_file,
            gendiff_args.format
        )
    )


if __name__ == '__main__':
    main()
