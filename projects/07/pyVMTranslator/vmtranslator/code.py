import os

curr_dir = os.path.dirname(os.path.realpath(__file__))
arithmetic_snippets = {}

jmp_cmds = ['eq', 'gt', 'lt']

class CodeWriter():

    def __init__(self, outfile, comment=False):
        self.comment = comment
        self.outfile = outfile

        self.jmpcnt = 0

    def write_arithmetic(self, cmd):
        asm = self.get_arithmetic_snippet(cmd)

        if self.comment:
            print('// {}'.format(cmd), file=self.outfile)

        if cmd in jmp_cmds:
            asm = asm.replace('JMPNUM', 'ARITHM_JMP_{}'.format(self.jmpcnt))
            self.jmpcnt += 1

        self.outfile.write(asm)

    def get_arithmetic_snippet(self, cmd):
        if cmd in arithmetic_snippets.keys():
            return arithmetic_snippets[cmd]
        else:
            filename = os.path.join(curr_dir, 'asm', '{}.asm'.format(cmd))
            with open(filename, 'r') as file:
                snippet = file.read()

            arithmetic_snippets[cmd] = snippet
            return snippet
