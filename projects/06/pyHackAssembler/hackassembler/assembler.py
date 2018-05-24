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

    def assemble(self):
        """Parse and assemble the input asm file and write to output file
        """
        with open(self.infile_name, 'r') as infile:
            self.parser = parser.Parser(infile)
            with open(self.outfile_name, 'w') as outfile:
                self.parser.first_pass()
                while self.parser.parse_next():
                    if self.parser.type == parser.INSTRUCTION_TYPE_A:
                        print(code.get_A_instruction(self.parser.value), file=outfile)
                    elif self.parser.type == parser.INSTRUCTION_TYPE_C:
                        print(code.get_C_instruction(self.parser.comp, self.parser.dest, self.parser.jump), file=outfile)
                    elif self.parser.type == parser.INSTRUCTION_TYPE_EMPTY:
                        pass
                    else:
                        print(line)
                        raise ValueError('Instruction type not recognized')
