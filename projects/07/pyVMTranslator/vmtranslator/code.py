import os

curr_dir = os.path.dirname(os.path.realpath(__file__))
arithmetic_snippets = {}
memory_access_snippets = {}

class CodeWriter():

    def __init__(self, outfile, comment=False):
        self.comment = comment
        self.outfile = outfile

        self.jmpcnt = 0

    def write_arithmetic(self, cmd):
        asm = self.get_arithmetic_snippet(cmd)

        if self.comment:
            print('// {}'.format(cmd), file=self.outfile)

        self.outfile.write(asm)

    def write_pushpop(self, cmd, segment, index):
        asm = self.get_memory_access_snippet(cmd, segment, index)

        if self.comment:
            print('// {} {} {}'.format(cmd, segment, index), file=self.outfile)

        self.outfile.write(asm)

    def get_arithmetic_snippet(self, cmd):
        if cmd in arithmetic_snippets.keys():
            snippet = arithmetic_snippets[cmd]
        else:
            filename = os.path.join(curr_dir, 'asm', '{}.asm'.format(cmd))
            with open(filename, 'r') as file:
                snippet = file.read()

            arithmetic_snippets[cmd] = snippet

        if cmd in ['eq', 'gt', 'lt']:
            snippet = snippet.replace('JMPNUM', 'ARITHM_JMP_{}'.format(self.jmpcnt))
            self.jmpcnt += 1

        return snippet


    def get_memory_access_snippet(self, cmd, segment, index):

        if segment in ['local', 'argument', 'this', 'that']:
            key = cmd + '_relative'
        else:
            key = cmd + '_' + segment

        if key in memory_access_snippets.keys():
            snippet = memory_access_snippets[key]
        else:
            filename = os.path.join(curr_dir, 'asm', '{}.asm'.format(key))
            with open(filename, 'r') as file:
                snippet = file.read()

            memory_access_snippets[key] = snippet

        if segment in ['local', 'argument', 'this', 'that']:
            snippet = snippet.replace('SEGMENT', {
                'local': 'LCL',
                'argument': 'ARG',
                'this': 'THIS',
                'that': 'THAT'
            }[segment])

        snippet = snippet.replace('IDX', str(index))

        if segment == 'pointer':
            snippet = snippet.replace('THISTHAT', ['THIS', 'THAT'][index])

        return snippet
