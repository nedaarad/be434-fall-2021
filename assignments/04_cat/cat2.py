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

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='A readable file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A line number',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print('{:>6}\t{}' .format(line_num, line.rstrip()))
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
