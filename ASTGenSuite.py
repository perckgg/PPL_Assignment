import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
#     def test_101(self):
#         input = """number a <- 5
#         """
#         expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(5.0))])"""
#         self.assertTrue(TestAST.test(input, expect, 101))
#     def test_102(self):
#         input = """number a <- 5
#         number b <- 6
#         """
#         expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(5.0)), VarDecl(Id(b), NumberType, None, NumLit(6.0))])"""
#         self.assertTrue(TestAST.test(input, expect, 102))
#     def test_103(self):
#         input = """func main(number a) return 1
#         """
#         expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Return(NumLit(1.0)))])"""
#         self.assertTrue(TestAST.test(input, expect, 103))
#     def test_104(self):
#         input = """func inc(number a) return a + 1
# func main() begin
# var a <- 1
# inc(a)
# writeNumber(a)
# end
# """
#         expect ="""Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
#         self.assertTrue(TestAST.test(input, expect, 104))
#     def test_105(self):
#         input = """func main(number a)
#         begin
#         write(1)
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([CallStmt(Id(write), [NumLit(1.0)])]))])"""
#         self.assertTrue(TestAST.test(input, expect, 105))
#     def test_106(self):
#         input = """func main() begin
# number a
# if (5 < 2) a <- 1
# elif (not true) a <- 2
# elif ("h" == "6") a <- 3
# end
# """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
#         self.assertTrue(TestAST.test(input, expect, 106))


#     def test_107(self):
#         input = """func main() begin
#         number a[5]
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([NumLit(5.0)], NumberType), None, None)]))])"""
#         self.assertTrue(TestAST.test(input, expect, 107))
#     def test_108(self):
#         input = """func main() begin
#         string b <- "hello"
#         string c <- "world"
#         string d <- b ... c
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), StringType, None, StringLit(hello)), VarDecl(Id(c), StringType, None, StringLit(world)), VarDecl(Id(d), StringType, None, BinaryOp(..., Id(b), Id(c)))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 108))
#     def test_109(self):
#         input = """func main() begin
#         string a <- (((((("a"))))))
#         write()
#         a[4] <- [3,4,5,[1,2]]
#         return
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), StringType, None, StringLit(a)), CallStmt(Id(write), []), AssignStmt(ArrayCell(Id(a), [NumLit(4.0)]), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0), ArrayLit(NumLit(1.0), NumLit(2.0)))), Return()]))])"""
#         self.assertTrue(TestAST.test(input, expect, 109))
#     def test_110(self):
#         input = """func main(number a[4,5]) begin
#         string a <- "hello"
#         write(a)
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([NumLit(4.0), NumLit(5.0)], NumberType), None, None)], Block([VarDecl(Id(a), StringType, None, StringLit(hello)), CallStmt(Id(write), [Id(a)])]))])"""
#         self.assertTrue(TestAST.test(input, expect, 110))
#     def test_111(self):
#         input = """func isPrime(number x) 
#         func main()
# begin
#     number x <- readNumber()
#     if (isPrime(x)) printString("Yes") 
#     else printString("No")

# end
# func isPrime(number x)
#     begin
#     if (x <= 1) return false
#     var i <- 2
#     for i until i > x / 2 by 1
#         begin
#             if (x % i = 0) return false
#         end
#     return true
#     end
# """
#         expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 111))
#     def test_112(self):
#         input = """## this is a comment
#             ## ## is also contained in comment






#             ## this is a comment




#             func main()      begin
#             number a
#             var a <- 12
#             var b <- \"something you must check \'\" \\r \\n \\t \\f \\b \\\'\'\"\"
#             dynamic cajfs____90928__
#             string ___________
#             number b[1, 2, 3, 0] <- [[123], 3, 4, [21324, [2123, 2, 1], [1, 2]]]
#             return 0
#             end
# """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(a), None, var, NumLit(12.0)), VarDecl(Id(b), None, var, StringLit(something you must check '" \\r \\n \\t \\f \\b \\''")), VarDecl(Id(cajfs____90928__), None, dynamic, None), VarDecl(Id(___________), StringType, None, None), VarDecl(Id(b), ArrayType([NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(0.0)], NumberType), None, ArrayLit(ArrayLit(NumLit(123.0)), NumLit(3.0), NumLit(4.0), ArrayLit(NumLit(21324.0), ArrayLit(NumLit(2123.0), NumLit(2.0), NumLit(1.0)), ArrayLit(NumLit(1.0), NumLit(2.0))))), Return(NumLit(0.0))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 112))
#     def test_113(self):
#         input = """func main() begin
#         number a <- 1
#         if (a < 2) a <- 1
#         elif (a > 3) a <- 2
#         elif (a == 4) a <- 3
#         else a <- 4
#         end
#         """
#         expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.0)), If((BinaryOp(<, Id(a), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(BinaryOp(>, Id(a), NumLit(3.0)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, Id(a), NumLit(4.0)), AssignStmt(Id(a), NumLit(3.0)))], AssignStmt(Id(a), NumLit(4.0)))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 113))
#     def test_114(self):
#         input = """func test_if(string a[1, 2, 3])
# begin
#     if (a < b)
#     if (a < b) number c
#     elif (a < c)
#     if (a < b) if (a < b) number c
#     else number c
#     if (a < b)
#     if (a < b) if (a < b)
#         number c
#     else number c
#     if (a < b) number c
#     elif (a < b) number c
#     else number c
# end
# """
#         expect = """Program([FuncDecl(Id(test_if), [VarDecl(Id(a), ArrayType([NumLit(1.0), NumLit(2.0), NumLit(3.0)], StringType), None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(c)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None))], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 114))
#     def test_115(self):
#         input = """func test_if(string a[1, 2, 3])
# begin
#     if (a < b)
#     if (a < b) number c
#     elif (a < c)
#         if (a < b) 
#             if (a < b) number c
#             else var c <- "hello"
#         else dynamic c <- 6
#     else return (a+b) or (a-b)
#     return a
#     end
#     """
#         expect = """Program([FuncDecl(Id(test_if), [VarDecl(Id(a), ArrayType([NumLit(1.0), NumLit(2.0), NumLit(3.0)], StringType), None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(c)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), None, var, StringLit(hello)))), [], VarDecl(Id(c), None, dynamic, NumLit(6.0))))], Return(BinaryOp(or, BinaryOp(+, Id(a), Id(b)), BinaryOp(-, Id(a), Id(b)))))), [], None), Return(Id(a))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 115))
#     def test_116(self):
#         input = """
# ## this is pre-declaration func
# func main()


# ## this is function definition
# func main()     begin
#     number a <- 1.2e-12
#     number c <- (b + a) / c * a - d + goo()[1, 2, 3] * goo(a + b) * a[1, foo(), _c]
#     foo()
#     number k <- goo()[a + b, foo(), 1e-1]
#     return a
# end
# """
#         expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.2e-12)), VarDecl(Id(c), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(*, BinaryOp(/, BinaryOp(+, Id(b), Id(a)), Id(c)), Id(a)), Id(d)), BinaryOp(*, BinaryOp(*, ArrayCell(CallExpr(Id(goo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), CallExpr(Id(goo), [BinaryOp(+, Id(a), Id(b))])), ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(foo), []), Id(_c)])))), CallStmt(Id(foo), []), VarDecl(Id(k), NumberType, None, ArrayCell(CallExpr(Id(goo), []), [BinaryOp(+, Id(a), Id(b)), CallExpr(Id(foo), []), NumLit(0.1)])), Return(Id(a))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 116))
#     def test_117(self):
#         input = """
# func test_looping(string a[1, 2], number __[0], bool cc_c)
# begin
#     if (a > b)
#         for a until a + 1 by b + 1 if (a > b)
#                 if (a > b) number c
#                 elif (a > b) number c
#                 elif (a > b) number c
#                 else number c
#             else
#                 break
#     else
#         for a until a > b by a * b / c
#             for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
#                 if (a > b) number c
#                 else number c
# end
# """
#         expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([NumLit(1.0), NumLit(2.0)], StringType), None, None), VarDecl(Id(__), ArrayType([NumLit(0.0)], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 117))
#     def test_118(self):
#         input = """func main(number a, number b) begin
# number a[1, 2] <- [[2, 3]]
# string b <- 1.e-12
# bool c <- "abc"
# return main(a, 3, d, b)
# end
# """
#         expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(a), ArrayType([NumLit(1.0), NumLit(2.0)], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)))), VarDecl(Id(b), StringType, None, NumLit(1e-12)), VarDecl(Id(c), BoolType, None, StringLit(abc)), Return(CallExpr(Id(main), [Id(a), NumLit(3.0), Id(d), Id(b)]))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 118))
#     def test_119(self):
#         input = """
# func test_exp()
# begin
#     bool a <- not not a and b or not not c or d or e and b < not not not c and d or e or not not e
#     return a
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<, BinaryOp(and, BinaryOp(or, BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, Id(a))), Id(b)), UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), Id(b)), BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), UnaryOp(not, UnaryOp(not, Id(e)))))), Return(Id(a))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 119))
#     def test_120(self):
#         input =  """
# func test_exp()
# begin
#     bool a <- a <= (b = ((k > (h == (b < c))) < (d > (e == f))))
#     return a
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<=, Id(a), BinaryOp(=, Id(b), BinaryOp(<, BinaryOp(>, Id(k), BinaryOp(==, Id(h), BinaryOp(<, Id(b), Id(c)))), BinaryOp(>, Id(d), BinaryOp(==, Id(e), Id(f))))))), Return(Id(a))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 120))
#     def test_121(self):
#         input = """
# func test_exp()
# begin
#     number a <- a[1, [1, 2]]
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(a), [NumLit(1.0), ArrayLit(NumLit(1.0), NumLit(2.0))]))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 121))
#     def test_122(self):
#         input = """
# func test_exp()
# begin
#     number a <- c[1, d[1, 2, 3, foo()[1, 2]], goo() + 1 * 3 / b, h[1, 1]]
#     return a
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(c), [NumLit(1.0), ArrayCell(Id(d), [NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0)])]), BinaryOp(+, CallExpr(Id(goo), []), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(3.0)), Id(b))), ArrayCell(Id(h), [NumLit(1.0), NumLit(1.0)])])), Return(Id(a))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 122))
#     def test_123(self):
#         input = """
# func test_exp()
# begin
#     number a <- [1, [1], [[1]], [[[1]]], [[[[1]]]]]
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), ArrayLit(NumLit(1.0)), ArrayLit(ArrayLit(NumLit(1.0))), ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))), ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))))))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 123))
#     def test_124(self):
#         input = """
# func foo123478_main_09()
# begin
#     number a <- [1, 2, [1, 2, [1, 4]], [3, 4]]
# end
# """ 
#         expect = """Program([FuncDecl(Id(foo123478_main_09), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(4.0))), ArrayLit(NumLit(3.0), NumLit(4.0))))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 124))
#     def test_125(self):
#         input = """
# func main(number a[5])
# begin
#     number n <- a[0]
#     for i until n by 1
#         begin
#             number b <- a[i]
#             if i = n
#                 break
#             else continue
#         end
# end
# """
#         expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([NumLit(5.0)], NumberType), None, None)], Block([VarDecl(Id(n), NumberType, None, ArrayCell(Id(a), [NumLit(0.0)])), For(Id(i), Id(n), NumLit(1.0), Block([VarDecl(Id(b), NumberType, None, ArrayCell(Id(a), [Id(i)])), If((BinaryOp(=, Id(i), Id(n)), Break), [], Continue)]))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 125))
#     def test_126(self):
#         input = """
# func test_exp()
# begin
#     number a <- a[1, [1, 2]]
#     string b <- ""
#     string c <- a
#     var i <- 0
#     dynamic d <- b
#     string b <- [a, b, c, d, i] + [a, b, c, d, i] * foo(1,2,3,4,5)[1,2,3,4,5]
# end
# """
#         expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(a), [NumLit(1.0), ArrayLit(NumLit(1.0), NumLit(2.0))])), VarDecl(Id(b), StringType, None, StringLit()), VarDecl(Id(c), StringType, None, Id(a)), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(d), None, dynamic, Id(b)), VarDecl(Id(b), StringType, None, BinaryOp(+, ArrayLit(Id(a), Id(b), Id(c), Id(d), Id(i)), BinaryOp(*, ArrayLit(Id(a), Id(b), Id(c), Id(d), Id(i)), ArrayCell(CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)]), [NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)]))))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 126))
#     def test_127(self):
#         input = """
# func main()
# begin
# end
# """
#         expect = """Program([FuncDecl(Id(main), [], Block([]))])"""
#         self.assertTrue(TestAST.test(input, expect, 127))
#     def test_128(self):
#         input = """
# func main() return
# """
#         expect = """Program([FuncDecl(Id(main), [], Return())])"""
#         self.assertTrue(TestAST.test(input, expect, 128))
#     def test_129(self):
#         input = """
# func main() return a + b
# func submain(string a, number b) return
# func test()
# """
#         expect = """Program([FuncDecl(Id(main), [], Return(BinaryOp(+, Id(a), Id(b)))), FuncDecl(Id(submain), [VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), NumberType, None, None)], Return()), FuncDecl(Id(test), [], None)])"""
#         self.assertTrue(TestAST.test(input, expect, 129))
#     def test_130(self):
#         input = """
# func main()
# begin
# if x == 3 return true
# if x == 4 return 1
# else return false
# end
# """
#         expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, Id(x), NumLit(3.0)), Return(BooleanLit(True))), [], None), If((BinaryOp(==, Id(x), NumLit(4.0)), Return(NumLit(1.0))), [], Return(BooleanLit(False)))]))])"""
#         self.assertTrue(TestAST.test(input, expect, 130))
#     def test_131(self):
#         input = """
# func callingDestroyer()
# begin
#     call()
#     call(call())
#     call(call(call()))
#     call(call(call(call())))
#     call(call(call(call(call()))))
#     call(call(call(call(call(call())))))
#     call(call(call(call(call(call(call()))))))
#     call(call(call(call(call(call(call(call())))))))
#     call(call(call(call(call(call(call(call(call()))))))))
#     call(call(call(call(call(call(call(call(call(call())))))))))
#     call(call(call(call(call(call(call(call(call(call(call()))))))))))
#     call(call(call(call(call(call(call(call(call(call(call(call())))))))))))
#     call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))
#     call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))
#     call(call(call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))))
#     call(call(call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))))
# end
# """
#         expect= """"""
# #         self.assertTrue(TestAST.test(input, expect, 131))
#     def test_132(self):
#         input = """
# func subDestroyer()
# begin
#     number a <- (b)
#     number a <- ((b))
#     number a <- (((b)))
#     number a <- ((((b))))
#     number a <- (((((b)))))
#     number a <- ((((((b))))))
#     number a <- (((((((b)))))))
#     number a <- ((((((((b))))))))
#     number a <- (((((((((b)))))))))
#     number a <- ((((((((((b))))))))))
#     number a <- (((((((((((b)))))))))))
#     number a <- ((((((((((((b))))))))))))
#     number a <- (((((((((((((b)))))))))))))
#     number a <- ((((((((((((((b))))))))))))))
#     number a <- (((((((((((((((b)))))))))))))))
# end
# """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 132))
#     def test_133(self):
#         input = """
# func arrayDestroyer()
# begin
#     number a <- [[[[[[[[[[[[[[[[[[[[[[[[[[[[[foo()[1, 2, 3]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# end
# """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 133))
#     def test_134(self):
#         input = """
# func unaryDestroyer()
# begin
#     a <- not not not---(not-(not-(not not-(not not not-(not not not not----(not-----(not not---(not not not--(foo()[0])))))))))
# end
# """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 134))
#     def test_135(self):
#         input = """
# func main()
# begin
#     number x <- [foo(), foo()[1, 2, 3], x[0, 1], 12 > 3]
# end
# """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 135))
#     def test_136(self):
#         input = """
# func main(number a, string s, bool _, number xxx[1, 2, 3])
# begin
#     do_something(a, s, _, xxx)
# end
# """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 136))
#     def test_137(self):
#         input = """
# func main() 
# begin
#     var i <- 0
#     number a <- [123,1234,12345,123456,foo()[1,2,3],[1,2,3,4]]
#     end
#     """
#         expect= """"""
#         self.assertTrue(TestAST.test(input, expect, 137))

    def test_300(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        if (3)
            c()
        elif (4)
            d()
        else
            e()
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(b), [])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(c), [])), [(NumLit(4.0), CallStmt(Id(d), []))], CallStmt(Id(e), [])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """
string s <- a ... b
"""
        expect = """Program([VarDecl(Id(s), StringType, None, BinaryOp(..., Id(a), Id(b)))])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """
func a()
begin
    begin
        begin
            begin
                begin
                    begin
                        begin
                        call()
                            begin
                                ##aaaa
                                call()
                                call()
                            end
                        end
                    end
                end
            end
        end
    end
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([Block([Block([Block([Block([Block([Block([CallStmt(Id(call), []), Block([CallStmt(Id(call), []), CallStmt(Id(call), [])])])])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """
func abc(number _a, string a0, number b[1, 2, 0])
begin
    if (a > b) number c
    elif (  a > b) number c
    if (a > b   ) number c
    elif ( a > b ) number c
    else number c
    if (     a > b ) number c
    else number c
    return c
end
"""
        expect = """Program([FuncDecl(Id(abc), [VarDecl(Id(_a), NumberType, None, None), VarDecl(Id(a0), StringType, None, None), VarDecl(Id(b), ArrayType([1.0, 2.0, 0.0], NumberType), None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], None), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)), Return(Id(c))]))])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """
## this is pre-declaration func
func main()


## this is function definition
func main()     begin
    number a <- 1.2e-12
    number c <- (b + a) / c * a - d + goo()[1, 2, 3] * goo(a + b) * a[1, foo(), _c]
    foo()
    number k <- goo()[a + b, foo(), 1e-1]
    return a
end
"""
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.2e-12)), VarDecl(Id(c), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(*, BinaryOp(/, BinaryOp(+, Id(b), Id(a)), Id(c)), Id(a)), Id(d)), BinaryOp(*, BinaryOp(*, ArrayCell(CallExpr(Id(goo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), CallExpr(Id(goo), [BinaryOp(+, Id(a), Id(b))])), ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(foo), []), Id(_c)])))), CallStmt(Id(foo), []), VarDecl(Id(k), NumberType, None, ArrayCell(CallExpr(Id(goo), []), [BinaryOp(+, Id(a), Id(b)), CallExpr(Id(foo), []), NumLit(0.1)])), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """
## this is a comment




## this is a comment
    ## this is a comment
func test_comment() ##this is no space comment
begin
    number a ## this is allowed
    return false
end
"""
        expect = """Program([FuncDecl(Id(test_comment), [], Block([VarDecl(Id(a), NumberType, None, None), Return(BooleanLit(False))]))])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """
func main(number a, number b) begin
number a[1, 2] <- [[2, 3]]
string b <- 1.e-12
bool c <- "abc"
return main(a, 3, d, b)
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)))), VarDecl(Id(b), StringType, None, NumLit(1e-12)), VarDecl(Id(c), BoolType, None, StringLit(abc)), Return(CallExpr(Id(main), [Id(a), NumLit(3.0), Id(d), Id(b)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """
func test_if(string a[1, 2, 3])
begin
    if (a < b)
    if (a < b) number c
    elif (a < c)
    if (a < b) if (a < b) number c
    else number c
    if (a < b)
    if (a < b) if (a < b)
        number c
    else number c
    if (a < b) number c
    elif (a < b) number c
    else number c
end
"""
        expect = """Program([FuncDecl(Id(test_if), [VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], StringType), None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(c)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None))], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """
func test_exp()
begin
    bool a <- not not a and b or not not c or d or e and b < not not not c and d or e or not not e
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<, BinaryOp(and, BinaryOp(or, BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, Id(a))), Id(b)), UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), Id(b)), BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), UnaryOp(not, UnaryOp(not, Id(e)))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """
func test_exp()
begin
    bool a <- a <= (b = ((k > (h == (b < c))) < (d > (e == f))))
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<=, Id(a), BinaryOp(=, Id(b), BinaryOp(<, BinaryOp(>, Id(k), BinaryOp(==, Id(h), BinaryOp(<, Id(b), Id(c)))), BinaryOp(>, Id(d), BinaryOp(==, Id(e), Id(f))))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """
func test_exp()
begin
    number a <- a[1, [1, 2]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(a), [NumLit(1.0), ArrayLit(NumLit(1.0), NumLit(2.0))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """
func test_exp()
begin
    number a <- c[1, d[1, 2, 3, foo()[1, 2]], goo() + 1 * 3 / b, h[1, 1]]
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(c), [NumLit(1.0), ArrayCell(Id(d), [NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0)])]), BinaryOp(+, CallExpr(Id(goo), []), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(3.0)), Id(b))), ArrayCell(Id(h), [NumLit(1.0), NumLit(1.0)])])), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """
func test_exp()
begin
    number a <- [1, [1], [[1]], [[[1]]], [[[[1]]]]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), ArrayLit(NumLit(1.0)), ArrayLit(ArrayLit(NumLit(1.0))), ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))), ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """
func foo123478_main_09()
begin
    number a <- [1, 2, [1, 2, [1, 4]], [3, 4]]
end
"""
        expect = """Program([FuncDecl(Id(foo123478_main_09), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(4.0))), ArrayLit(NumLit(3.0), NumLit(4.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """
func callingDestroyer()
begin
    call()
    call(call())
    call(call(call()))
    call(call(call(call())))
    call(call(call(call(call()))))
    call(call(call(call(call(call())))))
    call(call(call(call(call(call(call()))))))
    call(call(call(call(call(call(call(call())))))))
    call(call(call(call(call(call(call(call(call()))))))))
    call(call(call(call(call(call(call(call(call(call())))))))))
    call(call(call(call(call(call(call(call(call(call(call()))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call())))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))))
end
"""
        expect = """Program([FuncDecl(Id(callingDestroyer), [], Block([CallStmt(Id(call), []), CallStmt(Id(call), [CallExpr(Id(call), [])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """
func subDestroyer()
begin
    number a <- (b)
    number a <- ((b))
    number a <- (((b)))
    number a <- ((((b))))
    number a <- (((((b)))))
    number a <- ((((((b))))))
    number a <- (((((((b)))))))
    number a <- ((((((((b))))))))
    number a <- (((((((((b)))))))))
    number a <- ((((((((((b))))))))))
    number a <- (((((((((((b)))))))))))
    number a <- ((((((((((((b))))))))))))
    number a <- (((((((((((((b)))))))))))))
    number a <- ((((((((((((((b))))))))))))))
    number a <- (((((((((((((((b)))))))))))))))
end
"""
        expect = """Program([FuncDecl(Id(subDestroyer), [], Block([VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b))]))])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """
func arrayDestroyer()
begin
    number a <- [[[[[[[[[[[[[[[[[[[[[[[[[[foo()[1, 2, 3]]]]]]]]]]]]]]]]]]]]]]]]]]]
end
"""
        expect = """Program([FuncDecl(Id(arrayDestroyer), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))))))))))))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """
func unaryDestroyer()
begin
    a <- not not not---(not-(not-(not not-(not not not-(not not not not----(not-----(not not---(not not not--(foo()[0])))))))))
end
"""
        expect = """Program([FuncDecl(Id(unaryDestroyer), [], Block([AssignStmt(Id(a), UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, ArrayCell(CallExpr(Id(foo), []), [NumLit(0.0)])))))))))))))))))))))))))))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
func main()
begin
    number x <- [foo(), foo()[1, 2, 3], x[0, 1], 12 > 3]
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, ArrayLit(CallExpr(Id(foo), []), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), ArrayCell(Id(x), [NumLit(0.0), NumLit(1.0)]), BinaryOp(>, NumLit(12.0), NumLit(3.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """
func main(number a, string s, bool _, number xxx[1, 2, 3])
begin
    do_something(a, s, _, xxx)
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(s), StringType, None, None), VarDecl(Id(_), BoolType, None, None), VarDecl(Id(xxx), ArrayType([1.0, 2.0, 3.0], NumberType), None, None)], Block([CallStmt(Id(do_something), [Id(a), Id(s), Id(_), Id(xxx)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """
func __aaa__()
begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a" ... "b", foo()["index"]], [(a and not c) = d]]
end
"""
        expect = """Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a), StringLit(b)), ArrayCell(CallExpr(Id(foo), []), [StringLit(index)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
func calc()
begin
    number a <- 5 ## This is a
    number b <- 5 ## This is b
    number c <- 5 ## This is c
    number d <- 5 ## This is d
    ## This is e number e <- a + b + c + d
    number e <- (a) + (b) + ((c) + (d))
    return e ## This is return
end ## This is end of function
"""
        expect = """Program([FuncDecl(Id(calc), [], Block([VarDecl(Id(a), NumberType, None, NumLit(5.0)), VarDecl(Id(b), NumberType, None, NumLit(5.0)), VarDecl(Id(c), NumberType, None, NumLit(5.0)), VarDecl(Id(d), NumberType, None, NumLit(5.0)), VarDecl(Id(e), NumberType, None, BinaryOp(+, BinaryOp(+, Id(a), Id(b)), BinaryOp(+, Id(c), Id(d)))), Return(Id(e))]))])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """
## This is a comment
 ## This is a comment
  ## This is a comment
   ## This is a comment
    ## This is a comment
     ## This is a comment
      ## This is a comment
       ## This is a comment
        ## This is a comment
         ## This is a comment


func main()
begin
    if (not not not (a and b or c and not d)) if (not not not (a and b or c and not d))
    if (not not not (a and b or c and d))
    if (not not not (a and b or c > d))
    if (foo()[1, 0])
    if ("string") if ([1, 2, 3, 4])
    if ((("a" ... "b") ... c) > ((a * b * d + foo()[1, 2, 3]) <= (not a and not not c)))
    if ((("a" ... "b") ... c) > ((a * b * d + foo()[1, 2, 3]) <= (not a and not not c)))
    if ((foo() + _() - __(12, 3, "abc", [1, 2, 3])) > __aaa__("a", "", "\\n", abc, not false, true))
    if (true) if (false) do_something()
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), UnaryOp(not, Id(d)))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), UnaryOp(not, Id(d)))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), Id(d))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(>, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), Id(d))))), If((ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(0.0)]), If((StringLit(string), If((ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), If((BinaryOp(>, BinaryOp(..., BinaryOp(..., StringLit(a), StringLit(b)), Id(c)), BinaryOp(<=, BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), Id(d)), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), BinaryOp(and, UnaryOp(not, Id(a)), UnaryOp(not, UnaryOp(not, Id(c)))))), If((BinaryOp(>, BinaryOp(..., BinaryOp(..., StringLit(a), StringLit(b)), Id(c)), BinaryOp(<=, BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), Id(d)), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), BinaryOp(and, UnaryOp(not, Id(a)), UnaryOp(not, UnaryOp(not, Id(c)))))), If((BinaryOp(>, BinaryOp(-, BinaryOp(+, CallExpr(Id(foo), []), CallExpr(Id(_), [])), CallExpr(Id(__), [NumLit(12.0), NumLit(3.0), StringLit(abc), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))])), CallExpr(Id(__aaa__), [StringLit(a), StringLit(), StringLit(\\n), Id(abc), UnaryOp(not, BooleanLit(False)), BooleanLit(True)])), If((BooleanLit(True), If((BooleanLit(False), CallStmt(Id(do_something), [])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """
func main()
begin
    number i0
    number i1
    number i2
    number i3
    number i4
    number i5
    number i6
    number i7
    for i0 until true by 1
        for i1 until false by _ * _
            for i2 until ("a" ... "c") > (not b and c or d) by 12.12e-12
                for i3 until b >= (c + foo()[1, 2]) by foo("abc", d, true)
                    for i4 until -3 or -x by "string"
                        for i5 until "" by [1, 2, 3]
                            for i6 until [[foo()[0, 0]]] by 12.e-2
                                for i7 until false by _(_,_,_)
                                    do_something()
    return
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i0), NumberType, None, None), VarDecl(Id(i1), NumberType, None, None), VarDecl(Id(i2), NumberType, None, None), VarDecl(Id(i3), NumberType, None, None), VarDecl(Id(i4), NumberType, None, None), VarDecl(Id(i5), NumberType, None, None), VarDecl(Id(i6), NumberType, None, None), VarDecl(Id(i7), NumberType, None, None), For(Id(i0), BooleanLit(True), NumLit(1.0), For(Id(i1), BooleanLit(False), BinaryOp(*, Id(_), Id(_)), For(Id(i2), BinaryOp(>, BinaryOp(..., StringLit(a), StringLit(c)), BinaryOp(or, BinaryOp(and, UnaryOp(not, Id(b)), Id(c)), Id(d))), NumLit(1.212e-11), For(Id(i3), BinaryOp(>=, Id(b), BinaryOp(+, Id(c), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0)]))), CallExpr(Id(foo), [StringLit(abc), Id(d), BooleanLit(True)]), For(Id(i4), BinaryOp(or, UnaryOp(-, NumLit(3.0)), UnaryOp(-, Id(x))), StringLit(string), For(Id(i5), StringLit(), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), For(Id(i6), ArrayLit(ArrayLit(ArrayCell(CallExpr(Id(foo), []), [NumLit(0.0), NumLit(0.0)]))), NumLit(0.12), For(Id(i7), BooleanLit(False), CallExpr(Id(_), [Id(_), Id(_), Id(_)]), CallStmt(Id(do_something), []))))))))), Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
number arr[0, 0, 0] <- [1, 2, 3]
string arr[0, 0, 0] <- ["a", "b", "c"]
bool arr[0, 0, 0] <- [true, true, false]
func main()
begin
    number x <- arr[0, 0]
    return[1, 2, 3]
    return-3
    return"abc"
    return"abc\\t\\n\\b\\f\\r\\\\\\''""
end
"""
        expect = """Program([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], StringType), None, ArrayLit(StringLit(a), StringLit(b), StringLit(c))), VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], BoolType), None, ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False))), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, ArrayCell(Id(arr), [NumLit(0.0), NumLit(0.0)])), Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), Return(UnaryOp(-, NumLit(3.0))), Return(StringLit(abc)), Return(StringLit(abc\\t\\n\\b\\f\\r\\\\\\''"))]))])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """
func foo(number a, string s)
func main(bool arr)
func goo(number ABDS__)
func build(number ABC1092__ADBsdlhs__)
func create(number dosomething)
func hey(string arr[1, 2, 3])
func go(string arr[3, 4, 5])
func do()
func ____()
func _____abc____ABC___()
func ODLLAHJLBOSE()
func xxxxxxxxxxxxx()
"""
        expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(s), StringType, None, None)], None), FuncDecl(Id(main), [VarDecl(Id(arr), BoolType, None, None)], None), FuncDecl(Id(goo), [VarDecl(Id(ABDS__), NumberType, None, None)], None), FuncDecl(Id(build), [VarDecl(Id(ABC1092__ADBsdlhs__), NumberType, None, None)], None), FuncDecl(Id(create), [VarDecl(Id(dosomething), NumberType, None, None)], None), FuncDecl(Id(hey), [VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, None)], None), FuncDecl(Id(go), [VarDecl(Id(arr), ArrayType([3.0, 4.0, 5.0], StringType), None, None)], None), FuncDecl(Id(do), [], None), FuncDecl(Id(____), [], None), FuncDecl(Id(_____abc____ABC___), [], None), FuncDecl(Id(ODLLAHJLBOSE), [], None), FuncDecl(Id(xxxxxxxxxxxxx), [], None)])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """
func main()
begin
    number a <- 5
    begin
        number b <- 5
        begin
            number c <- 5
            begin
                number d <- a + (b) + (c) + d
                return d
            end
        end
    end
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(b), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(c), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(d), NumberType, None, BinaryOp(+, BinaryOp(+, BinaryOp(+, Id(a), Id(b)), Id(c)), Id(d))), Return(Id(d))])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """
func main()
begin 
    hello()
    kkap(kk(yeah(ha(idk(2,4,[2,4,[[[[[[[[[[[2]]]]]]]]]]],45],4)))))
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(hello), []), CallStmt(Id(kkap), [CallExpr(Id(kk), [CallExpr(Id(yeah), [CallExpr(Id(ha), [CallExpr(Id(idk), [NumLit(2.0), NumLit(4.0), ArrayLit(NumLit(2.0), NumLit(4.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(2.0)))))))))))), NumLit(45.0)), NumLit(4.0)])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (a) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(a), Return()), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) if (c) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) return
    elif (c) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), Return()), (Id(c), Return())], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) if (c) return
    var x <-  2
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None), VarDecl(Id(x), None, var, NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return())]))])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """
func a() 
begin
    if (d) if (b) if(g) d()
    else return
    else return
    elif (j) return 2
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), If((Id(g), CallStmt(Id(d), [])), [], Return())), [], Return())), [(Id(j), Return(NumLit(2.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
    else return
    if (tiep) ha()
    elif (dung) ha()
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return()), If((Id(tiep), CallStmt(Id(ha), [])), [(Id(dung), CallStmt(Id(ha), []))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """
func a() 
begin
    for doo until (doo <= 2) by "hello"...l
        exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    if  (a) 
    if (b) return
    elif (c) return
    else return
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello), Id(l)), CallStmt(Id(exe), [])), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), If((Id(a), If((Id(b), Return()), [(Id(c), Return())], Return())), [], Return())]))])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """
func a() 
begin
    for doo until (doo <= 2) by "hello'""...l
        for doo until (doo <= 2) by "hello'""...l
            for doo until (doo <= 2) by "hello'""...l
                if (a) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                elif (b) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                else no()
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), If((Id(a), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return())), [(Id(b), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return()))], CallStmt(Id(no), [])))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """
func __aaa__()
begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a\\'" ... "b\\'", foo()["index\\\\"]], [(a and not c) = d]]
end
"""
        expect = """Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a\\'), StringLit(b\\')), ArrayCell(CallExpr(Id(foo), []), [StringLit(index\\\\)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
func qq(number bbb, number qqq, string a)	
begin
    if(a) return
    elif(b) if (c) if (d) call() 
    else return
    else return
    elif (c) call()
end
"""
        expect = """Program([FuncDecl(Id(qq), [VarDecl(Id(bbb), NumberType, None, None), VarDecl(Id(qqq), NumberType, None, None), VarDecl(Id(a), StringType, None, None)], Block([If((Id(a), Return()), [(Id(b), If((Id(c), If((Id(d), CallStmt(Id(call), [])), [], Return())), [], Return())), (Id(c), CallStmt(Id(call), []))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
end
"""
        expect = """Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [], None))], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
            elif (false) i<-toAsciiCode("1")
            else i<-0
        elif (true) i<-1
end
"""
        expect = """Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [(BooleanLit(False), AssignStmt(Id(i), CallExpr(Id(toAsciiCode), [StringLit(1)])))], AssignStmt(Id(i), NumLit(0.0)))), (BooleanLit(True), AssignStmt(Id(i), NumLit(1.0)))], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """
func main() begin 
var i<-0
for i until i=1 by 1
    if (i=0) break 
end 
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(1.0)), NumLit(1.0), If((BinaryOp(=, Id(i), NumLit(0.0)), Break), [], None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """
func main() begin 
var i<-0
for i until i=10 by 1
    begin 
        var j<--0.87e-4
        i <- i*j
        continue
    end
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, UnaryOp(-, NumLit(8.7e-05))), AssignStmt(Id(i), BinaryOp(*, Id(i), Id(j))), Continue]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
func integral(number a, number b,number c) return c*b-c*a 
func sin(number x,bool degree, number exactrate) begin 
    var pi <- 3.141592653589793238462643383279502884197
    if (degree) x<- x*pi/180
    x<- x%(2*pi)
    number pow <- x 
    dynamic i<-1
    dynamic fact <- 1
    dynamic res <- 2*x
    for i until i=exactrate by 2
    begin
        res <- res - pow/fact 
        pow <- pow * x * X
        fact <- fact*i*(i-1)
    end
    return res
end
func main() begin 
    var n1 <- 1
    var n2 <- 2
    var n3 <- 3
    var n4 <- 4
    var b1 <- true 
    var b2 <- fasle 
    var b3 <- not true 
    var b4 <- true or false 
    dynamic res 
    res <- ( integral((n1*2 + 2*n1*n2 - n3*-n4)*n1%n2/n3+n4--n1*sin(3.14,false,701)) > sin(n1*n2-n3%n4,n1=n2*3-n4+sin(n1,n2>n3,701*n2%1),701) ) or (not b1 and b2 and not b3 or b4) and (b1 and not b4 or b3 and not b2)
end
"""
        expect = """Program([FuncDecl(Id(integral), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Return(BinaryOp(-, BinaryOp(*, Id(c), Id(b)), BinaryOp(*, Id(c), Id(a))))), FuncDecl(Id(sin), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(degree), BoolType, None, None), VarDecl(Id(exactrate), NumberType, None, None)], Block([VarDecl(Id(pi), None, var, NumLit(3.141592653589793)), If((Id(degree), AssignStmt(Id(x), BinaryOp(/, BinaryOp(*, Id(x), Id(pi)), NumLit(180.0)))), [], None), AssignStmt(Id(x), BinaryOp(%, Id(x), BinaryOp(*, NumLit(2.0), Id(pi)))), VarDecl(Id(pow), NumberType, None, Id(x)), VarDecl(Id(i), None, dynamic, NumLit(1.0)), VarDecl(Id(fact), None, dynamic, NumLit(1.0)), VarDecl(Id(res), None, dynamic, BinaryOp(*, NumLit(2.0), Id(x))), For(Id(i), BinaryOp(=, Id(i), Id(exactrate)), NumLit(2.0), Block([AssignStmt(Id(res), BinaryOp(-, Id(res), BinaryOp(/, Id(pow), Id(fact)))), AssignStmt(Id(pow), BinaryOp(*, BinaryOp(*, Id(pow), Id(x)), Id(X))), AssignStmt(Id(fact), BinaryOp(*, BinaryOp(*, Id(fact), Id(i)), BinaryOp(-, Id(i), NumLit(1.0))))])), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n1), None, var, NumLit(1.0)), VarDecl(Id(n2), None, var, NumLit(2.0)), VarDecl(Id(n3), None, var, NumLit(3.0)), VarDecl(Id(n4), None, var, NumLit(4.0)), VarDecl(Id(b1), None, var, BooleanLit(True)), VarDecl(Id(b2), None, var, Id(fasle)), VarDecl(Id(b3), None, var, UnaryOp(not, BooleanLit(True))), VarDecl(Id(b4), None, var, BinaryOp(or, BooleanLit(True), BooleanLit(False))), VarDecl(Id(res), None, dynamic, None), AssignStmt(Id(res), BinaryOp(and, BinaryOp(or, BinaryOp(>, CallExpr(Id(integral), [BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(%, BinaryOp(*, BinaryOp(-, BinaryOp(+, BinaryOp(*, Id(n1), NumLit(2.0)), BinaryOp(*, BinaryOp(*, NumLit(2.0), Id(n1)), Id(n2))), BinaryOp(*, Id(n3), UnaryOp(-, Id(n4)))), Id(n1)), Id(n2)), Id(n3)), Id(n4)), BinaryOp(*, UnaryOp(-, Id(n1)), CallExpr(Id(sin), [NumLit(3.14), BooleanLit(False), NumLit(701.0)])))]), CallExpr(Id(sin), [BinaryOp(-, BinaryOp(*, Id(n1), Id(n2)), BinaryOp(%, Id(n3), Id(n4))), BinaryOp(=, Id(n1), BinaryOp(+, BinaryOp(-, BinaryOp(*, Id(n2), NumLit(3.0)), Id(n4)), CallExpr(Id(sin), [Id(n1), BinaryOp(>, Id(n2), Id(n3)), BinaryOp(%, BinaryOp(*, NumLit(701.0), Id(n2)), NumLit(1.0))]))), NumLit(701.0)])), BinaryOp(or, BinaryOp(and, BinaryOp(and, UnaryOp(not, Id(b1)), Id(b2)), UnaryOp(not, Id(b3))), Id(b4))), BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(b1), UnaryOp(not, Id(b4))), Id(b3)), UnaryOp(not, Id(b2)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """
func foo(number a)
begin
    if ((a=1) or (a=0)) return 1
    return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
    number a<- arr[foo(1),foo(3)%3]
    return
end
"""
        expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(arr), [CallExpr(Id(foo), [NumLit(1.0)]), BinaryOp(%, CallExpr(Id(foo), [NumLit(3.0)]), NumLit(3.0))])), Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """
func main()
begin
    number _ <- readNumber()
    number __<- readNumber()
    for _ until _*_ = _+_*_-2*_ by _+_
        if (_) 
            for _ until _/(_*_)%_ < _/(_*_+_) by _/_
                if (_*_<_+_) begin
                end
                elif (__<_) if ((__+_/__ = _%__) and (__*_< -1)) 
                    for _ until _/(_*_)%_ < _/(_*_+_) by _/_ 
                        if (true) break 
                        else continue
                else break
        elif (true) continue
        else break
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(_), NumberType, None, CallExpr(Id(readNumber), [])), VarDecl(Id(__), NumberType, None, CallExpr(Id(readNumber), [])), For(Id(_), BinaryOp(=, BinaryOp(*, Id(_), Id(_)), BinaryOp(-, BinaryOp(+, Id(_), BinaryOp(*, Id(_), Id(_))), BinaryOp(*, NumLit(2.0), Id(_)))), BinaryOp(+, Id(_), Id(_)), If((Id(_), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BinaryOp(<, BinaryOp(*, Id(_), Id(_)), BinaryOp(+, Id(_), Id(_))), Block([])), [(BinaryOp(<, Id(__), Id(_)), If((BinaryOp(and, BinaryOp(=, BinaryOp(+, Id(__), BinaryOp(/, Id(_), Id(__))), BinaryOp(%, Id(_), Id(__))), BinaryOp(<, BinaryOp(*, Id(__), Id(_)), UnaryOp(-, NumLit(1.0)))), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BooleanLit(True), Break), [], Continue))), [], Break)), (BooleanLit(True), Continue)], Break))), [], None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """
func main() 
begin
    dynamic a
    a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x!=y)
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, None), AssignStmt(Id(a), BinaryOp(..., BinaryOp(<=, BinaryOp(and, BinaryOp(or, Id(A), Id(B)), BinaryOp(+, Id(C), BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), NumLit(2.0)), NumLit(4.0)), NumLit(3.0)))), UnaryOp(not, BinaryOp(+, UnaryOp(-, NumLit(1.0)), CallExpr(Id(foo), [BinaryOp(+, Id(x), BinaryOp(*, Id(y), BinaryOp(-, Id(z), NumLit(1.0))))])))), BinaryOp(!=, Id(x), Id(y))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_350(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 350))
        #except:
            #print(f"fail test case: 50. This test case is: ## assignment check ")
    def test_351(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a <- [1,2,3]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 351))
        #except:
            #print(f"fail test case: 51. This test case is: ## assignment check ")
    def test_352(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,true,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), BooleanLit(True), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 352))
        #except:
            #print(f"fail test case: 52. This test case is: ## assignment check ")
    def test_353(self):
        input = """##declaration check 
number a<-2
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 353))
        #except:
            #print(f"fail test case: 53. This test case is: ##declaration check ")
    def test_354(self):
        input = """##declaration check 
string a
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, None)])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 354))
        #except:
            #print(f"fail test case: 54. This test case is: ##declaration check ")
    def test_355(self):
        input = """##declaration check 
string a<-2
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 355))
        #except:
            #print(f"fail test case: 55. This test case is: ##declaration check ")
    def test_356(self):
        input = """##declaration check 
bool a<-2
"""
        expect = '''Program([VarDecl(Id(a), BoolType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 356))
        #except:
            #print(f"fail test case: 56. This test case is: ##declaration check ")
    def test_357(self):
        input = """##declaration check 
var a<-2
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 357))
        #except:
            #print(f"fail test case: 57. This test case is: ##declaration check ")
    def test_358(self):
        input = """##declaration check 
dynamic a
"""
        expect = '''Program([VarDecl(Id(a), None, dynamic, None)])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 358))
        #except:
            #print(f"fail test case: 58. This test case is: ##declaration check ")
    def test_359(self):
        input = """## array is a expression too
func main()
begin
number b<-1
var a<- --------[1,2]*----------------b
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, ArrayLit(NumLit(1.0), NumLit(2.0)))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 359))
        #except:
            #print(f"fail test case: 59. This test case is: ## array is a expression too")
    def test_360(self):
        input = """## a lot of minus 
func main()
begin
number b<-1
var a<- --------1*----------------b
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 360))
        #except:
            #print(f"fail test case: 60. This test case is: ## a lot of minus ")
    def test_361(self):
        input = """## only function call
func main() begin 
doNoThing()
hello("TheHieu")
test_3(h[14,2])
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([CallStmt(Id(doNoThing), []), CallStmt(Id(hello), [StringLit(TheHieu)]), CallStmt(Id(test_3), [ArrayCell(Id(h), [NumLit(14.0), NumLit(2.0)])])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 361))
        #except:
            #print(f"fail test case: 61. This test case is: ## only function call")
    def test_362(self):
        input = """## check numlit 
var a<- 1.e91
number b<- -3.255e-4
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(1e+91)), VarDecl(Id(b), NumberType, None, UnaryOp(-, NumLit(0.0003255)))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 362))
        #except:
            #print(f"fail test case: 62. This test case is: ## check numlit ")
    def test_363(self):
        input = """## this code with alot of newline


func main()


begin 
if (a=2) 



a<-2


end 

"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(2.0)), AssignStmt(Id(a), NumLit(2.0))), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 363))
        #except:
            #print(f"fail test case: 63. This test case is: ## this code with alot of newline")
    def test_364(self):
        input = """## if if else else 
func main() begin 
bool a<-true 
bool b<-false 
if (not a) 
    if (b) writeString("b is correct")
    else writeString("b is not correct")
else writeString("a is correct")
return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), VarDecl(Id(b), BoolType, None, BooleanLit(False)), If((UnaryOp(not, Id(a)), If((Id(b), CallStmt(Id(writeString), [StringLit(b is correct)])), [], CallStmt(Id(writeString), [StringLit(b is not correct)]))), [], CallStmt(Id(writeString), [StringLit(a is correct)])), Return()]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 364))
        #except:
            #print(f"fail test case: 64. This test case is: ## if if else else ")
    def test_365(self):
        input = """## if elif if elif elif else 
func main()
begin 
if(1) return 
elif (2) 
    if (3) return 
    elif (4) return 
    elif (5) return 
    else return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Return()), [(NumLit(2.0), If((NumLit(3.0), Return()), [(NumLit(4.0), Return()), (NumLit(5.0), Return())], Return()))], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 365))
        #except:
            #print(f"fail test case: 65. This test case is: ## if elif if elif elif else ")
    def test_366(self):
        input = """##BST with Zcode 
func initTree(number tree[100,3]) begin 
    var i<-0 
    for i until i=100 by 1
        begin 
            tree[i,0] <- -1
            tree[i,1] <- -1
            tree[i,2] <- -1
        end
end

func appendNode(number val,number head,number tree[100,3],bool freeNode[100])
begin 
number node <- 0 
for node until node=100 by 1
    if (freeNode[node]) break 
freeNode[node] <- false 
tree[node,0] <- val 
if (head = -1) return node 
var i <- 0 
number currNode <- 0
for i until i=100 by 1 
begin 
if (tree[node,0] < tree[currNode,0])
    begin 
        if (tree[currNode,1]!=-1) currNode <- tree[currNode,1]
        else tree[currNode,1] <- node 
    end
else begin
    if (tree[currNode,2]!=-1) currNode <- tree[currNode,2]
    else tree[currNode,2] <- node
end
end 
return head
end 

func main() begin 
number tree[100,3]
bool freeNode[100]
number head <- -1
initTree(tree)
var i<-0 
for i until i=100 by 1
    freeNode[i] <- true
i<-0 
for i until i=100 by 1
    begin 
        number val <- readNumber()
        head <- appendNode(val,head,tree, freeNode)
    end
end
"""
        expect = '''Program([FuncDecl(Id(initTree), [VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(0.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(2.0)]), UnaryOp(-, NumLit(1.0)))]))])), FuncDecl(Id(appendNode), [VarDecl(Id(val), NumberType, None, None), VarDecl(Id(head), NumberType, None, None), VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None)], Block([VarDecl(Id(node), NumberType, None, NumLit(0.0)), For(Id(node), BinaryOp(=, Id(node), NumLit(100.0)), NumLit(1.0), If((ArrayCell(Id(freeNode), [Id(node)]), Break), [], None)), AssignStmt(ArrayCell(Id(freeNode), [Id(node)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), Id(val)), If((BinaryOp(=, Id(head), UnaryOp(-, NumLit(1.0))), Return(Id(node))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(currNode), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([If((BinaryOp(<, ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), ArrayCell(Id(tree), [Id(currNode), NumLit(0.0)])), Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), Id(node)))])), [], Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), Id(node)))]))])), Return(Id(head))])), FuncDecl(Id(main), [], Block([VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None), VarDecl(Id(head), NumberType, None, UnaryOp(-, NumLit(1.0))), CallStmt(Id(initTree), [Id(tree)]), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(freeNode), [Id(i)]), BooleanLit(True))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([VarDecl(Id(val), NumberType, None, CallExpr(Id(readNumber), [])), AssignStmt(Id(head), CallExpr(Id(appendNode), [Id(val), Id(head), Id(tree), Id(freeNode)]))]))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 366))
        #except:
            #print(f"fail test case: 66. This test case is: ##BST with Zcode ")
    def test_367(self):
        input = """## count the number of digits of a number 
func main() begin 
var num <- readNumber() 
number count <- 1 
number core <- 10 
for core until false by 0
    if (num < core) break
    else core <- 10*core
    count<-count+1
writeNumber(num)
writeString(" has ")
writeNumber(count) 
writeString(" digits.")
end 
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(count), NumberType, None, NumLit(1.0)), VarDecl(Id(core), NumberType, None, NumLit(10.0)), For(Id(core), BooleanLit(False), NumLit(0.0), If((BinaryOp(<, Id(num), Id(core)), Break), [], AssignStmt(Id(core), BinaryOp(*, NumLit(10.0), Id(core))))), AssignStmt(Id(count), BinaryOp(+, Id(count), NumLit(1.0))), CallStmt(Id(writeNumber), [Id(num)]), CallStmt(Id(writeString), [StringLit( has )]), CallStmt(Id(writeNumber), [Id(count)]), CallStmt(Id(writeString), [StringLit( digits.)])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 367))
        #except:
            #print(f"fail test case: 67. This test case is: ## count the number of digits of a number ")
    def test_368(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) number a[3,2] <- [[1,2],[3,4],[5,6]]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 368))
        #except:
            #print(f"fail test case: 68. This test case is: ##declare in statement without block")
    def test_369(self):
        input = """##declare in statement without block
func main() 
begin 
    for i until i!=0 by 1 dynamic i
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(!=, Id(i), NumLit(0.0)), NumLit(1.0), VarDecl(Id(i), None, dynamic, None))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 369))
        #except:
            #print(f"fail test case: 69. This test case is: ##declare in statement without block")
    def test_370(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) string s <- "kkk"
    elif (2) string s <- "TheHieu"
    else bool b <- false
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(s), StringType, None, StringLit(kkk))), [(NumLit(2.0), VarDecl(Id(s), StringType, None, StringLit(TheHieu)))], VarDecl(Id(b), BoolType, None, BooleanLit(False)))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 370))
        #except:
            #print(f"fail test case: 70. This test case is: ##declare in statement without block")
    def test_371(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) string a[3,2] <- [[1,2],[3,4],[5,6]]
    else number b[4,4,4]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], StringType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], VarDecl(Id(b), ArrayType([4.0, 4.0, 4.0], NumberType), None, None))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 371))
        #except:
            #print(f"fail test case: 71. This test case is: ##declare in statement without block")
    def test_372(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if(var_) for_<-1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), If((Id(var_), AssignStmt(Id(for_), NumLit(1.0))), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 372))
        #except:
            #print(f"fail test case: 72. This test case is: ## use identifier nearly the same with key words")
    def test_373(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if_ (var_)
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if_), [Id(var_)])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 373))
        #except:
            #print(f"fail test case: 73. This test case is: ## use identifier nearly the same with key words")
    def test_374(self):
        input = """## string using ## 
func main()
begin 
    string s<-"this test case is to check if it is work normally if ## in the string"
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(s), StringType, None, StringLit(this test case is to check if it is work normally if ## in the string))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 374))
        #except:
            #print(f"fail test case: 74. This test case is: ## string using ## ")
    def test_375(self):
        input = """## exmaple of block in Zcode specification page 12
func main() begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0)), VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), ArrayType([5.0], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 375))
        #except:
            #print(f"fail test case: 75. This test case is: ## exmaple of block in Zcode specification page 12")
    def test_376(self):
        input = """## test_3 in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591
func main() begin
if (1)
	if (2)
		b()
	elif (3)
		if (4)
			c()
		elif (5)
			d()
		else e()
	elif(6)
		f()
	else g()
elif (7) h()
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), CallStmt(Id(b), [])), [(NumLit(3.0), If((NumLit(4.0), CallStmt(Id(c), [])), [(NumLit(5.0), CallStmt(Id(d), []))], CallStmt(Id(e), []))), (NumLit(6.0), CallStmt(Id(f), []))], CallStmt(Id(g), []))), [(NumLit(7.0), CallStmt(Id(h), []))], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 376))
        #except:
            #print(f"fail test case: 76. This test case is: ## test_3 in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591")
    def test_377(self):
        input = """## test_3 in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591
func main() begin
var i<-0 
if (1) 
	for i until i=10 by 1
		if (2) return
		elif (3) return
		else  return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), If((NumLit(1.0), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), If((NumLit(2.0), Return()), [(NumLit(3.0), Return())], Return()))), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 377))
        #except:
            #print(f"fail test case: 77. This test case is: ## test_3 in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591")
    def test_378(self):
        input = r"""## check nested if with for loop
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("g") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("b")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true and true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
end
"""
        expect = r'''Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(g)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(b)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BinaryOp(and, BooleanLit(True), BooleanLit(True)), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [], None))], None)), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 378))
        #except:
            #print(f"fail test case: 78. This test case is: ## check nested if with for loop")
    def test_379(self):
        input = r"""## print function 
func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\n"
    writeString(output)
end
"""
        expect = r'''Program([FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None)], Block([AssignStmt(Id(output), StringLit(Move 1 disk from tower )), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(src))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit( to tower ))), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(des))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit(\n))), CallStmt(Id(writeString), [Id(output)])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 379))
        #except:
            #print(f"fail test case: 79. This test case is: ## print function ")
    def test_380(self):
        input = """## only function call
func main() begin 
doNoThing()
hello("HelloTheHieu")
test_3(h[14,2])
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([CallStmt(Id(doNoThing), []), CallStmt(Id(hello), [StringLit(HelloTheHieu)]), CallStmt(Id(test_3), [ArrayCell(Id(h), [NumLit(14.0), NumLit(2.0)])])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 380))
        #except:
            #print(f"fail test case: 80. This test case is: ## only function call")
    def test_381(self):
        input = """## expresion in array lit 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)+3
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(4)*foo(foo(3))]]
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(+, BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])), NumLit(3.0)))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [NumLit(4.0)])), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])])))))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 381))
        #except:
            #print(f"fail test case: 81. This test case is: ## expresion in array lit ")
    def test_382(self):
        input = """## hello world
var str <- "Hello world!"
"""
        expect = '''Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 382))
        #except:
            #print(f"fail test case: 82. This test case is: ## hello world")
    def test_383(self):
        input = """##single declaration
number a 
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, None)])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 383))
        #except:
            #print(f"fail test case: 83. This test case is: ##single declaration")
    def test_384(self):
        input = """## array declaration check
func foo(number a) return a+1
number a[2,3] <- [[1+2,3,"abc",foo(4)],[true,false,true]]
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0), StringLit(abc), CallExpr(Id(foo), [NumLit(4.0)])), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True))))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 384))
        #except:
            #print(f"fail test case: 84. This test case is: ## array declaration check")
    def test_385(self):
        input = """ ##mergesort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
"""
        expect = '''Program([FuncDecl(Id(merge), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(mid), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(k), NumberType, None, None), VarDecl(Id(n1), NumberType, None, BinaryOp(+, BinaryOp(-, Id(mid), Id(left)), NumLit(1.0))), VarDecl(Id(n2), NumberType, None, BinaryOp(-, Id(right), Id(mid))), VarDecl(Id(L), ArrayType([100.0], NumberType), None, None), VarDecl(Id(R), ArrayType([100.0], NumberType), None, None), For(Id(i), BinaryOp(<, Id(i), Id(n1)), NumLit(1.0), AssignStmt(ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(left), Id(i))]))), For(Id(j), BinaryOp(<, Id(j), Id(n2)), NumLit(1.0), AssignStmt(ArrayCell(Id(R), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, BinaryOp(+, Id(mid), NumLit(1.0)), Id(j))]))), AssignStmt(Id(i), NumLit(0.0)), AssignStmt(Id(j), NumLit(0.0)), AssignStmt(Id(k), Id(left)), For(Id(k), BinaryOp(<=, Id(k), Id(right)), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(and, BinaryOp(<, Id(i), Id(n1)), BinaryOp(>=, Id(j), Id(n2))), BinaryOp(<=, ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(R), [Id(j)]))), Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(L), [Id(i)])), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(R), [Id(j)])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0)))]))]))])), FuncDecl(Id(mergeSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(<, Id(left), Id(right)), Block([VarDecl(Id(mid), NumberType, None, BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))), CallStmt(Id(mergeSort), [Id(arr), Id(left), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(right)]), CallStmt(Id(merge), [Id(arr), Id(left), Id(mid), Id(right)])])), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 385))
        #except:
            #print(f"fail test case: 85. This test case is: ##mergesort with zcode")
    def test_386(self):
        input = """##if else check
func main()
begin
bool a<-true
if (a) b<-a+1
else if (not a) b<-a+2
else b<-a+3
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), If((Id(a), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(1.0)))), [], If((UnaryOp(not, Id(a)), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(2.0)))), [], AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(3.0)))))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 386))
        #except:
            #print(f"fail test case: 86. This test case is: ##if else check")
    def test_387(self):
        input = """##if else check 
func main() begin 
number today <- getToday()
number day <- getDay()
if (today=2) writeString("Hom nay phai di hoc")
elif (today = 3) 
if (day=1) writeString("hom nay duoc nghi hoc")
elif (day=25) writeString("hom nay lam kiem tra")
else writeString("hom nay di hoc bth")
elif (today=4) writeString("Hom nay di hoc buoi sang")
else writeString("Hom nay duoc nghi hoc")
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(today), NumberType, None, CallExpr(Id(getToday), [])), VarDecl(Id(day), NumberType, None, CallExpr(Id(getDay), [])), If((BinaryOp(=, Id(today), NumLit(2.0)), CallStmt(Id(writeString), [StringLit(Hom nay phai di hoc)])), [(BinaryOp(=, Id(today), NumLit(3.0)), If((BinaryOp(=, Id(day), NumLit(1.0)), CallStmt(Id(writeString), [StringLit(hom nay duoc nghi hoc)])), [(BinaryOp(=, Id(day), NumLit(25.0)), CallStmt(Id(writeString), [StringLit(hom nay lam kiem tra)]))], CallStmt(Id(writeString), [StringLit(hom nay di hoc bth)]))), (BinaryOp(=, Id(today), NumLit(4.0)), CallStmt(Id(writeString), [StringLit(Hom nay di hoc buoi sang)]))], CallStmt(Id(writeString), [StringLit(Hom nay duoc nghi hoc)]))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 387))
        #except:
            #print(f"fail test case: 87. This test case is: ##if else check ")
    def test_388(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for1 
    var var1  <- for_ 
    if(var_) for_<-1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for1), None, dynamic, None), VarDecl(Id(var1), None, var, Id(for_)), If((Id(var_), AssignStmt(Id(for_), NumLit(1.0))), [], None)]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 388))
        #except:
            #print(f"fail test case: 88. This test case is: ## use identifier nearly the same with key words")
    def test_389(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if__(var_)
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if__), [Id(var_)])]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 389))
        #except:
            #print(f"fail test case: 89. This test case is: ## use identifier nearly the same with key words")
    def test_390(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 390))
        #except:
            #print(f"fail test case: 90. This test case is: ## assignment check ")
    def test_391(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a <- [1,2,3]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 391))
        #except:
            #print(f"fail test case: 91. This test case is: ## assignment check ")
    def test_392(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,true,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), BooleanLit(True), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 392))
        #except:
            #print(f"fail test case: 92. This test case is: ## assignment check ")
    def test_393(self):
        input = """##declaration check 
number a<-2
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 393))
        #except:
            #print(f"fail test case: 93. This test case is: ##declaration check ")
    def test_394(self):
        input = """##declaration check 
string a
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, None)])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 394))
        #except:
            #print(f"fail test case: 94. This test case is: ##declaration check ")
    def test_395(self):
        input = """##declaration check 
string a<-2
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 395))
        #except:
            #print(f"fail test case: 95. This test case is: ##declaration check ")
    def test_396(self):
        input = """##declaration check 
bool a<-2
"""
        expect = '''Program([VarDecl(Id(a), BoolType, None, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 396))
        #except:
            #print(f"fail test case: 96. This test case is: ##declaration check ")
    def test_397(self):
        input = """##declaration check 
var a<-2
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(2.0))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 397))
        #except:
            #print(f"fail test case: 97. This test case is: ##declaration check ")
    def test_398(self):
        input = """##declaration check 
dynamic a
"""
        expect = '''Program([VarDecl(Id(a), None, dynamic, None)])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 398))
        #except:
            #print(f"fail test case: 98. This test case is: ##declaration check ")
    def test_399(self):
        input = """##if in for
func main() begin
    number i<-0 
    for i until i>0 by 1
        if (1) 
            for i until i<0 by 1
                if (2) continue
                else break
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), NumLit(0.0)), NumLit(1.0), If((NumLit(1.0), For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), NumLit(1.0), If((NumLit(2.0), Continue), [], Break))), [], None))]))])'''
        #try:
        self.assertTrue(TestAST.test(input, expect, 399))
        #except:
            #print(f"fail test case: 99. This test case is: ##if in for")