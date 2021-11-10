#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-11-10
Purpose: Conserved bases in aligned sequences
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Conserved bases in aligned sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='File',
                        help='Input file',
                        type=argparse.FileType('rt'))

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Conserved bases in aligned sequences"""

    args = get_args()
    file = args.file
    seqs = []
    for seq in file:
        seqs.append(seq.rstrip())
        print(seq, end='')

    for i in range(len(seqs[0])):
        bases = []
        for seq in seqs:
            bases += seq[i]
        print('|' if len(set(bases)) == 1 else 'X', end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
