#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-11-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_files = len(args.files)

    for fh in args.files:
        for line in fh:
            if re.search(args.pattern, line,
                         re.IGNORECASE if args.insensitive else 0):
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if num_files > 1 else '', line))


# --------------------------------------------------
if __name__ == '__main__':
    main()
