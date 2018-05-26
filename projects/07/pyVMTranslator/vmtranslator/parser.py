import re

COMMAND_TYPE_UNKNOWN = -1
COMMAND_TYPE_EMPTY = 0
COMMAND_TYPE_ARITHMETIC = 1
COMMAND_TYPE_PUSH = 2
COMMAND_TYPE_POP = 3

arithmetic_cmds = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']

class Parser():
    def __init__(self, infile):

        # initial variables
        self.type = COMMAND_TYPE_UNKNOWN
        self.arg1 = ''
        self.arg2 = 0

        self.line = ''

        self.infile = infile

    def next(self):
        """Read next line
        """
        self.line = self.infile.readline()
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
        """Parse single line
        """
        l = self.trim(line)

        if l == '':
            self.type = COMMAND_TYPE_EMPTY
        elif l in arithmetic_cmds:
            self.type = COMMAND_TYPE_ARITHMETIC
            self.arg1 = l
        else:
            spl = l.split(' ')
            cmd = spl[0]
            if cmd == 'push':
                self.type = COMMAND_TYPE_PUSH
                self.arg1 = spl[1]
                self.arg2 = int(spl[2])
            elif cmd == 'pop':
                self.type = COMMAND_TYPE_POP
                self.arg1 = spl[1]
                self.arg2 = int(spl[2])

    def trim(self, line):
        """Trim comments and leading and tailing spaces
        """
        return re.sub('//.*?$','',line).strip()
