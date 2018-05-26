#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Translate Hack assemble language into Hack machine code.')

parser.add_argument('infile', type=str,
                    help='asm file path')
parser.add_argument('-o', '--outfile', default='out.hack', type=str,
                    help='output file path (default: out.hack)')

args = parser.parse_args()

print(args.infile)
