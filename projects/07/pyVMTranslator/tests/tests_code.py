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

    def test_write_pushpop_push_constant(self):
        cmd = 'push'
        seg = 'constant'
        idx = 66
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_local(self):
        cmd = 'push'
        seg = 'local'
        idx = 10
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_argument(self):
        cmd = 'push'
        seg = 'argument'
        idx = 7
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_this(self):
        cmd = 'push'
        seg = 'this'
        idx = 13
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_that(self):
        cmd = 'push'
        seg = 'that'
        idx = 0
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_temp(self):
        cmd = 'push'
        seg = 'temp'
        idx = 2
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_static(self):
        cmd = 'push'
        seg = 'static'
        idx = 4
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_push_pointer(self):
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmd = 'push'
        seg = 'pointer'

        # THIS
        idx = 0
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

        # THAT
        idx = 1
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

        os.remove(outfile)

    def test_write_pushpop_pop_local(self):
        cmd = 'pop'
        seg = 'local'
        idx = 8
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_argument(self):
        cmd = 'pop'
        seg = 'argument'
        idx = 0
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_this(self):
        cmd = 'pop'
        seg = 'this'
        idx = 3
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_that(self):
        cmd = 'pop'
        seg = 'that'
        idx = 22
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_temp(self):
        cmd = 'pop'
        seg = 'temp'
        idx = 1
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_static(self):
        cmd = 'pop'
        seg = 'static'
        idx = 5
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))
        os.remove(outfile)

    def test_write_pushpop_pop_pointer(self):
        outfile = os.path.join(self.tmp_dir, 'arithm_jmp_test.asm')
        cmd = 'pop'
        seg = 'pointer'

        # THIS
        idx = 0
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
        self.assertFileEqual(outfile, cmpfile, 'Write {} command failed'.format(cmd))

        # THAT
        idx = 1
        cmpfile = os.path.join(curr_dir, 'pushpop_cmp', '{}_{}_{}.asm'.format(cmd, seg, idx))
        with open(outfile, 'w') as file:
            codewriter = code.CodeWriter(file)
            codewriter.write_pushpop(cmd, seg, idx)
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
