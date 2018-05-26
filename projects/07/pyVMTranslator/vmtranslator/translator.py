from . import parser
from . import code

class Translator():
    def __init__(self, infile_name, outfile_name=''):
        self.infile_name = infile_name

        if outfile_name == '':
            outfile_name = splitext(infile)[0] + '.asm'

        if outfile_name.lower().endswith('.asm'):
            self.outfile_name = outfile_name
        else:
            self.outfile_name = outfile_name + '.asm'

        self.infile = open(self.infile_name, 'r')
        self.outfile = open(self.outfile_name, 'w')

        self.parser = parser.Parser(self.infile)

    def translate(self):
        pass

    def close(self):
        self.infile.close()
        self.outfile.close()
