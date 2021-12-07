#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-12-06
Purpose: To print the given lines in reverse
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='To print the given lines in reverse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Reversed lines',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Create reversed lines"""

    args = get_args()
    for fh in args.file:
        lines = fh.readlines()
        for line in reversed(lines):
            print(line, file=args.outfile, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
