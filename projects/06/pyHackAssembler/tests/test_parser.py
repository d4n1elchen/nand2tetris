import unittest

import hackassembler.parser as parser

class parserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

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

    def test_parse_a_instruction_default_symbol(self):
        self.assertEqual(self.parser.parse_type_A("@KBD"), ("@", 0x6000),
                         "Failed to parse A instruction with default symbol");

    def test_parse_a_instruction_symbol(self):
        self.parser.parse_type_A("@somevar")
        self.assertEqual(self.parser.parse_type_A("@sum"), ("@", 17),
                         "Failed to parse A instruction with user symbol");

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

    def test_parse_a_line_symbol(self):
        self.parser.parse("  @R0  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_A, "Failed to recognize A type instruction");
        self.assertEqual(self.parser.value, 0,
                         "Failed to parse value in A type instruction with default symbol");

        self.parser.parse("  @var1  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_A, "Failed to recognize A type instruction");
        self.assertEqual(self.parser.value, 16,
                         "Failed to parse value in A type instruction with user symbol creation");

        self.parser.parse("  @var1  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_A, "Failed to recognize A type instruction");
        self.assertEqual(self.parser.value, 16,
                         "Failed to parse value in A type instruction with user symbol reference");

    def test_parse_c_line(self):
        self.parser.parse("  D=M+1;JLT  // commnets bla bla")
        self.assertEqual(self.parser.type, parser.INSTRUCTION_TYPE_C, "Failed to recognize C type instruction");
        self.assertEqual((self.parser.dest, self.parser.comp, self.parser.jump),
                         ("D", "M+1", "JLT"),
                         "Failed to parse fields in C type instruction");

    def test_first_pass_label_line(self):
        self.parser.pc = 10
        self.parser.first_pass("(LABEL)")
        self.assertEqual(self.parser.symbol["LABEL"], 10,
                         "Failed to parse label");

    def test_first_pass_comment_line(self):
        self.parser.pc = 10
        self.parser.first_pass("// comments bla bla")
        self.assertEqual(self.parser.pc, 10,
                         "Failed to parse comment line during first pass");

    def test_first_pass_A_instruction_line(self):
        self.parser.pc = 10
        self.parser.first_pass("  @123  // comments bla bla")
        self.assertEqual(self.parser.pc, 11,
                         "Failed to parse A instruction during first pass");

    def test_first_pass_C_instruction_line(self):
        self.parser.pc = 10
        self.parser.first_pass("  D=M+1;JLT  // comments bla bla")
        self.assertEqual(self.parser.pc, 11,
                         "Failed to parse C instruction during first pass");

if __name__ == '__main__':
    unittest.main()
