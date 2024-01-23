import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        input = "\"this is a string:\'\"abc\'\"\""
        expect = "this is a string:\'\"abc\'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))

    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    