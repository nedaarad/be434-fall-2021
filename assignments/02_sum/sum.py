#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        metavar='int',
                        type = int,
                        nargs = '+',
                        help='Sum Integers')




    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    integers_list = args.integers


    print('{} = {}'.format(' + '.join(map(str, integers_list)), sum(integers_list)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
