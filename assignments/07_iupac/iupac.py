#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-10-16
Purpose: Expand IUPAC codes
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequences')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    sequences = args.sequences
    IUPAC_code = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'T',
        'U': 'U',
        'R': '[AG]',
        'Y': '[CT]',
        'S': '[GC]',
        'W': '[AT]',
        'K': '[GT]',
        'M': '[AC]',
        'B': '[CGT]',
        'D': '[AGT]',
        'H': '[ACT]',
        'V': '[ACG]',
        'N': '[ACGT]'
    }

    for sequence in sequences:
        print(f'{sequence} ', end='', file=args.outfile)
        for char in sequence:
            code = IUPAC_code.get(char, char)
            print(f'{code}', end='', file=args.outfile)
        print(file=args.outfile)

    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
