#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-10-22
Purpose: Find k-mers and frequencies
"""

import argparse

# --------------------------------------------------


def get_args():
    """k-mers"""

    parser = argparse.ArgumentParser(
        description='Find k-mers in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Readable file1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Readable file2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='An integer value greater than 0',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmer < 1:
        parser.error('--kmer "{}" must be > 0'.format(args.kmer))

    return args

# --------------------------------------------------


def find_kmers(seq, k):
    """n"""

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]

# --------------------------------------------------


def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []

# --------------------------------------------------


def main():
    """Find k-mers in string"""

    args = get_args()
    counts1 = count_kmers(args.file1, args.kmer)
    counts2 = count_kmers(args.file2, args.kmer)
    for kmer in counts1:
        if kmer in counts2:
            print('{0:10}{1:6}{2:6}'.format(
                kmer, counts1.get(kmer), counts2.get(kmer)))

# --------------------------------------------------


def count_kmers(fh, k):
    """Function"""

    counts = {}
    for line in fh:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer not in counts:
                    counts[kmer] = 0
                counts[kmer] += 1

    return counts


# --------------------------------------------------
if __name__ == '__main__':
    main()
