import unittest
import os
from random import randint

import vmtranslator.parser as parser

class parserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser(None)

    def tearDown(self):
        pass

    def test_trim_commnet_line(self):
        self.assertEqual(self.parser.trim('// commnets bla bla'),
                         '', 'Failed to trim comment line');

    def test_trim_commnet_line_with_leading_space(self):
        self.assertEqual(self.parser.trim('   // commnets bla bla'),
                         '', 'Failed to trim comment line with leading spaces');

    def test_trim_inline_commnet_with_tailing_space(self):
        self.assertEqual(self.parser.trim('Some thing  // commnets bla bla'),
                         'Some thing', 'Failed to trim inline comment with tailing spaces');

    def test_trim_inline_commnet_with_leading_space(self):
        self.assertEqual(self.parser.trim('  Some thing// commnets bla bla'),
                         'Some thing', 'Failed to trim inline comment with leading spaces');

    def test_trim_inline_commnet(self):
        self.assertEqual(self.parser.trim('  Some thing  // commnets bla bla'),
                         'Some thing', 'Failed to trim inline comment with both-end spaces');

    def test_parse_commnet_line(self):
        self.parser.parse('  // commnets bla bla')
        self.assertEqual(self.parser.type, parser.COMMAND_TYPE_EMPTY, 'Failed to parse comment line');

    def test_arithmetic_line(self):
        arithm_cmds = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        for cmd in arithm_cmds:
            self.parser.parse(cmd)
            self.assertEqual(self.parser.type, parser.COMMAND_TYPE_ARITHMETIC, 'Failed to parse {} line'.format(cmd));
            self.assertEqual(self.parser.arg1, cmd, 'Failed to parse arg1 of {} line'.format(cmd));

    def test_push_line(self):
        segments = ['static', 'local', 'argument', 'this', 'that', 'const', 'pointer']
        addr_max = [239, 1024, 1024, 1024, 1024, 1024, 1]
        for idx, seg in enumerate(segments):
            rand_addr = randint(0, addr_max[idx])
            cmd = 'push {} {}'.format(seg, rand_addr)
            self.parser.parse(cmd)
            self.assertEqual(self.parser.type, parser.COMMAND_TYPE_PUSH, 'Failed to parse push line, cmd = {}'.format(cmd));
            self.assertEqual(self.parser.arg1, seg, 'Failed to parse arg1 of push line, cmd = {}'.format(cmd));
            self.assertEqual(self.parser.arg2, rand_addr, 'Failed to parse arg2 of push line, cmd = {}'.format(cmd));
