# Parser for parse a single line of Hack Assembly
import re

INSTRUCTION_TYPE_UNKNOWN = -1
INSTRUCTION_TYPE_EMPTY = 0
INSTRUCTION_TYPE_A = 1
INSTRUCTION_TYPE_C = 2

DEFAULT_SYMBOLS = {
    'SP': 0x0000,
    'LCL': 0x0001,
    'ARG': 0x0002,
    'THIS': 0x0003,
    'THAT': 0x0004,
    'R0': 0x0000,
    'R1': 0x0001,
    'R2': 0x0002,
    'R3': 0x0003,
    'R4': 0x0004,
    'R5': 0x0005,
    'R6': 0x0006,
    'R7': 0x0007,
    'R8': 0x0008,
    'R9': 0x0009,
    'R10': 0x000a,
    'R11': 0x000b,
    'R12': 0x000c,
    'R13': 0x000d,
    'R14': 0x000e,
    'R15': 0x000f,
    'SCREEN': 0x4000,
    'KBD': 0x6000
}

class Parser:
    def __init__(self, in_stream):
        self.type = INSTRUCTION_TYPE_UNKNOWN

        # instruction parts
        self.value = ''
        self.comp = ''
        self.dest = ''
        self.jump = ''

        # current line content
        self.line = ''

        # init symbol table
        self.symbol = DEFAULT_SYMBOLS

        # init programe counter
        self.pc = 0

        # init variable allocator
        self.n = 16

        # file in stream
        self.in_stream = in_stream

    def next(self):
        """Read next line
        """
        self.line = self.in_stream.readline()
        return self.line

    def parse_next(self):
        """Read next line and parse
        """
        if self.next():
            self.parse(self.line)
            return True
        else:
            return False

    def parse(self, line):
        """Parse a single line
        """
        l = self.trim(line)

        if l == "" or l[0] == "(":
            self.type = INSTRUCTION_TYPE_EMPTY
        elif l[0] == "@":
            self.type = INSTRUCTION_TYPE_A
            _, self.value = self.parse_type_A(l)
        else:
            self.type = INSTRUCTION_TYPE_C
            self.dest, self.comp, self.jump = self.parse_type_C(l)

    def first_pass(self):
        """Parse a single line for first pass
        """
        while self.next():
            self.first_pass_line(self.line)

        # Go back to begining
        self.in_stream.seek(0)

    def first_pass_line(self, line):
        l = self.trim(line)

        if l == '':
            pass
        elif l[0] == '(':
            s = re.search('\((.*?)\)', l).group(1)
            self.symbol[s] = self.pc
        else:
            self.pc += 1

    def trim(self, line):
        """Trim comments and leading and tailing spaces
        """
        return re.sub('//.*?$','',line).strip()

    def parse_type_A(self, line):
        """Parse type A instruction
        """
        at = line[0]
        val = line[1:]
        if val.isdigit():
            return at, int(val)
        elif val in self.symbol:
            return at, self.symbol[val]
        else:
            self.symbol[val] = self.n
            self.n += 1
            return at, self.symbol[val]

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
