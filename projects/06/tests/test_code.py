import unittest

import hackassembler.code as code

class CodeTestCase(unittest.TestCase):
    def test_A_code_construct(self):
        self.assertEqual(code.get_A_instruction(123),
                         "0000000001111011", "Failed to construct A code");

    def test_C_code_construct_without_jump(self):
        self.assertEqual(code.get_C_instruction("M+1", "MD", ""),
                         "1111110111011000", "Failed to construct C code without jump field");

    def test_C_code_construct_without_comp(self):
        self.assertEqual(code.get_C_instruction("0", "", "JMP"),
                         "1110101010000111", "Failed to construct C code without comp field");

    def test_C_code_construct_with_all(self):
        self.assertEqual(code.get_C_instruction("M+1", "D", "JMP"),
                         "1111110111010111", "Failed to construct C code with all fields");

if __name__ == '__main__':
    unittest.main()
