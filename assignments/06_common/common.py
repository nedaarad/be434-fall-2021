#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        metavar='FILE',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Shared words',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    FILE1 = args.FILE1
    FILE2 = args.FILE2
    words = {}
    shared = []
    words[FILE1.name] = FILE1.read().split()
    words[FILE2.name] = FILE2.read().split()
    for word in words[FILE1.name]:
        if word in words[FILE2.name]:
            if word not in shared:
                shared.append(word)

    for word in shared:
        print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
