#!/usr/bin/env python3

import vmtranslator.translator as translator
import argparse

parser = argparse.ArgumentParser(description='Translate Hack assemble language into Hack machine code.')

parser.add_argument('infile', type=str,
                    help='vm file path')
parser.add_argument('-o', '--outfile', default='', type=str,
                    help='output file path (default: [infile_name].asm)')

args = parser.parse_args()

trnsltor = translator.Translator(args.infile, args.outfile)
trnsltor.translate()
trnsltor.close()
