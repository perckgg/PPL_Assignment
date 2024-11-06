import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase): 

    def test_201(self):
        input = """
func main()
begin
    dynamic arr[0, 0, 0] <- "abc" or false
end
"""
        expect = "Error on line 4 col 15: ["
        self.assertTrue(TestParser.test(input,expect,201))


    def test_202(self):
        input = """func isPrime(number x) 
        func main()
begin
    number a <- 12
    number x <- readNumber()
    if (isPrime(x)) printString("Yes") 
    else printString("No")

end
func isPrime(number x)
    begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
    return true
    end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))


    def test_203(self):
        input = """## this is a comment
## ## is also contained in comment






## this is a comment




func main()      begin
    number a
    var a <- 12
    var b <- \"something you must check \'\" \\r \\n \\t \\f \\b \\\'\'\"\"
    dynamic cajfs____90928__
    string ___________
    number b[1, 2, 3, 0] <- [[123], 3, 4, [21324, [2123, 2, 1], [1, 2]]]
    return 0
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))


    def test_204(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))


    def test_205(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))


    def test_206(self):
        input = """
func test_expr()
begin
    string a <- "hello world"
    string c <- "!"
    string d <- "!"
    return a ... c ... d
end
"""
        expect = "Error on line 7 col 19: ..."
        self.assertTrue(TestParser.test(input,expect,206))


    def test_207(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))


    def test_208(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))


    def test_209(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))


    def test_210(self):
        input = """
func foo()


## this is a comment


## this is a comment


goo()
"""
        expect = "Error on line 11 col 0: goo"
        self.assertTrue(TestParser.test(input,expect,210))


    def test_211(self):
        input = """
## this is test for simple predefine function
func main(bool a_a_a[2, 0]) number a
"""
        expect = "Error on line 3 col 28: number"
        self.assertTrue(TestParser.test(input,expect,211))


    def test_212(self):
        input = """func main(number a, number b) begin
number a[1, 2] <- [[2, 3]]
string b <- 1.e-12
bool c <- "abc"
return main(a, 3, d, b)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))


    def test_213(self):
        input = """
func test_exp()
begin
    bool a <- not not not goo() not a not c not d not love
    return a
end
"""
        expect = "Error on line 4 col 32: not"
        self.assertTrue(TestParser.test(input,expect,213))


    def test_214(self):
        input = """
func test_exp()
begin
    bool a <- not not a and b or not not c or d or e and b < not not not c and d or e or not not e
    return a
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))


    def test_215(self):
        input = """
func test_exp()
begin
    bool a <- a <= (b = ((k > (h == (b < c))) < (d > (e == f))))
    return a
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))


    def test_216(self):
        input = """
func test_exp()
begin
    number a <- a[1, [1, 2]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))


    def test_217(self):
        input = """
func test_exp()
begin
    number a <- b[]
    return a
end
"""
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestParser.test(input,expect,217))


    def test_218(self):
        input = """
func test_exp()
begin
    number a[3] <- [1, 2, 3]
    number b[3] <- [2, 3, 4]
    number c[2] <- [a, b]
    number d <- c[0][0]
end
"""
        expect = "Error on line 7 col 20: ["
        self.assertTrue(TestParser.test(input,expect,218))


    def test_219(self):
        input = """
func test_exp()
begin
    number a <- c[1, d[1, 2, 3, foo()[1, 2]], goo() + 1 * 3 / b, h[1, 1]]
    return a
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))


    def test_220(self):
        input = """
func test_exp()
begin
    number a <- [1, [1], [[1]], [[[1]]], [[[[1]]]]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))


    def test_221(self):
        input = """
func test_exp()
begin
    bool a <- b < c < d
end
"""
        expect = "Error on line 4 col 20: <"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_222(self):
        input = """
func test_exp()
begin
    number a[foo(), 1, b] <- [1, 2, 3]
end
"""
        expect = "Error on line 4 col 13: foo"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_223(self):
        input ="""number a["5"]
"""
        expect = "Error on line 1 col 9: 5"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_224(self):
        input = """
func foo123478_main_09()
begin
    number a <- [1, 2, [1, 2, [1, 4]], [3, 4]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_225(self):
        input = """
func main()
begin
    a <- "abc"
    number b <- 1 * 2 - 3 % 5
    begin
        string c <- "'"
        begin
            string c <- "'""
        end
        begin
            string c <- "\\\\"
        end
    end
    return 23 > 43
end
"""
        expect = "'\""
        self.assertTrue(TestParser.test(input,expect,225))

    def test_226(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_227(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_228(self):
        input = """
func unaryDestroyer()
begin
    a <- not not not---not-not-not not-not not not-not not not not----not-----not not---not not not--foo()[0]
end
"""
        expect = "Error on line 4 col 23: not"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_229(self):
        input = """
func arrayDestroyer()
begin
    number a <- [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[foo()[1, 2, 3]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_230(self):
        input = """
func unaryDestroyer()
begin
    a <- not not not---(not-(not-(not not-(not not not-(not not not not----(not-----(not not---(not not not--(foo()[0])))))))))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_231(self):
        input = """
func main()
begin
    number x <- [foo(), foo()[1, 2, 3], x[0, 1], 12 > 3]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_232(self):
        input = """
func main(number a, string s, bool _, number xxx[1, 2, 3])
begin
    do_something(a, s, _, xxx)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_233(self):
        input = """
func main(number a, string s, number foo()[1, 2])
begin
    print("Not allowed in parameter list")
end
"""
        expect = "Error on line 2 col 40: ("
        self.assertTrue(TestParser.test(input,expect,233))

    def test_234(self):
        input = """
func main(number a, string s, number arr[2 * 3])
begin
    print("Allowed in parameter list")
end
"""
        expect = "Error on line 2 col 43: *"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_235(self):
        input = """
func main(number a, string s, number arr[])
begin
    print("Not allowed in parameter list")
end
"""
        expect = "Error on line 2 col 41: ]"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_236(self):
        input = """
func main(123, "abc", [1, 2, 3])
begin
    print("Not allowed in parameter list")
end
"""
        expect = "Error on line 2 col 10: 123"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_237(self):
        input = """
func main(number arr[1][2][3])
begin
    print("Not allowed in parameter list")
end
"""
        expect = "Error on line 2 col 23: ["
        self.assertTrue(TestParser.test(input,expect,237))

    def test_238(self):
        input = """
func _______()
begin
    number a <- 00012789.10002992017e-179423
    string s <- ""
    foo()[12] <- a
    return foo()[12]
end
"""
        expect = "Error on line 6 col 9: ["
        self.assertTrue(TestParser.test(input,expect,238))

    def test_239(self):
        input = """
func ______abc_____()
begin
    bool b <- false
    number foo() <- [1, 2, 3]
    return foo()
end
"""
        expect = "Error on line 5 col 14: ("
        self.assertTrue(TestParser.test(input,expect,239))

    def test_240(self):
        input = """
func __self__()
begin
    string abc <- "43817807890982835"
    number a <- --00192878.20018273e-18253
    number arr <- [[], []]
end
"""
        expect = "Error on line 6 col 20: ]"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_241(self):
        input = """
func __aaa__()
begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a" ... "b", foo()["index"]], [(a and not c) = d]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_242(self):
        input = """
func __bbb__()
begin
    number arr[] <- [[1], [1]]
end
"""
        expect = "Error on line 4 col 15: ]"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_243(self):
        input = """
func __ccc__()
begin
    number arr[-2, "a", true, false, a not c] <- [1, 2, 3]
end
"""
        expect = "Error on line 4 col 15: -"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_244(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_245(self):
        input = """## This is a comment
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_246(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_247(self):
        input = """
func main()
begin
    number i, j, k
    ## Not allowed in declaration
end
"""
        expect = "Error on line 4 col 12: ,"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_248(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_249(self):
        input = """
func test()
begin
    string s <- "abc'"
end
"""
        expect = "abc'\""
        self.assertTrue(TestParser.test(input,expect,249))

    def test_250(self):
        input = """
func test()
begin
    string s <- "abc''\\''"
end
"""
        expect = "abc''\\''\""
        self.assertTrue(TestParser.test(input,expect,250))

    def test_251(self):
        input = """
func test()
begin
    string s <- "abc'''''''\\'"
    string s <- "abc"
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_252(self):
        input = """
func test()
begin
    string s <- "abc\\i"
    string s <- "abc"
end
"""
        expect = "abc\\i"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_253(self):
        input = """
func test()
begin
    string s <- "abc
    string s <- "abc"
end
"""
        expect = "abc"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_254(self):
        input = """
func test()
begin
    number arr <- [[1, 2, 3], foo()[23], a > b, "a" ... "c", foo() ... goo(), []]
end
"""
        expect = "Error on line 4 col 79: ]"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_255(self):
        input = """
func main()
begin
    number option
    cin >> option
    if (option = 1) cout << "Hello world"
    elif (option = 2)
    begin
        string name
        cin >> name
        cout << "Hello " << name
    end
    else
    begin
        string name
        number age
        cin >> name >> age
        cout << "Hello " << age << " years old " << name
    end
end
"""
        expect = "Error on line 5 col 8: >"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_256(self):
        input = """
func recursion(number i, number n)
begin
    if (i = n) return n
    else return recursion(i + 1, n) + i
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_257(self):
        input = """
func buildHouse()
begin
    number width <- readNumber()
    number length <- readNumber()
    number budget <- readNumber()
    print("Starting building house")
    print("Creating strong base")
    print("Buying brick, cement and hiring labours")
    print("Working on materials")
    print("Completing the house, cleaning dirt")
    print("Decorating the house")
    print("Having fun with new house")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_258(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_259(self):
        input = """func main()
begin
           if (a) do(a)
           elif (a=2=2) do(b)
end
"""
        expect = "Error on line 4 col 20: ="
        self.assertTrue(TestParser.test(input,expect,259))

    def test_260(self):
        input = """
func main(var a[12])
begin
end
"""
        expect = "Error on line 2 col 10: var"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_261(self):
        input = """
func main(dynamic a[12])
begin
end
"""
        expect = "Error on line 2 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_262(self):
        input = """
func main()
begin
    var arr <- [1, 2, 3]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_263(self):
        input = """
func main()
begin
    dynamic arr <- [1, 2, 3]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_264(self):
        input = """
        ## test
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_265(self):
        input = """
func main()
begin
    dynamic arr
    dynamic arr <- "abc"
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_266(self):
        input = """
func main()
begin
    2[0, 0] <- "abc"
    return 2[0, 0]
end
"""
        expect = "Error on line 4 col 4: 2"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_267(self):
        input = """
func main()
begin
    a[0, 0] <- "abc"[34] + 2[0, 0]
end
"""
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input,expect,267))

    def test_268(self):
        input = """
func main()
begin
    number arr[0, 0] <- [foo()[12], "abc", 2[0, 0]]
end
"""
        expect = "Error on line 4 col 44: ["
        self.assertTrue(TestParser.test(input,expect,268))

    def test_269(self):
        input = """
func main()
begin
    number arr[0, 0] <- 123
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_270(self):
        input = """
func main()
begin
    var arr[0, 0] <- [1, 2, 3, 4]
end
"""
        expect = "Error on line 4 col 11: ["
        self.assertTrue(TestParser.test(input,expect,270))

    def test_271(self):
        input = """
func main()
begin
    dynamic arr[0, 0] <- [1, 2, 3, 4]
end
"""
        expect = "Error on line 4 col 15: ["
        self.assertTrue(TestParser.test(input,expect,271))

    def test_272(self):
        input = """
func main()
begin
end"""
        expect = "Error on line 4 col 3: <EOF>"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_273(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_274(self):
        input="""## If statement error testing
func main()
    begin
    if (a[1])
    a == b
    else b <- a
end
        """
        expect = "Error on line 5 col 6: =="
        self.assertTrue(TestParser.test(input,expect,274))

    def test_275(self):
        input="""## If statement error testing
func main()
    begin
    if (x ... y)
    a <- b
    else b <- a
    else a <- b
end
        """
        expect = "Error on line 7 col 4: else"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_276(self):
        input="""## If statement testing
func main()
begin
    if ((5 < a) and (b < 10))
        a <- b
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_277(self):
        input="""## If statement testing
func main()
begin
    if (a > b)
    
    a <- b
    elif (a < b)
    b <- a
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_278(self):
        input="""## Block Statement testing
func main()
    begin
    end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_279(self):
        input="""## Block Statement testing
func main()
begin


    var a <- 1
    var b <- 2
    var c <- a + b
    return c
end
    
    
    
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_280(self):
        input="""## Block Statement error testing
func main()
begin var a <- 1
    var b <- 2
    var c <- a + b
    return c
end
"""
        expect = "Error on line 3 col 6: var"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_281(self):
        input="""## Function call statement testing
        func main()
    return updateVer()
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_282 (self):
        input="""## Function call statement testing
func main()
    return printString("Hello World")
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_283(self):
        input="""## Function call statement testing error
func main()
    return printString(a b)
"""
        expect = "Error on line 3 col 25: b"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_284(self):
        input="""## Return statement testing
func main()
    return isPrime(x)
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_285(self):
        input="""## Return statement testing
func main()
    return
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_286(self):
        input="""## assignment error checking
func main( )
begin
    number arr <- [1,2,3,4,5]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_287(self):
        input="""## assignment error checking
func main()
begin
    var a <- [1,2,3,4,5][4]
end
"""
        expect = "Error on line 4 col 24: ["
        self.assertTrue(TestParser.test(input,expect,287))

    def test_288(self):
        input = """func main()
return (a > b) or (b > a)
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_289(self):
        input = """func main() begin
a[5] <- [1,2,3,4,5]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
   
    def test_290(self):
        input = """func main()


begin
    if (a < b)  a <- b
    elif (a > b) b <- a
    elif (a = b) a <- b
    else a <- b
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
   
    def test_291(self):
        input = """func main()


begin
var i <- 0
for i until i > 10 by 1


        print(i)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
   
    def test_292(self):
        input = """func main()
begin
    var i <- 0
    for i until i > 10 by 1
    begin
        print(i)
        if (i = 5) break
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
   
    def test_293(self):
        input = """func main()
begin
    var i <- 0
    for i until i > 10 by 1
    begin
        if (i = 5) continue
        print(i)
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
   
    def test_294(self):
        input ="""number a["5"]
"""
        expect = "Error on line 1 col 9: 5"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_295(self):
        input ="""number a[5] b[5]
"""
        expect = "Error on line 1 col 12: b"
        self.assertTrue(TestParser.test(input,expect,295))    

    def test_296(self):
        input = """dynamic a[8]
"""
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input,expect,297))
       
    def test_297(self):
        input = """number a[3 + 2] <- [1, 2, 3, 4, 5]
"""
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.test(input,expect,297))
   
    def test_298(self):
        input = """
func main(dynamic a, var c)
begin
end
"""
        expect = "Error on line 2 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,298))
   
    def test_299(self):
        input = """number a[5] <- [a * a, 2 + 8, 900 % 7, (3 + 8) / 3 * 9, true]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    
    def test_300(self):
        input = """func main()
        begin
        string c <- "\\mmmp"
        end
        """
        expect = '\m'
        self.assertTrue(TestParser.test(input,expect,300))
    
    def test_302(self):
        input = """
func main()
begin
    number arr[1] <- number a
end
"""
        expect = "Error on line 4 col 21: number"
        self.assertTrue(TestParser.test(input,expect, 302))
