#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-11-01
Purpose: FASTA Interleaved Paired Read Splitter
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='FASTA Interleaved Paired Read Splitter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='An output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """FASTA Interleaved Paired Read Splitter"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fh in args.files:
        root, ext = os.path.splitext(os.path.basename(fh.name))
        forward = open(os.path.join(args.outdir, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(args.outdir, root + '_2' + ext), 'wt')
        parser = SeqIO.parse(fh, 'fasta')

        # for i, rec in enumerate(parser):
        #     out_fh = forward if i % 2 == 0 else reverse
        #     print(f'>{rec.id}', file=out_fh)
        #     print(rec.seq, file=out_fh)

        for i, rec in enumerate(parser):
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')

    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
