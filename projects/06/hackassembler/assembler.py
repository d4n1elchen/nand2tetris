from os.path import splitext

from . import parser
from . import code

class HackAssembler:
    def __init__(self, infile, outfile=''):
        self.parser = parser.Parser()

        self.infile = infile

        if outfile == '':
            outfile = splitext(infile)[0] + ".hack"

        if outfile.lower().endswith(".hack"):
            self.outfile = outfile
        else:
            self.outfile = outfile + ".hack"

    def assemble(self):
        """Parse and assemble the input asm file and write to output file
        """
        self.first_pass()
        with open(self.infile, 'r') as infile:
            with open(self.outfile, 'w') as outfile:
                line = infile.readline()
                while line != '':
                    self.parser.parse(line)
                    if self.parser.type == parser.INSTRUCTION_TYPE_A:
                        print(code.get_A_instruction(self.parser.value), file=outfile)
                    elif self.parser.type == parser.INSTRUCTION_TYPE_C:
                        print(code.get_C_instruction(self.parser.comp, self.parser.dest, self.parser.jump), file=outfile)
                    elif self.parser.type == parser.INSTRUCTION_TYPE_EMPTY:
                        pass
                    else:
                        print(line)
                        raise ValueError("Instruction type not recognized")
                    line = infile.readline()

    def first_pass(self):
        """First pass for parsing labels
        """
        with open(self.infile, 'r') as infile:
            line = infile.readline()
            while line != '':
                self.parser.first_pass(line)
                line = infile.readline()
