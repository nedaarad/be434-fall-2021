#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-11-17
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str', metavar='str', help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()
    return args


# --------------------------------------------------
def rle(seq):
    """define the rle function"""
    zipped = []
    count = 1
    var = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == var:
            count = count + 1
        else:
            zipped.append([var, count])
            var = seq[i]
            count = 1
    zipped.append([var, count])
    return zipped


# --------------------------------------------------
def main():
    """Run-length encoding/data compression"""

    args = get_args()
    seq = args.str
    list = rle(seq)
    zipped_seq = ''
    for i in range(0, len(list)):
        for x in list[i]:
            zipped_seq += str(x)
    string = zipped_seq.replace('1', '')
    print(string, end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
