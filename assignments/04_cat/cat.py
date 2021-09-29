#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-09-28
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', nargs='+',
                        type=argparse.FileType('rt'), help='Input file')

    parser.add_argument('-n',
                        '--number',
                        help='A line number',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.file:
        line_num = 0
        if args.number:
            for line in file:
                line_num += 1
                print('     ' + f'{line_num}' + '\t' + f'{line}', end='')

        else:
            print(file.read(), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
