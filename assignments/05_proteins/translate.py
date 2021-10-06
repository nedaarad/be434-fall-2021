#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence to translate')

    parser.add_argument('-c',
                        '--codons',
                        metavar='FILE',
                        help='A file with codon translations',
                        required=True,
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ protein sequence"""
    args = get_args()
    codon_table = {}
    for line in args.codons:
        key, val = line.rstrip().split()
        codon_table[key] = val

    k = 3
    seq = args.sequence.upper()
    protein = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        protein += codon_table.get(codon, '-')

    print(protein, file=args.outfile)

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
