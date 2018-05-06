# Parser for parse a single line of Hack Assembly
import re

INSTRUCTION_TYPE_UNKNOWN = -1
INSTRUCTION_TYPE_EMPTY = 0
INSTRUCTION_TYPE_A = 1
INSTRUCTION_TYPE_C = 2

class Parser:
    def __init__(self):
        self.type = INSTRUCTION_TYPE_UNKNOWN

        # instruction parts
        self.value = ''
        self.comp = ''
        self.dest = ''
        self.jump = ''

        # current line content
        self.line = ''

    def parse(self, line):
        """Parse a single line
        """
        self.line = line
        l = self.trim(line)

        if l == "":
            self.type = INSTRUCTION_TYPE_EMPTY
        elif l[0] == "@":
            self.type = INSTRUCTION_TYPE_A
            _, self.value = self.parse_type_A(l)
        else:
            self.type = INSTRUCTION_TYPE_C
            self.dest, self.comp, self.jump = self.parse_type_C(l)

    def trim(self, line):
        """Trim comments and leading and tailing spaces
        """
        return re.sub('//.*?$','',line).strip()

    def parse_type_A(self, line):
        """Parse type A instruction
        """
        return line[0], int(line[1:])

    def parse_type_C(self, line):
        """Parse type C instruction
        """
        dest = ''
        comp = ''
        jump = ''

        spl = line.split(';')
        if len(spl) > 1:
            line = spl[0]
            jump = spl[1]

        spl = line.split('=')
        if len(spl) > 1:
            dest = spl[0]
            comp = spl[1]
        else:
            comp = spl[0]

        return dest, comp, jump
