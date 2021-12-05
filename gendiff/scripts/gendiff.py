#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
from gendiff.gendiff import STYLISH


DESCRIPTION = 'Generate diff'
FIRST_FILE = 'first_file'
GENDIFF = 'gendiff'
HELP = 'set format of output'
SECOND_FILE = 'second_file'


def main():
    gendiff_args_parser = argparse.ArgumentParser(
        prog=GENDIFF,
        description=DESCRIPTION
    )
    gendiff_args_parser.add_argument(FIRST_FILE)
    gendiff_args_parser.add_argument(SECOND_FILE)
    gendiff_args_parser.add_argument(
        '-f', '--format',
        default=STYLISH,
        help=HELP
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
