from os.path import splitext

from . import parser
from . import code

class Translator():
    def __init__(self, infile_name, outfile_name=''):
        self.infile_name = infile_name

        if outfile_name == '':
            outfile_name = splitext(infile_name)[0] + '.asm'

        if outfile_name.lower().endswith('.asm'):
            self.outfile_name = outfile_name
        else:
            self.outfile_name = outfile_name + '.asm'

        self.infile = open(self.infile_name, 'r')
        self.outfile = open(self.outfile_name, 'w')

        self.parser = parser.Parser(self.infile)
        self.writer = code.CodeWriter(self.outfile, comment=True)

    def translate(self):
        """Translate input file
        """
        while self.parser.parse_next():
            if self.parser.type == parser.COMMAND_TYPE_EMPTY:
                pass
            elif self.parser.type == parser.COMMAND_TYPE_ARITHMETIC:
                self.writer.write_arithmetic(self.parser.arg1)
            elif self.parser.type == parser.COMMAND_TYPE_PUSH:
                self.writer.write_pushpop('push', self.parser.arg1, self.parser.arg2)
            elif self.parser.type == parser.COMMAND_TYPE_POP:
                self.writer.write_pushpop('pop', self.parser.arg1, self.parser.arg2)
            else:
                print(self.parser.line)
                raise Error('Cannot parse command.')

    def close(self):
        """Close all file
        """
        self.infile.close()
        self.outfile.close()
