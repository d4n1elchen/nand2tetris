import unittest
import os

import vmtranslator.code as code

curr_dir = os.path.dirname(os.path.realpath(__file__))

class CodeTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = os.path.join(curr_dir, "out_asm")

        if not os.path.isdir(self.tmp_dir):
            os.mkdir(self.tmp_dir)

    def tearDown(self):
        if not os.listdir(self.tmp_dir):
            os.rmdir(self.tmp_dir)

    def test_write_arithmetic(self):
        arithm_cmds = ['add', 'sub', 'neg', 'and', 'or', 'not']
        outfile = os.path.join(self.tmp_dir, 'arithm_test.asm')

        for cmd in arithm_cmds:
            cmpfile = os.path.join(curr_dir, '..', 'vmtranslator', 'asm', '{}.asm'.format(cmd))
            with open(outfile, 'w') as file:
                codewriter = code.CodeWriter(file)
                codewriter.write_arithmetic(cmd)
            self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

            os.remove(outfile)

    def test_write_arithmetic_jmp(self):
        arithm_jmp_cmds = ['eq', 'gt', 'lt']
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')

        for cmd in arithm_jmp_cmds:
            cmpfile = os.path.join(curr_dir, 'arithm_jmp_cmp', '{}.asm'.format(cmd))
            with open(outfile, 'w') as file:
                codewriter = code.CodeWriter(file)
                codewriter.write_arithmetic(cmd)
            self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

            os.remove(outfile)

    def test_write_arithmetic_jmp(self):
        arithm_jmp_cmds = ['eq', 'gt', 'lt']
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'arithm_jmp_cmp', 'seq.asm')

        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            for cmd in arithm_jmp_cmds:
                codewriter.write_arithmetic(cmd)

        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

        os.remove(outfile)

    def assertFileEqual(self, first, second, msg=None):
        """Assert that contents in two files are equal
        """
        self.assertTrue(isinstance(first, str),
                'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                'Second argument is not a string')

        with open(first, 'r') as firstfile:
            with open(second, 'r') as secondfile:
                first_str = firstfile.read()
                second_str = secondfile.read()
                self.assertMultiLineEqual(first_str, second_str, msg)

if __name__ == '__main__':
    unittest.main()
