#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-09-19
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('key', metavar='str', nargs='+', help='my keys')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    key = args.key
    answers = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'
    }
    for x in key:
        if x in answers:
            # print("%s, %s" % (x, answers[x]))
            # print(f'{x}, {answers[x]}')
            print('{}, {}'.format(x, answers[x]))
        else:
            print("I don't know \"%s\"" % (x))
            # instead of x it is better to write key in keys


# --------------------------------------------------
if __name__ == '__main__':
    main()
