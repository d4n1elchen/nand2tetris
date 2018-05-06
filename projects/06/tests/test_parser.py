import unittest

import HackAssembler.parser as parser

class parserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = parser.parser()

    def test_trim_commnet_line(self):
        self.assertEqual(self.parser.trim("// commnets bla bla"),
                         "", "Failed to trim comment line");

    def test_trim_commnet_line_with_leading_space(self):
        self.assertEqual(self.parser.trim("   // commnets bla bla"),
                         "", "Failed to trim comment line with leading spaces");

    def test_trim_inline_commnet_with_tailing_space(self):
        self.assertEqual(self.parser.trim("Some thing  // commnets bla bla"),
                         "Some thing", "Failed to trim inline comment with tailing spaces");

    def test_trim_inline_commnet_with_leading_space(self):
        self.assertEqual(self.parser.trim("  Some thing// commnets bla bla"),
                         "Some thing", "Failed to trim inline comment with leading spaces");

    def test_trim_inline_commnet(self):
        self.assertEqual(self.parser.trim("  Some thing  // commnets bla bla"),
                         "Some thing", "Failed to trim inline comment with both-end spaces");

    def test_parse_commnet_line(self):
        self.parser.parse("  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_EMPTY,
                         "Failed to parse comment line");

    def test_parse_a_instruction(self):
        self.assertEqual(self.parser.parse_type_A("@123"), ("@", 123),
                         "Failed to parse A instruction");

    def test_parse_c_instruction_without_jump(self):
        self.assertEqual(self.parser.parse_type_C("MD=M+1"), ("MD", "M+1", ""),
                         "Failed to C insturction w/o jump");

    def test_parse_c_instruction_without_dest_with_jump(self):
        self.assertEqual(self.parser.parse_type_C("D;JMP"), ("", "D", "JMP"),
                         "Failed to C instruction w/o comp and w/ jump");

    def test_parse_c_instruction_without_dest_with_jump_0(self):
        self.assertEqual(self.parser.parse_type_C("0;JMP"), ("", "0", "JMP"),
                         "Failed to C instruction w/o comp and w/ jump");

    def test_parse_c_instruction_with_all(self):
        self.assertEqual(self.parser.parse_type_C("D=D+1;JGT"), ("D", "D+1", "JGT"),
                         "Failed to C instruction w/ all field");

    def test_parse_a_line(self):
        self.parser.parse("  @123  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_A,
                         "Failed to recognize A type instruction");
        self.assertEqual(self.parser.value, 123,
                         "Failed to parse value in A type instruction");

    def test_parse_c_line(self):
        self.parser.parse("  D=M+1;JLT  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_C,
                         "Failed to recognize C type instruction");
        self.assertEqual((self.parser.dest, self.parser.comp, self.parser.jump),
                         ("D", "M+1", "JLT"),
                         "Failed to parse fields in C type instruction");

if __name__ == '__main__':
    unittest.main()
