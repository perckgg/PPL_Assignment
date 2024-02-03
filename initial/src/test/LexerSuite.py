import unittest
from TestUtils import TestLexer
## MSSV : 2110242
class LexerSuite(unittest.TestCase):
    def test_100(self):
        """test 100"""
        input = "\"\""
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))
    def test_101(self):
        """test 101"""
        input = "\"Hello \'world\'\""
        expect = "Hello 'world',<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
    def test_102(self):
        """test 102"""
        input = "\"This is a  \'\"string\'\"\""
        expect = "This is a  \'\"string\'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
    def test_103(self):
        """test 103"""
        input = "\"This is"
        expect = "Unclosed String: This is"
        self.assertTrue(TestLexer.test(input,expect,103))
    def test_104(self):
        """test 104"""
        input = "\"Get Ready To Code"
        expect = "Unclosed String: Get Ready To Code"
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_105(self):
        """test 105"""
        input = "\"Get Ready\'\"To Code\'\" this is a string\'\"\""
        expect = "Get Ready\'\"To Code\'\" this is a string\'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
    def test_106(self):
        """test 106"""
        input = "\"Get Ready\'\"To Code\""
        expect = "Get Ready\'\"To Code,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
    def test_107(self):
        """test 107"""
        input = "\"\'\"Get ReadyTo \\n Code\""
        expect = "\'\"Get ReadyTo \\n Code,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
    def test_108(self):
        """test 108"""
        input = "\"Get ReadyTo \\n \\t \\b Code 10.00e-10\""
        expect = "Get ReadyTo \\n \\t \\b Code 10.00e-10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
    def test_109(self):
        """test 109"""
        input = "\"Get ReadyTo Code"
        expect = "Unclosed String: Get ReadyTo Code"
        self.assertTrue(TestLexer.test(input,expect,109))
    def test_110(self):
        """test 110"""
        input = "Get ReadyTo Code\""
        expect = "Get,ReadyTo,Code,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,110))
    def test_111(self):
        """test 111"""
        input = "\"Get ReadyTo \\x Code\""
        expect = "Illegal Escape In String: Get ReadyTo \\x"
        self.assertTrue(TestLexer.test(input,expect,111))
    #############################################################
    def test_112(self):
        """test 112"""
        input = "\"Get ReadyTo \\\\ Code\""
        expect = "Get ReadyTo \\\\ Code,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
    def test_113(self):
        """test 113"""
        input = "\"\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\"  \'\"my\'\" \'\"code\'\"\""
        expect = "\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\"  \'\"my\'\" \'\"code\'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    def test_114(self):
        """test 114"""
        input = "\"\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\"\\n \\t \\b \\f \\r\'\"my\'\" \'\"code\'\"\""
        expect = "\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\"\\n \\t \\b \\f \\r\'\"my\'\" \'\"code\'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
    def test_115(self):
        """test 115"""
        input = "\"\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\" \\n \\t \\b \\n \\r\'\"my\'\" \'\"code\'\""
        expect = "\'\"Hello\'\", \'\"welcome\'\"  \'\"to\'\" \\n \\t \\b \\n \\r\'\"my\'\" \'\"code\',<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_116(self):
        """test 116"""
        input = "\""
        expect = "Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,116))
    ######################################################
    def test_117(self):
        """test 117"""
        input = "abc \"abc\""
        expect = "abc,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_118(self):
        """test 118"""
        input = "10.43 \"abc\""
        expect = "10.43,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_119(self):
        """test 119"""
        input = "\'123\' \"abc\""
        expect = "Error Token \'"
        self.assertTrue(TestLexer.test(input,expect,119))
    def test_120(self):
        """test 120"""
        input = "\"123\' \"abc\""
        expect = "123' ,abc,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,120))
    ########################################################
    def test_121(self):
        """test 121"""
        input = "\"123\" \"abc\""
        expect = "123,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,121))
    def test_122(self):
        """test 122"""
        input = "10.43 \"abc\""
        expect = "10.43,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,122))
    def test_123(self):
        """test 123"""
        input = "\"123\" \'abc\'"
        expect = "123,Error Token \'"
        self.assertTrue(TestLexer.test(input,expect,123))
    def test_124(self):
        """test 124"""
        input = "\"123\"  ##!abc&% "
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,124))
    def test_125(self):
        """test 125"""
        input = "number a  ##!abc&% \n "
        expect = "number,a,\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,125))
    ########################################################
    def test_126(self):
        """test 126"""
        input = "var i <- 5  ##!abc&% \n"
        expect = "var,i,<-,5,\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,126))
    def test_127(self):
        """test 127"""
        input = "var i <- \"this is string\"  ##this is comment \n"
        expect = "var,i,<-,this is string,\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,127))
    def test_128(self):
        """test 128"""
        input = "var i <- \"this is \\n \\t string\"  ##this is comment "
        expect = "var,i,<-,this is \\n \\t string,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,128))
    def test_129(self):
        """test 129"""
        input = "var i <- \"this is \\n \\i string\"  ##this is comment\n "
        expect = "var,i,<-,Illegal Escape In String: this is \\n \\i"
        self.assertTrue(TestLexer.test(input,expect,129))
    def test_130(self):
        """test 130"""
        input = "var i <- \"this is \\n \\t string"
        expect = "var,i,<-,Unclosed String: this is \\n \\t string"
        self.assertTrue(TestLexer.test(input,expect,130))
    ########################################################
    def test_131(self):
        """test 131"""
        input = "123a123"
        expect = "123,a123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,131))
    def test_132(self):
        """test 132"""
        input = "123.e10a123"
        expect = "123.e10,a123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,132))
    def test_133(self):
        """test 133"""
        input = "string a string b bool c number a dynamic f"
        expect = "string,a,string,b,bool,c,number,a,dynamic,f,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,133))
    def test_134(self):
        """test 134"""
        input = "123_123"
        expect = "123,_123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,134))
    def test_135(self):
        """test 135"""
        input = "abc_def"
        expect = "abc_def,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,135))
    #################################
    def test_136(self):
        """test 136"""
        input = "if \"abc\" else \"def\""
        expect = "if,abc,else,def,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,136))
    def test_137(self):
        """test 137"""
        input = "03"
        expect = "03,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,137))
    def test_138(self):
        """test 138"""
        input = "10230333643579.155775645545e-2"
        expect = "10230333643579.155775645545e-2,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,138))
    def test_139(self):
        """test 139"""
        input = "func main (number a)"
        expect = "func,main,(,number,a,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,139))
    def test_140(self):
        """test 140"""
        input = "103579.155e0"
        expect = "103579.155e0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,140))
    ########################################################
    def test_141(self):
        """test 141"""
        input = "begin var i<- 5 end"
        expect = "begin,var,i,<-,5,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,141))
    def test_142(self):
        """test 142"""
        input = "begin var i < 5 end"
        expect = "begin,var,i,<,5,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,142))
    def test_143(self):
        """test 143"""
        input = "{103579e-10}"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,143))
    def test_144(self):
        """test 144"""
        input = "return (false or true)"
        expect = "return,(,false,or,true,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,144))
    def test_145(self):
        """test 145"""
        input = "9999.(e-10"
        expect = "9999.,(,e,-,10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,145))
    ####################################################33
    def test_146(self):
        """test 146"""
        input = "return 0 or true"
        expect = "return,0,or,true,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,146))
    def test_147(self):
        """test 147"""
        input = "99999.E-10"
        expect = "99999.E-10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,147))
    def test_148(self):
        """test 148"""
        input = "return 0 OR 1 and 3"
        expect = "return,0,OR,1,and,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,148))
    def test_149(self):
        """test 149"""
        input = "99999.f-10"
        expect = "99999.,f,-,10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,149))
    def test_150(self):
        """test 150"""
        input = "+ - * % / = < > <= >= != == and or not"
        expect = "+,-,*,%,/,=,<,>,<=,>=,!=,==,and,or,not,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,150))
    #########################################################3
    def test_151(self):
        """test 151"""
        input = " 55.4e3 + 10.01 * 35 - 0 / 10"
        expect = "55.4e3,+,10.01,*,35,-,0,/,10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,151))
    def test_152(self):
        """test 152"""
        input = "|& or ! and and not or not 55.4e3"
        expect = "Error Token |"
        self.assertTrue(TestLexer.test(input,expect,152))
    def test_153(self):
        """test 153"""
        input = "55.4e3 or 10.01 and 35 - 0 & 10"
        expect = "55.4e3,or,10.01,and,35,-,0,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,153))
    def test_154(self):
        """test 154"""
        input = "( ) [ ] ... =="
        expect = "(,),[,],...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,154))
    def test_155(self):
        """test 155"""
        input = "( ))))))))))))))) [[[[[[[[[[[[[ ] c... a...b ========"
        expect = "(,),),),),),),),),),),),),),),),[,[,[,[,[,[,[,[,[,[,[,[,[,],c,...,a,...,b,==,==,==,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,155))
    #######################################################
    def test_156(self):
        """test 156"""
        input = " \" \' \" ... \" \' \" \t"
        expect = " ' ,..., ' ,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,156))
    def test_157(self):
        """test 157"""
        input = "\n"
        expect = "\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,157))
    def test_158(self):
        """test 158"""
        input = "\" ' \\n \\t \" ... \" \' \\x \""
        expect = " \' \\n \\t ,...,Illegal Escape In String:  \' \\x"
        self.assertTrue(TestLexer.test(input,expect,158))
    def test_159(self):
        """test 159"""
        input = "\t"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,159))
    ##########################################33
    def test_160(self):
        """test 160"""
        input = "10.43 \"abc\""
        expect = "10.43,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,160))
    def test_161(self):
        """test 161"""
        input = "\n\t\n"
        expect = "\n\n,\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,161))
    def test_162(self):
        """test 162"""
        input = "\" ' \\n \\t \" ... \" ' \\n \\t \""
        expect = " ' \\n \\t ,..., ' \\n \\t ,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,162))
    def test_163(self):
        """test 163"""
        input = "return break for until by + 1 if else"
        expect = "return,break,for,until,by,+,1,if,else,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,163))
    def test_164(self):
        """test 164"""
        input = "====================="
        expect = "==,==,==,==,==,==,==,==,==,==,=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,164))
    def test_165(self):
        """test 165"""
        input = "a_1 A_1"
        expect = "a_1,A_1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,165))
    def test_166(self):
        """test 166"""
        input = "PrintLN println"
        expect = "PrintLN,println,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,166))
    def test_167(self):
        """test 167"""
        input = "___"
        expect = "___,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,167))
    def test_168(self):
        """test 168"""
        input = "\"''\""
        expect = "'',<EOF>"
        self.assertTrue(TestLexer.test(input,expect,168))
    def test_169(self):
        """test 169"""
        input = "_9__a_aa 123"
        expect = "_9__a_aa,123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,169))
    def test_170(self):
        """test 170"""
        input = "_\"'_\""
        expect = "_,'_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
    def test_171(self):
        """test 1"""
        input = "a##aaaaaaaaaaaaa!@#**$&%$()"
        expect = "a,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,171))
    def test_172(self):
        """test 172"""
        input = "_@a"
        expect = "_,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,172))
    def test_173(self):
        """test 173"""
        input = "......."
        expect = "...,...,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,173))
    def test_174(self):
        """test 174"""
        input = "a = b + c"
        expect = "a,=,b,+,c,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,174))
    def test_175(self):
        """test 175"""
        input = "number a = 2110.0242e21 + 2e-1 - 2e+1"
        expect = "number,a,=,2110.0242e21,+,2e-1,-,2e+1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,175))

    def test_176(self):
        """test 176"""
        input = "a = b + c = d + e = e + f = f + g = 3 * 8 / 5 *7 +9 - 6.4 * 2"
        expect = "a,=,b,+,c,=,d,+,e,=,e,+,f,=,f,+,g,=,3,*,8,/,5,*,7,+,9,-,6.4,*,2,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,176))
    def test_177(self):
        """test 177"""
        input = "string new_string <- \"Hello World!\\n\""
        expect = "string,new_string,<-,Hello World!\\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,177))

    def test_178(self):
        """test 178"""
        input = " bool d = false number e = 1 "
        expect = "bool,d,=,false,number,e,=,1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,178))
    def test_179(self):
        """test 179"""
        input = " bool d <- true number e <- 1 "
        expect = "bool,d,<-,true,number,e,<-,1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,179))

    def test_180(self):
        """test 180"""
        input = "number e = 2110242.e2110242 string b <-\"2110242.e2110242\""
        expect = "number,e,=,2110242.e2110242,string,b,<-,2110242.e2110242,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,180))
    def test_181(self):
        """test 181"""
        input = "number e = 2110242.e2110242 string b <-\"2110242.e2110242"
        expect = "number,e,=,2110242.e2110242,string,b,<-,Unclosed String: 2110242.e2110242"
        self.assertTrue(TestLexer.test(input,expect,181))
    def test_182(self):
        """test 182"""
        input = "number e = 2110242.e2110242 string b <-\"2110242.e2110242\\i\""
        expect = "number,e,=,2110242.e2110242,string,b,<-,Illegal Escape In String: 2110242.e2110242\\i"
        self.assertTrue(TestLexer.test(input,expect,182))
    def test_183(self):
        """test 183"""
        input = "9999_99_99$$"
        expect = "9999,_99_99,Error Token $"
        self.assertTrue(TestLexer.test(input,expect,183))
    def test_184(self):
        """test 184"""
        input = "9999_99_99 and _90_00_1 and AAA_AAA_AAA or sssss or bbbbb"
        expect = "9999,_99_99,and,_90_00_1,and,AAA_AAA_AAA,or,sssss,or,bbbbb,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,184))
    def test_185(self):
        """test 185"""
        input = "if (i <= 10) or i = 0 \n i = i - 1"
        expect = "if,(,i,<=,10,),or,i,=,0,\n\n,i,=,i,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,185))
    def test_186(self):
        """test 186"""
        input = "func main() { var a <- 1 var b <- 2 }"
        expect = "func,main,(,),Error Token {"
        self.assertTrue(TestLexer.test(input,expect,186))
    def test_187(self):
        """test 187"""
        input = "1...3"
        expect = "1.,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,187))
    def test_188(self):
        """test 188"""
        input = "1..3"
        expect = "1.,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,188))
    def test_189(self):
        """test 189"""
        input = "1.3"
        expect = "1.3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,189))
    def test_190(self):
        """test 190"""
        input = "!===="
        expect = "!=,==,=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,190))
    def test_191(self):
        """test 191"""
        input = "if (a == b) return (true or false)"
        expect = "if,(,a,==,b,),return,(,true,or,false,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,191))
    def test_192(self):
        """test 192"""
        input = "if (a == b) return (true or false)"
        expect = "if,(,a,==,b,),return,(,true,or,false,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,192))
    def test_193(self):
        """test 193"""
        input = "'Yanxian' == 'Yanxian' || 'Yanxian' == 'Yanxian'"
        expect = "Error Token '"
        self.assertTrue(TestLexer.test(input,expect,193))
    def test_194(self):
        """test 194"""
        input = "#a sjd djf \n"
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input,expect,194))
    def test_195(self):
        """test 195"""
        input = "##a sjd djf \n ##asssssj"
        expect = "\n\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,195))
    def test_196(self):
        """test 196"""
        input = "##a sjd djf  ##a "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,196))
    def test_197(self):
        """test 197"""
        input = "##a\b \f "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197))
    def test_198(self):
        """test 198"""
        input = "\b\t\f "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198))
    def test_199(self):
        """test 199"""
        input = "_a_1_2_3_4_5\b\t\f ##@!$%^%#@@@$$$86544gnugyyt7dtyftyf88975776t"
        expect = "_a_1_2_3_4_5,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,199))