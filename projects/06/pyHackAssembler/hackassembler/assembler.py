from os.path import splitext

from . import parser
from . import code

class HackAssembler:
    def __init__(self, infile_name, outfile_name=''):
        self.infile_name = infile_name

        if outfile_name == '':
            outfile_name = splitext(infile)[0] + '.hack'

        if outfile_name.lower().endswith('.hack'):
            self.outfile_name = outfile_name
        else:
            self.outfile_name = outfile_name + '.hack'

        self.infile = open(self.infile_name, 'r')
        self.outfile = open(self.outfile_name, 'w')

        # initialize infile
        self.parser = parser.Parser(self.infile)

    def assemble(self):
        """Parse and assemble the input asm file and write to output file
        """
        self.parser.first_pass()
        while self.parser.parse_next():
            if self.parser.type == parser.INSTRUCTION_TYPE_A:
                print(code.get_A_instruction(self.parser.value), file=self.outfile)
            elif self.parser.type == parser.INSTRUCTION_TYPE_C:
                print(code.get_C_instruction(self.parser.comp, self.parser.dest, self.parser.jump), file=self.outfile)
            elif self.parser.type == parser.INSTRUCTION_TYPE_EMPTY:
                pass
            else:
                print(line)
                raise ValueError('Instruction type not recognized')

    def close(self):
        self.infile.close()
        self.outfile.close()
