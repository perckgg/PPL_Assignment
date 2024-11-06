

import unittest
from TestUtils import TestChecker

class CheckSuite(unittest.TestCase):
        def test401(self):
            input = """
    func f()
    begin
        dynamic x
        x <- [[1, 2, 3], [4, 5, 6]]
        return x[0, 0]
    end

    func main()
    begin
        number x <- f()
    end

    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 401))
        
        def test402(self):
            input = """
    func f(number x)
    func f(number x)
    begin
        if (x >= 2) return f(x - 1) + f(x - 2)
        return 1
    end
    func main()
    begin
        number x <- f(2)
        writeNumber(x)
    end


    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 402))
        
        def test403(self):
            input = """
    func main()
    begin
        var x <- [[1, 2, 3], [4, 5, 6]]
        var y <- x[0, 0] + 1
        writeBool(y)
    end

    """
            expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
            self.assertTrue(TestChecker.test(input, expect, 403))
        
        def test404(self):
            input = """
    dynamic x

    func main()
    begin
        var y <- x[0, 0] + 1
        writeNumber(y)
    
    end

    """
            expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
            self.assertTrue(TestChecker.test(input, expect, 404))
        
        def test405(self):
            input = """
    dynamic x
    func main()
    begin
        x <- [1, 2, 3, 4, 5, 6]
        var y <- x[0, 0] + 1
        writeNumber(y)
    end

    """
            expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
            self.assertTrue(TestChecker.test(input, expect, 405))
        
        def test406(self):
            input = """
    dynamic x <- f(2)
    func f(number x)

    func main()
    begin

    end
    """
            expect = "Undeclared Function: f"
            self.assertTrue(TestChecker.test(input, expect, 406))
        
        def test407(self):
            input = """
    func f(number x)

    dynamic x <- f(2) + 1

    func f(number y)
    begin
        if (y <= 1) return 1
        return y * f(y - 1)
    end

    func main()
    begin
        return 2
    end
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 407))
        
        def test408(self):
            input = """
    func f(number x)

    dynamic x <- f(2) + 1

    func main()
    begin
        return
    end
    """
            expect = "No Function Definition: f"
            self.assertTrue(TestChecker.test(input, expect, 408))
        
        def test409(self):
            input = """
    func f(number x[2, 3])
        return x[2]

    func main()
    begin
        number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        writeNumber(f()[2])
    end
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
            self.assertTrue(TestChecker.test(input, expect, 409))
        
        def test410(self):
            input = """
    func f(number x[2, 3])
        return x

    func main()
    begin
        number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        writeNumber(f(x)[0, 1])
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 410))
        
        def test411(self):
            input = """
    func f(number x[2, 3])
        return x

    func main()
    begin
        dynamic x <- [[1, 2, 3], [4, 5, 6]]
        var y <- x[0, 0]
        writeString(y)
    end
    """
            expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
            self.assertTrue(TestChecker.test(input, expect, 411))
        
        def test412(self):
            input = """
    func f(number x[2, 3], number i, number j)
        return x[i, j]

    func main()
    begin
        dynamic x <- [[1, 2, 3], [4, 5, 6]]
        var i <- 0
        for i until i >= 2 by 1
            for j until j >= 3 by 1
                writeNumber(f(x, i, j))
    end
    """
            expect = "Undeclared Identifier: j"
            self.assertTrue(TestChecker.test(input, expect, 412))
        
        def test413(self):
            input = """
    func main()
    begin
        number x <- readNumber()
        if (x <= 10) writeString("Number is less than or equal to 10")
        elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
        else writeString("Invalid number!")
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 413))
        
        def test414(self):
            input = """
    func isPrime(number x)

    func main()
    begin
        number x <- readNumber()
        if (isPrime(x)) writeString("x is a prime number")
        else writeString("x is not a prime number")
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
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 414))
        
        def test415(self):
            input = """
    func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))

    func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 415))
        
        def test416(self):
            input = """
    func f()
    begin
        var i <- 0
        for i until i > 10 by 1
        begin

        end
        continue
    end

    func main()
    begin
        f()
    end
    """
            expect = "Continue Not In Loop"
            self.assertTrue(TestChecker.test(input, expect, 416))
        
        def test417(self):
            input = """
    func findMax(number x[10], number n)
    begin
        if (n = 1) return x[0]
        number k <- findMax(x, n - 1)
        if (k >= x[n]) return k
        return x[n]
    end

    func main()
    begin
        dynamic x <- [3, 4, 0, 1, 2, 7, 9, 8, 5, 6]
        writeNumber(findMax(x, 10))
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 417))
        
        def test418(self):
            input = """
    func main()
    begin
        number x <- 2 + true
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
            self.assertTrue(TestChecker.test(input, expect, 418))
        
        def test419(self):
            input = """
    func main()
    begin
        var x <- [ [ [[1, 2]], [3, 4, 5] ], [[6, 7, 8], [9, 10, 11]] ]
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
            self.assertTrue(TestChecker.test(input, expect, 419))
        
        def test420(self):
            input = """
    func foo(number a, string d)
    func foo(number a) return
    func main() return
    """
            expect = "Redeclared Function: foo"
            self.assertTrue(TestChecker.test(input, expect, 420))
        
        def test_421(self):
            input = """number a[5]
    string a[5]
    func main()
    begin
        string b[5]
        number a
    end
            """
            expect = "Redeclared Variable: a"
            self.assertTrue(TestChecker.test(input, expect, 421))

        def test422(self):
            input = """
     func foo(number a, string a)
                func foo(number a, string a) return 
                func main() return
    """
            expect = "Redeclared Parameter: a"
            self.assertTrue(TestChecker.test(input, expect, 422))
        
        def test423(self):
            input = """
    func f(number x)
    begin
        if (x = 0) return 0
        elif (x = 1) return 1
        else return f(x - 1) + f(x - 2)
    end
        
    func main()
    begin
        dynamic a
        number x <- f(a)
        a[0] <- [1, 2, 3]
    end
    """
            expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
            self.assertTrue(TestChecker.test(input, expect, 423))
        
        def test424(self):
            input = """
    func max(number x, number y)
    begin
        if (x <= y) return y
        return x
    end

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        number z <- readNumber()
        writeNumber(max(max(x, y), z))
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 424))
        
        def test425(self):
            input = """
    func pow(number x, number y)

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        writeNumber(pow(x, y))
    end

    func pow(number a, number b)
    begin
        if (b = 0) return 1
        number k <- pow(a, b / 2)
        if (b % 2 = 0) return k * k
        return a * k * k
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 425))
        
        def test426(self):
            input = """
    func add(number x, number x)

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        writeNumber(add(x, y))
    end

    func add(number a, number b)
    begin
        return a + b
    end
    """
            expect = "Redeclared Parameter: x"
            self.assertTrue(TestChecker.test(input, expect, 426))
        
        def test427(self):
            input = """
    func add(number x, number y)

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        writeNumber(pow(x, y))
    end

    func add(number a, number b)
    begin
        return a + b
    end
    """
            expect = "Undeclared Function: pow"
            self.assertTrue(TestChecker.test(input, expect, 427))
        
        def test428(self):
            input = """
    func add(number x, number y)

    func main()
    begin
        var i <- 0
        for i until i > 10 by 0
        begin
            i <- add(i, 1)
            writeNumber(i)
        end
    end

    func add(number a, number b)
    begin
        number x <- a + b
        return x
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 428))
        
        def test429(self):
            input = """
    func f(number x)

    func main()
    begin
        number x <- 10
        number y <- f(x)
        writeNumber(y)
    end

    func f(string x)
    begin
        return x == "Hello"
    end
    """
            expect = "Type Mismatch In Statement: Return(BinaryOp(==, Id(x), StringLit(Hello)))"
            self.assertTrue(TestChecker.test(input, expect, 429))
        
        def test430(self):
            input = """
    func main()
    begin
        var i <- 0
        for i until i < 0 by 1
        begin
            string x <- readString()
            if (x == "Hello") 
            begin
                x <- x ... ", world!"
                writeString(x)
            end
            else writeString("Try again")
        end
        break
    end
    """
            expect = "Break Not In Loop"
            self.assertTrue(TestChecker.test(input, expect, 430))
        
        def test431(self):
            input = """
    func f(number arr[10], number n)
    begin
        var i <- 0
        for i until i >= n by 1
            writeNumber(arr[i])
    end

    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 431))
        
        def test432(self):
            input = """
    func f(number arr[10], number n)
    begin
        var i <- 0
        for i until i >= n by 1
            writeNumber(arr[i])
    end

    func main()
    begin
        dynamic n
        f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
        n <- 10
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 432))
        
        def test433(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        number x[2, 2] <- [a, [b, 2]]
        a <- 2
        b <- 3
        c <- true
    end
    """
            expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
            self.assertTrue(TestChecker.test(input, expect, 433))
        
        def test434(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        number x[3, 2] <- [a, b, [c, 0]]
        a <- [1]
        b <- [3, 4]
        c <- 0
    end
    """
            expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
            self.assertTrue(TestChecker.test(input, expect, 434))
        
        def test435(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        dynamic x <- [readNumber(), a, b, c]
        a <- 3
        b <- x[0]
        c <- a + b
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 435))
        
        def test436(self):
            input = """
    func main()
    begin
        dynamic x <- readBool()
        dynamic y <- not readBool()
        if (x and y) writeNumber(1)
        else writeNumber(0)
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 436))
        
        def test437(self):
            input = """
    func main()
    begin
        dynamic x
        if (x) writeString("x is infer to true value")
        else writeString("x is infer to false value")
        x <- 1 + true
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
            self.assertTrue(TestChecker.test(input, expect, 437))
        
        def test438(self):
            input = """
    func main()
    begin
        dynamic x
        if (x) writeString("x is infer to true value")
        else writeString("x is infer to false value")
        x <- not (true and not false) and not (false and not true)
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 438))
        
        def test439(self):
            input = """
    func f(number x)
    begin
        dynamic x <- (x - 2) * (x + true)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
            self.assertTrue(TestChecker.test(input, expect, 439))
        
        def test440(self):
            input = """
    func f()
    begin
        dynamic x
        x <- (x - 2) * (x + true)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
            self.assertTrue(TestChecker.test(input, expect, 440))
        
        def test441(self):
            input = """
    number a <- 1 + "Hello"
    func main()
        return
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
            self.assertTrue(TestChecker.test(input, expect, 441))
        
        def test442(self):
            input = """
    func f()

    func main()
    begin
        number x <- g(1, 2, 3)
    end
    """
            expect = "Undeclared Function: g"
            self.assertTrue(TestChecker.test(input, expect, 442))
        
        def test443(self):
            input = """
    number x
    number y
    func f()

    func main()
        return
    """
            expect = "No Function Definition: f"
            self.assertTrue(TestChecker.test(input, expect, 443))
        
        def test444(self):
            input = """
    func f()

    number f
    dynamic x
    func main()
        return
    """
            expect = "No Function Definition: f"
            self.assertTrue(TestChecker.test(input, expect, 444))
        
        def test445(self):
            input = """
    func f()
    begin

    end
    dynamic a
    number b
    bool c
    string d
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 445))
        
        def test446(self):
            input = """
    func f()
    begin

    end
    dynamic a
    number b
    bool c
    string d
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 446))
        
        def test447(self):
            input = """
    func f(number x)
    begin
        return 1
    end

    func main()
    begin
        f(2018)
    end
    """
            expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2018.0)])"
            self.assertTrue(TestChecker.test(input, expect, 447))
        
        def test448(self):
            input = """
    func main()
    begin
        continue
    end
    """
            expect = "Continue Not In Loop"
            self.assertTrue(TestChecker.test(input, expect, 448))
        
        def test449(self):
            input = """
    func main()
    begin
        break
    end
    """
            expect = "Break Not In Loop"
            self.assertTrue(TestChecker.test(input, expect, 449))
        
        def test450(self):
            input = """
    number x
    number y
    func add()
        return x + y

    func main()
    begin
        x <- readNumber()
        y <- readNumber()
        writeNumber(add())
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 450))
        
        def test451(self):
            input = """
    func add(number x, number y)

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        dynamic a <- add(x, y) + 1
    end

    func add(number x, number y)
        return "Hello"
    """
            expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
            self.assertTrue(TestChecker.test(input, expect, 451))
        
        def test452(self):
            input = """
    func add(number x, number y)

    func main()
    begin
        dynamic a
        a[0] <- [1, 2, 3]
    end

    func add(number x, number y)
        return "Hello"
    """
            expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
            self.assertTrue(TestChecker.test(input, expect, 452))
        
        def test_453(self):
            input = """func foo(number a[5], string b)
    begin
        number a[5]
        var i <- 0
        for i until i >= 5 by 1
        begin
            a[i] <- i * i + 5
        end
        return -1
    end

    func main()
    begin
        string c
    end
        func foo(number a[5], string b)
            """
            expect = "Redeclared Function: foo"
            self.assertTrue(TestChecker.test(input, expect, 453))
        
        def test454(self):
            input = """
    func f(number arr[10], number x)

    func main()
    begin
        dynamic n
        var i <- 0
        number arr[10]
        for i until true by 1
        begin
            n <- readNumber()
            if ((n > 10) or (n <= 0)) writeString("Try again")
            else break
        end
        
        for i until i >= n by 1
            arr[i] <- readNumber()
        
        f(arr, n)
    end
    """
            expect = "No Function Definition: f"
            self.assertTrue(TestChecker.test(input, expect, 454))
        
        def test455(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        a[2] <- b
    end
    """
            expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), Id(b))"
            self.assertTrue(TestChecker.test(input, expect, 455))
        
        def test456(self):
            input = """
    func foo(number a) return "1"
                func main() 
                begin
                    dynamic x
                    var a <- [[1,2,3], [x,x]]
                end
    """
            expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
            self.assertTrue(TestChecker.test(input, expect, 456))
        
        def test457(self):
            input = """
    func main()
    begin
        dynamic x <- "Hello"
        if (x == "Hello") writeString(x)
        else writeString("Something weird!")
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 457))
        
        def test458(self):
            input = """
    func main()
    begin
        dynamic x <- [1, 2, 3]
        dynamic a <- x
        writeNumber(a[0])
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 458))
        
        def test459(self):
            input = """
    func foo(number a)

    func main()
    begin
        number a <- foo(1)
        return
    end

    func foo(number a)
    begin
        return "std"
    end
    """
            expect = "Type Mismatch In Statement: Return(StringLit(std))"
            self.assertTrue(TestChecker.test(input, expect, 459))
        
        def test460(self):
            input = """
    var f <- 10
    func f()
        return

    func main()
    begin
        dynamic a
        dynamic b
        number c
        dynamic x <- f([a, b, c])
        x <- ["Hello", ", my name is ", "Kien"]
    end
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(f), [ArrayLit(Id(a), Id(b), Id(c))])"
            self.assertTrue(TestChecker.test(input, expect, 460))
        
        def test461(self):
            input = """
    func f(number a[3], number b[3])
        return

    func main()
    begin
        f([1, 3, 2], [1, "Hello", 2])
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
            self.assertTrue(TestChecker.test(input, expect, 461))
        
        
        def test463(self):
            input = """
    number x <- 10
    func f(number x)
    begin
        number x <- x + 20
        writeNumber(x)
    end
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 463))
        
        def test464(self):
            input = """
    func f(number n)

    number a[2, 3] <- [[f(1), f(2), f(3)], [f(4), f(5), f(6)]]
    func main()
    begin
        var i <- 0
        dynamic j <- 0
        for i until i > 1 by 1
            for j until j > 2 by 1
                writeNumber(a[i, j])
    end

    func f(number a)
        return a
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 464))
        
        def test465(self):
            input = """
    func f(number x[2, 3])
        return x[0]

    func main()
    begin
        dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
            self.assertTrue(TestChecker.test(input, expect, 465))
        
        def test466(self):
            input = """
    func f(number n)

    func main()
    begin
        var i <- f(2, 3)
    end

    func f(number a)
        return a
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
            self.assertTrue(TestChecker.test(input, expect, 466))
        
        def test467(self):
            input = """
    func f(number x, number y)

    func main()
    begin
        var i <- f(2)
    end

    func f(number a)
        return a
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
            self.assertTrue(TestChecker.test(input, expect, 467))
        
        def test468(self):
            input = """
    dynamic a
    func main()
    begin
        var i <- a ... 2.75
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
            self.assertTrue(TestChecker.test(input, expect, 468))
        
        def test469(self):
            input = """
    dynamic a
    func main()
    begin
        var i <- a[2] ... 2.75
    end
    """
            expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75)))"
            self.assertTrue(TestChecker.test(input, expect, 469))
        
        def test470(self):
            input = """
    func main()
    begin
        if (1) writeBool(true)
        else writeBool(false)
    end
    """
            expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
            self.assertTrue(TestChecker.test(input, expect, 470))
        
        def test471(self):
            input = """
    func main()

    func main()

    func main()
    begin
        if (1) writeBool(true)
        else writeBool(false)
    end
    """
            expect = "Redeclared Function: main"
            self.assertTrue(TestChecker.test(input, expect, 471))
        
        def test472(self):
            input = """
    number a
    bool b
    string c
    dynamic d
    func main()
    begin
        if (b) d <- 1 + a
        else d <- a - 1.75
        c <- "Hello, world!"
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 472))
        
        def test473(self):
            input = """
    func f(number arr[10], number n)
    begin
        if ((n < 0) or (n >= 10)) return -999
        number i <- 0
        for i until i >= n by 1
            if (arr[i] < 10) return i
        
        return not (n < 20)
    end

    func main()
    begin
        f([1, 9, 6, 5, 3, 8, 10, 28, 0, -10], 10)
    end
    """
            expect = "Type Mismatch In Statement: Return(UnaryOp(not, BinaryOp(<, Id(n), NumLit(20.0))))"
            self.assertTrue(TestChecker.test(input, expect, 473))
        
        def test474(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        var arr <- [[a, 1], [b, true], [c, "Hello"]]
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
            self.assertTrue(TestChecker.test(input, expect, 474))
        
        def test475(self):
            input = """
    dynamic x
    dynamic y
    func main()
    begin
        dynamic z
        dynamic arr 
        arr <- [[1, x], [2, y], [3, z]]
        z <- "Hi"
        x <- 20
        y <- 30

    end
    """
            expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
            self.assertTrue(TestChecker.test(input, expect, 475))
        
        def test476(self):
            input = """
    func main()
    begin
        var x <- [10, 20, 40]
        var y <- [true, false, true]
        number a[2, 3] <- [x, y]
        writeNumber(a[0, 0])
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
            self.assertTrue(TestChecker.test(input, expect, 476))
        
        def test477(self):
            input = """
          func main() 
                begin
                    dynamic x
                    dynamic y
                    for x until y[1] by 1
                        return
                end
    """
            expect = "Type Cannot Be Inferred: For(Id(x), ArrayCell(Id(y), [NumLit(1.0)]), NumLit(1.0), Return())"
            self.assertTrue(TestChecker.test(input, expect, 477))
        
        def test478(self):
            input = """
     func main() 
                begin
                    dynamic x
                    return x[1]
                end
    """
            expect = "Type Cannot Be Inferred: Return(ArrayCell(Id(x), [NumLit(1.0)]))"
            self.assertTrue(TestChecker.test(input, expect, 478))
        
        def test479(self):
            input = """
    func f(number x, bool y, string z)
        return not y

    func main()
    begin
        dynamic x
        dynamic y
        dynamic z
        bool t <- f(x, y, z)
        writeBool(y and not t)
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 479))
        
        def test480(self):
            input = """
    func main()
    begin
        var x <- [[1, 2], [3, 4, 5]]
        writeNumber(x[0, 2])
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
            self.assertTrue(TestChecker.test(input, expect, 480))
        
        def test481(self):
            input = """
    func test(number x)
    begin
        var y <- 1
    end
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 481))
        
        def test482(self):
            input = """
    func test(number x)
    begin
        var a <- x
        var b <- -a
        var c <- a + b
        writeNumber(a + b + c)
    end

    func main()
    begin
        test(2018)
        return -1
    end
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 482))
        
        def test483(self):
            input = """
    dynamic a
    func main()
    begin
        number a[2, 3] <- [a, [10, 20, 30]]
        a <- [1, 9, 6]
        writeNumber(a[0])
    end
    """
            expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(NumLit(10.0), NumLit(20.0), NumLit(30.0)))"
            self.assertTrue(TestChecker.test(input, expect, 483))
        
        def test484(self):
            input = """
    dynamic a
    func main()
    begin
        var x <- [a, [1, 2, 3]]
        a <- [1, 9, 6]
        x <- [[3, 9, 6], [1, 3, 2]]
        writeNumber(x[0, 0])
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 484))
        
        def test485(self):
            input = """
     func abc() 
                begin
                    dynamic x
                    return [x, [x, x]]
                end
    func main() return
    """
            expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x), ArrayLit(Id(x), Id(x))))"
            self.assertTrue(TestChecker.test(input, expect, 485))

        def test486(self):
            input = """
     func main() 
                begin
                    dynamic x
                    dynamic y
                    for x until true by x[1]
                        return
                end
    """
            expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
            self.assertTrue(TestChecker.test(input, expect, 486))
        
        def test487(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c <- a ... ", world!"
        a <- b
        b <- [1, 2, 3]
    end
    """
            expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
            self.assertTrue(TestChecker.test(input, expect, 487))
        
        def test488(self):
            input = """
    func main()
    begin
        number x
        begin
            number x <- (10 + x) * 2
        end
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 488))
        
        def test489(self):
            input = """
    func test(number x)

    func main()
    begin
        number test
        begin
            number x <- test(2018) + 1
        end
    end
    """
            expect = "No Function Definition: test"
            self.assertTrue(TestChecker.test(input, expect, 489))
        
        def test490(self):
            input = """
    dynamic x
    func f(number x)
        return x + 1

    func main()
    begin
        x <- f(20, 30, 40) + 1
    end
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(20.0), NumLit(30.0), NumLit(40.0)])"
            self.assertTrue(TestChecker.test(input, expect, 490))
        
        def test491(self):
            input = """
    func main()
    begin
        number a[1, 2, 3, 4]
        var b <- a[0]
        number d[1, 3, 4]
        b <- d
    end
    """
            expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(d))"
            self.assertTrue(TestChecker.test(input, expect, 491))
        
        def test492(self):
            input = """
    func f(number x, number y)
    begin
        if (y == 0) return x
        return f(y, x % y)
    end

    func main()
    begin
        number x <- readNumber()
        number y <- readNumber()
        dynamic res <- f(x, y)
        writeString(res)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(==, Id(y), NumLit(0.0))"
            self.assertTrue(TestChecker.test(input, expect, 492))
        
        def test493(self):
            input = """
    func f(number x, number y)
    begin
        if (y = 0) return x
        return f(y, x % y)
    end

    func main()
    begin
        number x[10]
        number y[10]
        var i <- 0
        for i until i >= 10 by 1
            x[i] <- readNumber()
        
        for i until i >= 10 by "Hello"
            y[i] <- readNumber()
        
    end
    """
            expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), StringLit(Hello), AssignStmt(ArrayCell(Id(y), [Id(i)]), CallExpr(Id(readNumber), [])))"
            self.assertTrue(TestChecker.test(input, expect, 493))
        
        def test494(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        dynamic x <- [a, b, c]
    end
    """
            expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
            self.assertTrue(TestChecker.test(input, expect, 494))
        
        def test495(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        dynamic x
        x <- [a, b, [c]]
    end
    """
            expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
            self.assertTrue(TestChecker.test(input, expect, 495))
        
        def test496(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        dynamic x <- (a ... b) ... c
        writeString(x)
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 496))
        
        def test497(self):
            input = """
     number a
                func foo(number a)
                begin
                    number a
                    if (true)
                    begin
                        number a
                    end
                    
                    begin
                        number a
                    end
                    
                    for a until true by 1
                    begin
                        number a
                    end
                end
                func main() 
                begin
                    number a
                end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 497))
        
        def test498(self):
            input = """
     number a
                func foo(number a)
                begin
                    number a
                    if (true) number b
                    else 
                        number b
                    
                end
                func main() return
    """
            expect = "Redeclared Variable: b"
            self.assertTrue(TestChecker.test(input, expect, 498))
        
        def test499(self):
            input = """
    func main()
    begin
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic x <- [a, [b, c], [d + 20, d ... "Hello"]]
        d <- x[0, 0] + x[0, 1]
        writeNumber(a[0] + a[1] + b + c + d)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(..., Id(d), StringLit(Hello))"
            self.assertTrue(TestChecker.test(input, expect, 499))
        
        def test500(self):
            input = """
    func main()
    begin
        number arr[2, 2] <- [1, 2, 3, 4]
    end
    """
            expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
            self.assertTrue(TestChecker.test(input, expect, 500))

        def test501(self):
            input = """
    func main(number x)
    begin
        writeNumber(x)
    end
    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 501))
            
        def test502(self):
            input = """
    number x
    var y <- 1.0
    dynamic z        

    func main()
    begin
        writeNumber(x)
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 502))
            
        def test503(self):
            input = """
    number x
    string s <- "Hello"
    var y <- 1.0
    dynamic z
    number k <- "OK"        

    func main()
    begin
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Statement: VarDecl(Id(k), NumberType, None, StringLit(OK))"
            self.assertTrue(TestChecker.test(input, expect, 503))
            
        def test504(self):
            input = """
    number x <- 1.0 + 2.0
    var y <- 1.2 + 3.2
    var z <- "OK" + 1
    func main()
    begin
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, StringLit(OK), NumLit(1.0))"
            self.assertTrue(TestChecker.test(input, expect, 504))
            
        def test505(self):
            input = """
    number x <- 1.0 + 2.0
    var y <- 1.2 + 3.2
    dynamic z
    var a <- z + x
    var k <- "OK" + 1
    func main()
    begin
        writeNumber(x)
    end
    """
            expect = "Type Mismatch In Expression: BinaryOp(+, StringLit(OK), NumLit(1.0))"
            self.assertTrue(TestChecker.test(input, expect, 505))
            
        def test506(self):
            input = """
    func foo(number y)
    begin
        return y
    end        

    func foo(number x)
    begin
        return x
    end

    func main()
    begin
        writeNumber(x)
    end
    """
            expect = "Redeclared Function: foo"
            self.assertTrue(TestChecker.test(input, expect, 506))
            
        def test507(self):
            input = """
    func foo() begin
         dynamic d
         return d
    end
    func main() return

    """
            expect = "Type Cannot Be Inferred: Return(Id(d))"
            self.assertTrue(TestChecker.test(input, expect, 507))
            
        def test508(self):
            input = """
    func main()
    """
            expect = "No Function Definition: main"
            self.assertTrue(TestChecker.test(input, expect, 508))
            
        def test509(self):
            input = """
    func foo(number a, number b)

    func main()
    begin
    	return 1 + foo(1, "str")
    end

    func foo(number a, number b)
    begin
    	return 0
    end
    """
            expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(str)])"
            self.assertTrue(TestChecker.test(input, expect, 509))
            
        def test510(self):
            input = """
    func foo(number a, number b)

    func main()
    begin
    	var x <- 1 + foo(1, 2)
    end

    func foo(number a, number b)
    begin
    	return 0
    end
    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 510))
    
# import unittest
# from TestUtils import TestChecker
# from AST import *


# class CheckSuite(unittest.TestCase):
    
#     def test_400(self):
#         input = """
# number a[5]
# string a[5]
# func main()
# begin
#     string b[5]
#     number a
# end
# """
#         expect = """Redeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 400))

#     def test_401(self):
#         input = """
# number a[5]
# func main()
# begin
#     string b[5]
#     number b
# end
# """
#         expect = """Redeclared Variable: b"""
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test_402(self):
#         input = """
# func foo(number a[5], string b)
# begin
#     number a[5]
#     var i <- 0
#     for i until i >= 5 by 1
#     begin
#         a[i] <- i * i + 5
#     end
#     return -1
# end

# func main()
# begin
#     string c
#     number c
# end
# """
#         expect = """Redeclared Variable: c"""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test_403(self):
#         input = """
# func foo(number a[5], string a)
# begin
#     number a[5]
#     var i <- 0
#     for i until i >= 5 by 1
#     begin
#         a[i] <- i * i + 5
#     end
#     return -1
# end

# func main()
# begin
#     string c
# end
# """
#         expect = """Redeclared Parameter: a"""
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test_404(self):
#         input = """
# func hey(string a[5], bool b)
# func foo(number a[5], bool b, string c)
# begin
#     number a[5]
#     var i <- 0
#     for i until i >= 5 by 1
#     begin
#         a[i] <- i * i + 5
#     end
#     return -1
# end

# func main()
# begin
#     string c
# end
# """
#         expect = """No Function Definition: hey"""
#         self.assertTrue(TestChecker.test(input, expect, 404))

#     def test_405(self):
#         input = """
# func foo(number a[5], string b)
# begin
#     number a[5]
#     var i <- 0
#     for i until i >= 5 by 1
#     begin
#         a[i] <- i * i + 5
#     end
#     return -1
# end

# func hey(string a[5], bool b)
# func foo(number a[5], string b)

# func main()
# begin
#     string c
# end
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 405))

#     def test_406(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- [[1, 2, 3], [4, 5, 6]]
#     return x[0, 0]
# end

# func main()
# begin
#     number x <- f()
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test_407(self):
#         input = """
# func f(number x)
# func f(number x)
# begin
#     if (x >= 2) return f(x - 1) + f(x - 2)
#     return 1
# end
# func main()
# begin
#     number x <- f(2)
#     writeNumber(x)
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test_408(self):
#         input = """
# func main()
# begin
#     number x
#     string s
#     bool a
#     x <- readNumber()
#     writeNumber(x)
#     s <- readString()
#     writeString(s)
#     a <- readBool()
#     writeBool(a)
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 408))

#     def test_409(self):
#         input = """
# func readNumber()
# func main()
# begin
# end
# """
#         expect = """Redeclared Function: readNumber"""
#         self.assertTrue(TestChecker.test(input, expect, 409))

#     def test_410(self):
#         input = """
# func main()
# """
#         expect = """No Function Definition: main"""
#         self.assertTrue(TestChecker.test(input, expect, 410))

#     def test_411(self):
#         input = """
# func main(number a)
# begin
#     return
# end
# """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test_412(self):
#         input = """
# func main()
# begin
#     return 0
# end
# """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 412))

#     def test_413(self):
#         input = """
# func foo(number a, string a, bool a[3])
# func foo(number a, string b, bool c[3])
# begin
#     return a
# end

# func main()
# begin
#     dynamic x <- foo(12, "abc", [true, true, false])
#     return
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 413))

#     def test_414(self):
#         input = """
# dynamic n
# func main()
# begin
#     dynamic a <- n
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(n))"""
#         self.assertTrue(TestChecker.test(input, expect, 414))

#     def test_415(self):
#         input = """
# dynamic n
# func main()
# begin
#     dynamic arr <- [[[n]], [[n]]]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(arr), None, dynamic, ArrayLit(ArrayLit(ArrayLit(Id(n))), ArrayLit(ArrayLit(Id(n)))))"""
#         self.assertTrue(TestChecker.test(input, expect, 415))

#     def test_416(self):
#         input = """
# func foo(number a, string a)
# func main()
# begin
#     dynamic c <- foo
# end
# """
#         expect = """Undeclared Identifier: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 416))

#     def test_417(self):
#         input = """
# dynamic x
# func main()
# begin
#     var y <- x
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(y), None, var, Id(x))"""
#         self.assertTrue(TestChecker.test(input, expect, 417))

#     def test_418(self):
#         input = """
# dynamic x
# func main()
# begin
#     var y <- [[[x]], [[x]]]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(y), None, var, ArrayLit(ArrayLit(ArrayLit(Id(x))), ArrayLit(ArrayLit(Id(x)))))"""
#         self.assertTrue(TestChecker.test(input, expect, 418))

#     def test_419(self):
#         input = """
# func foo(number a, string a)
# func main()
# begin
#     var c <- foo
# end
# """
#         expect = """Undeclared Identifier: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 419))

#     def test_420(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     number arr[2] <- [x, x, y]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0], NumberType), None, ArrayLit(Id(x), Id(x), Id(y)))"""
#         self.assertTrue(TestChecker.test(input, expect, 420))

#     def test_421(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     number arr[2, 3] <- [[x, x], y]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y)))"""
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test_422(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     string arr <- [[x, x], y]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(arr), StringType, None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y)))"""
#         self.assertTrue(TestChecker.test(input, expect, 422))

#     def test_423(self):
#         input = """
# func main()
# begin
#     number a <- "abc" ... "hello"
# end
# """
#         expect = """Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, BinaryOp(..., StringLit(abc), StringLit(hello)))"""
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test_424(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     number arr[2, 3] <- [[x, x, x], y]
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test_425(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     number arr[3, 2] <- [[x, x], y, ["abc", ""]]
# end
# """
#         expect = """Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y), ArrayLit(StringLit(abc), StringLit())))"""
#         self.assertTrue(TestChecker.test(input, expect, 425))

#     def test_426(self):
#         input = """
# func foo() return
# func foo()
# func main() return
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 426))

#     def test_427(self):
#         input = """
# func foo(number a) return
# func foo() return
# func main() return
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 427))

#     def test_428(self):
#         input = """
# func foo(number a, string a)
# func foo(number b, string b)
# func main() return
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 428))

#     def test_429(self):
#         input = """
# func foo()
# func foo() return
# func main() return
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 429))

#     def test_430(self):
#         input = """
# func foo(number a, string a)
# func foo(number c) return
# func main() return
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 430))

#     def test_431(self):
#         input = """
# func foo(number a, string a)
# func foo(number c, bool b) return
# func main() return
# """
#         expect = """Redeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 431))

#     def test_432(self):
#         input = """
# dynamic a
# dynamic b
# func main()
# begin
#     dynamic res <- a and (a % b)
# end
# """
#         expect = """Type Mismatch In Expression: BinaryOp(%, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 432))

#     def test_433(self):
#         input = """
# dynamic a
# dynamic b
# func main()
# begin
#     dynamic res <- a and (a >= b)
# end
# """
#         expect = """Type Mismatch In Expression: BinaryOp(>=, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 433))

#     def test_434(self):
#         input = """
# dynamic a
# dynamic b
# func main()
# begin
#     dynamic res <- a and (a ... b)
# end
# """
#         expect = """Type Mismatch In Expression: BinaryOp(..., Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 434))

#     def test_435(self):
#         input = """
# dynamic a
# dynamic b
# func main()
# begin
#     dynamic res <- a + (a == b)
# end
# """
#         expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 435))

#     def test_436(self):
#         input = """
# string s
# func main()
# begin
#     dynamic a <- -s
# end
# """
#         expect = """Type Mismatch In Expression: UnaryOp(-, Id(s))"""
#         self.assertTrue(TestChecker.test(input, expect, 436))

#     def test_437(self):
#         input = """
# string s
# func main()
# begin
#     dynamic a <- not s
# end
# """
#         expect = """Type Mismatch In Expression: UnaryOp(not, Id(s))"""
#         self.assertTrue(TestChecker.test(input, expect, 437))

#     def test_438(self):
#         input = """
# func main()
# begin
#     number a <- foo()
# end
# """
#         expect = """Undeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 438))

#     def test_439(self):
#         input = """
# func foo(number a, string a)
# func foo(number a, string b) return
# func main()
# begin
#     dynamic a <- foo(12)
# end
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(12.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 439))

#     def test_440(self):
#         input = """
# dynamic x
# func foo(number a[2]) return 12
# func main()
# begin
#     dynamic a <- foo([x, x, x]) + 33
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x), Id(x))]), NumLit(33.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 440))

#     def test_441(self):
#         input = """
# dynamic x
# func foo(number a[3, 2]) return 12
# func main()
# begin
#     dynamic a <- foo([x, x]) + 13
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), NumLit(13.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 441))

#     def test_442(self):
#         input = """
# dynamic x
# func foo(string a) return 12
# func main()
# begin
#     dynamic a <- foo([x, x]) + 13
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), NumLit(13.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 442))

#     def test_443(self):
#         input = """
# dynamic x
# func foo(number a[2]) return 12
# func main()
# begin
#     x <- 10 + 20
#     dynamic a <- foo([x, x]) + 13
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 443))

#     def test_444(self):
#         input = """
# dynamic x
# func foo(number a) return 12
# func main()
# begin
#     x <- 10 + 20
#     dynamic a <- foo("abc") + 13
# end
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(abc)])"""
#         self.assertTrue(TestChecker.test(input, expect, 444))

#     def test_445(self):
#         input = """
# func main() return x
# """
#         expect = """Undeclared Identifier: x"""
#         self.assertTrue(TestChecker.test(input, expect, 445))

#     def test_446(self):
#         input = """
# dynamic x
# func main()
# begin
#     number a <- x[0]
# end
# """
#         expect = """Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayCell(Id(x), [NumLit(0.0)]))"""
#         self.assertTrue(TestChecker.test(input, expect, 446))

#     def test_447(self):
#         input = """
# string s <- "Hello world"
# func main()
# begin
#     string ss <- s[1]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayCell(Id(s), [NumLit(1.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 447))

#     def test_448(self):
#         input = """
# number arr[3, 2, 2] <- [[[3, 4], [1, 9]], [[6, 6], [7, 7]], [[8, 8], [10, 10]]]
# func main()
# begin
#     dynamic x <- arr[2, 1, 1, 2]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayCell(Id(arr), [NumLit(2.0), NumLit(1.0), NumLit(1.0), NumLit(2.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 448))

#     def test_449(self):
#         input = """
# func foo() return
# func main()
# begin
#     number arr[3] <- [1, 2, 3]
#     dynamic x <- arr[foo()]
# end
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [])"""
#         self.assertTrue(TestChecker.test(input, expect, 449))

#     def test_450(self):
#         input = """
# func foo() return
# func main()
# begin
#     if(foo()) dynamic x
# end
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [])"""
#         self.assertTrue(TestChecker.test(input, expect, 450))

#     def test_451(self):
#         input = """
# func foo() return true
# func main()
# begin
#     number x
#     if(foo()) dynamic x
# end
# """
#         expect = """Redeclared Variable: x"""
#         self.assertTrue(TestChecker.test(input, expect, 451))

#     def test_452(self):
#         input = """
# func foo() return true
# func foo1() return
# func main()
# begin
#     if(foo()) dynamic x
#     elif(true) dynamic z
#     elif(foo1()) dynamic y
# end
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo1), [])"""
#         self.assertTrue(TestChecker.test(input, expect, 452))

#     def test_453(self):
#         input = """
# func main()
# begin
#     if(true) dynamic x
#     elif(true) var x <- 123
#     elif(true) dynamic y
# end
# """
#         expect = """Redeclared Variable: x"""
#         self.assertTrue(TestChecker.test(input, expect, 453))

#     def test_454(self):
#         input = """
# func foo() return true
# func foo1() return true
# func main()
# begin
#     if(foo()) dynamic x
#     elif(true)
#     begin
#         var x <- 123
#     end
#     elif(foo1()) dynamic y
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 454))

#     def test_455(self):
#         input = """
# func foo() return true
# func foo1() return true
# func main()
# begin
#     if(foo()) dynamic x
#     elif(true)
#     begin
#         var x <- 123
#     end
#     elif(foo1()) dynamic y
#     else
#         var y <- 12
# end
# """
#         expect = """Redeclared Variable: y"""
#         self.assertTrue(TestChecker.test(input, expect, 455))

#     def test_456(self):
#         input = """
# func foo() return true
# func foo1() return true
# func main()
# begin
#     if(foo()) dynamic x
#     elif(true)
#     begin
#         var x <- 123
#     end
#     elif(foo1()) dynamic y
#     else
#     begin
#         var y <- 12
#     end
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 456))

#     def test_457(self):
#         input = """
# func main()
# begin
#     string i
#     for i until true by 1
#         dynamic x
# end
# """
#         expect = """Type Mismatch In Statement: For(Id(i), BooleanLit(True), NumLit(1.0), VarDecl(Id(x), None, dynamic, None))"""
#         self.assertTrue(TestChecker.test(input, expect, 457))

#     def test_458(self):
#         input = """
# func main()
# begin
#     number i
#     dynamic j
#     for i until j + 3 by 1
#         dynamic x
# end
# """
#         expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(+, Id(j), NumLit(3.0)), NumLit(1.0), VarDecl(Id(x), None, dynamic, None))"""
#         self.assertTrue(TestChecker.test(input, expect, 458))

#     def test_459(self):
#         input = """
# func main()
# begin
#     number i
#     dynamic j
#     for i until true by j = 2
#         dynamic x
# end
# """
#         expect = """Type Mismatch In Statement: For(Id(i), BooleanLit(True), BinaryOp(=, Id(j), NumLit(2.0)), VarDecl(Id(x), None, dynamic, None))"""
#         self.assertTrue(TestChecker.test(input, expect, 459))

#     def test_460(self):
#         input = """
# func main()
# begin
#     number x
#     number i <- 1
#     for i until i < 10 by 1
#         dynamic x
# end
# """
#         expect = """Redeclared Variable: x"""
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test_461(self):
#         input = """
# func main()
# begin
#     number x
#     number i <- 1
#     for i until i < 10 by 1
#         if(true) dynamic x
# end
# """
#         expect = """Redeclared Variable: x"""
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test_462(self):
#         input = """
# func main()
# begin
#     number x
#     number i <- 1
#     number j <- 1
#     for i until i < 10 by 1
#         if(true)
#             for j until j < 10 by 1
#                 dynamic x
# end
# """
#         expect = """Redeclared Variable: x"""
#         self.assertTrue(TestChecker.test(input, expect, 462))

#     def test_463(self):
#         input = """
# func main()
# begin
#     number x
#     number i <- 1
#     number j <- 1
#     for i until i < 10 by 1
#     begin
#         if(true)
#             for j until j < 10 by 1
#                 dynamic x <- i + 12
#                 number i <- 100
#     end
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 463))

#     def test_464(self):
#         input = """
# func foo()
# begin
#     continue
# end
# func main()
# begin
#     number i <- 1
#     number j <- 1
#     for i until i < 10 by 1
#         for j until j < 10 by 1
#             foo()
# end
# """
#         expect = """Continue Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 464))

#     def test_465(self):
#         input = """
# func foo()
# begin
#     break
# end
# func main()
# begin
#     number i <- 1
#     number j <- 1
#     for i until i < 10 by 1
#         for j until j < 10 by 1
#             foo()
# end
# """
#         expect = """Break Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 465))

#     def test_466(self):
#         input = """
# func foo()
# begin
#     return
# end
# func main()
# begin
#     number i <- 1
#     number j <- 1
#     continue
#     break
#     for i until i < 10 by 1
#         for j until j < 10 by 1
#             foo()
# end
# """
#         expect = """Continue Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test_467(self):
#         input = """
# func main()
# begin
#     number i <- 1
#     number j <- 1
#     number k <- 1
#     for i until i < 10 by 1
#     begin
#         continue
#         for j until j < 10 by 1
#         begin
#             break
#             for k until k < 10 by 1
#                 if (true) continue
#                 elif (false) break
#                 else continue
#         end
#     end
                
# end
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test_468(self):
#         input = """
# dynamic x
# func foo() return x
# func main() return
# """
#         expect = """Type Cannot Be Inferred: Return(Id(x))"""
#         self.assertTrue(TestChecker.test(input, expect, 468))

#     def test_469(self):
#         input = """
# dynamic x
# func foo() return [x, x]
# func main() return
# """
#         expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test_470(self):
#         input = """
# func foo()
# func main()
# begin
#     number a <- foo() + 13
# end
# func foo() return
# """
#         expect = """Type Mismatch In Statement: Return()"""
#         self.assertTrue(TestChecker.test(input, expect, 470))

#     def test_471(self):
#         input = """
# dynamic x
# func foo()
# func main()
# begin
#     foo()
# end
# func foo() return [x, x]
# """
#         expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 471))

#     def test_472(self):
#         input = """
# dynamic x
# dynamic arr
# func foo()
# func main()
# begin
#     number a[3]
#     arr <- a
#     arr <- foo()
# end
# func foo() return [[x]]
# """
#         expect = """Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(x))))"""
#         self.assertTrue(TestChecker.test(input, expect, 472))

#     def test_473(self):
#         input = """
# dynamic x
# dynamic arr
# func foo()
# func main()
# begin
#     number a[3]
#     arr <- a
#     arr <- foo()
# end
# func foo() return [x, x]
# """
#         expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 473))

#     def test_474(self):
#         input = """
# dynamic x
# func foo()
# func main()
# begin
#     number a
#     a <- foo()
# end
# func foo() return [x, x]
# """
#         expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 474))

#     def test_475(self):
#         input = """
# dynamic x
# dynamic arr
# func foo()
# func main()
# begin
#     number a[3]
#     arr <- a
#     arr <- foo()
# end
# func foo() return [x, x, x]
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 475))

#     def test_476(self):
#         input = """
# dynamic x
# func foo()
# func main()
# begin
#     number a
#     a <- foo()
# end
# func foo() return true
# """
#         expect = """Type Mismatch In Statement: Return(BooleanLit(True))"""
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test_477(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     x <- y
# end
# """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(x), Id(y))"""
#         self.assertTrue(TestChecker.test(input, expect, 477))

#     def test_478(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     x <- [y, y, x]
# end
# """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(y), Id(y), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 478))

#     def test_479(self):
#         input = """
# func main()
# begin
#     dynamic x
#     number a[2]
#     a <- [[x, x], [x, x]]
# end
# """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(x), Id(x))))"""
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test_480(self):
#         input = """
# func main()
# begin
#     dynamic x
#     number a[2]
#     a <- [[x, x], [x, 1]]
# end
# """
#         expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(x), NumLit(1.0))))"""
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test_481(self):
#         input = """
# func main()
# begin
#     dynamic x
#     number a[2]
#     a <- [x, x, x]
# end
# """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 481))

#     def test_482(self):
#         input = """
# func main()
# begin
#     dynamic x
#     string a
#     a <- [x, x, x]
# end
# """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 482))

#     def test_483(self):
#         input = """
# func main()
# begin
#     number x
#     string a
#     a <- [x, x, x]
# end
# """
#         expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 483))

#     def test_484(self):
#         input = """
# func main()
# begin
#     number x
#     string a
#     a <- x
# end
# """
#         expect = """Type Mismatch In Statement: AssignStmt(Id(a), Id(x))"""
#         self.assertTrue(TestChecker.test(input, expect, 484))

#     def test_485(self):
#         input = """
# func main()
# begin
#     foo()
# end
# """
#         expect = """Undeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test_486(self):
#         input = """
# func foo() return 12
# func main()
# begin
#     foo()
# end
# """
#         expect = """Type Mismatch In Statement: CallStmt(Id(foo), [])"""
#         self.assertTrue(TestChecker.test(input, expect, 486))

#     def test_487(self):
#         input = """
# func foo(number a, string a)
# func main()
# begin
#     foo(12, "abc", true)
# end
# func foo(number x, string y) return
# """
#         expect = """Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(12.0), StringLit(abc), BooleanLit(True)])"""
#         self.assertTrue(TestChecker.test(input, expect, 487))

#     def test_488(self):
#         input = """
# func foo(number a[3], string b) return
# func main()
# begin
#     dynamic x
#     foo([[x]], "abc")
# end
# """
#         expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
#         self.assertTrue(TestChecker.test(input, expect, 488))

#     def test_489(self):
#         input = """
# func foo(number a[1, 3], string b) return
# func main()
# begin
#     dynamic x
#     foo([[x]], "abc")
# end
# """
#         expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
#         self.assertTrue(TestChecker.test(input, expect, 489))

#     def test_490(self):
#         input = """
# func foo(number a, string b) return
# func main()
# begin
#     dynamic x
#     foo([[x]], "abc")
# end
# """
#         expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
#         self.assertTrue(TestChecker.test(input, expect, 490))

#     def test_491(self):
#         input = """
# func foo(number a, string b) return
# func main()
# begin
#     dynamic x
#     foo([x, false], "abc")
# end
# """
#         expect = """Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x), BooleanLit(False)), StringLit(abc)])"""
#         self.assertTrue(TestChecker.test(input, expect, 491))

#     def test_492(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 2, 3]
#     a <- [[[x, x]], [y, y]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(Id(x), Id(x))), ArrayLit(Id(y), Id(y)))"""
#         self.assertTrue(TestChecker.test(input, expect, 492))

#     def test_493(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 2, 3]
#     a <- [[1, 1], [[y, y]]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0)), ArrayLit(ArrayLit(Id(y), Id(y))))"""
#         self.assertTrue(TestChecker.test(input, expect, 493))

#     def test_494(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 2, 3]
#     a <- [[[1, 1]], [y, y]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))), ArrayLit(Id(y), Id(y)))"""
#         self.assertTrue(TestChecker.test(input, expect, 494))

#     def test_495(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 2, 3]
#     a <- [[[y, y]], [1, 1]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(Id(y), Id(y))), ArrayLit(NumLit(1.0), NumLit(1.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 495))

#     def test_496(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 2, 3]
#     a <- [[y, y], [[1, 1]]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))))"""
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test_497(self):
#         input = """
# func main()
# begin
#     number a[2, 2, 3]
#     a <- [[1, 2], [[1, 1]]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))))"""
#         self.assertTrue(TestChecker.test(input, expect, 497))

#         input = """
# func main()
# begin
#     dynamic x
#     number a[2, 2, 3]
#     a <- ["abc", [x]]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(StringLit(abc), ArrayLit(Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 497))

#         input = """
# func main()
# begin
#     dynamic x
#     number a[2, 2, 3]
#     a <- [[x], 12]
# end
# """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x)), NumLit(12.0))"""
#         self.assertTrue(TestChecker.test(input, expect, 497))

#     def test_498(self):
#         input = """
# func x()
# func main()
# begin
#     dynamic x
#     number a[2]
#     a <- [x, [x, x]]
# end
# func x() return 12
# """
#         expect = """Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"""
#         self.assertTrue(TestChecker.test(input, expect, 498))
        
#         input = """
# func x()
# func main()
# begin
#     dynamic x
#     number a[2, 2]
#     a <- [x, [x(), x()]]
# end
# func x() return 12
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 498))

#         input = """
# func x()
# func main()
# begin
#     dynamic x
#     number a[2, 2]
#     a <- [x(), [x, x]]
#     number c[2] <- x()
# end
# func x() return [1, 2]
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 498))

#         input = """
# func x()
# func y()
# func z()
# func main()
# begin
#     dynamic x
#     dynamic y
#     dynamic z
#     number a[2, 2, 2, 2]
#     a <- [[[[y(), x], y], z], [[[x, y()], z()], x()]]
#     number x1 <- x
#     number x2[2, 2] <- x()
#     number y1[2] <- y
#     number y2 <- y()
#     number z1[2, 2] <- z
#     number z2[2] <- z() 
# end
# func x() return [[1, 2], [3, 4]]
# func y() return 5
# func z() return [6, 7]
# """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 498))

#     def test_499(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if ([x]) return
# end
# """
#         expect = """Type Cannot Be Inferred: If((ArrayLit(Id(x)), Return()), [], None)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#         input = """
# func main()
# begin
#     if ([1, 2, 3]) return
# end
# """
#         expect = """Type Mismatch In Statement: If((ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), Return()), [], None)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#         input = """
# func main()
# begin
#     dynamic x
#     number i <- 1
#     for i until [x] by 1
#         break
# end
# """
#         expect = """Type Cannot Be Inferred: For(Id(i), ArrayLit(Id(x)), NumLit(1.0), Break)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#         input = """
# func main()
# begin
#     dynamic x
#     number i <- 1
#     for i until i < 10 by [x]
#         break
# end
# """
#         expect = """Type Cannot Be Inferred: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), ArrayLit(Id(x)), Break)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#         input = """
# func main()
# begin
#     dynamic x
#     number i <- 1
#     for i until [1, 2] by 1
#         break
# end
# """
#         expect = """Type Mismatch In Statement: For(Id(i), ArrayLit(NumLit(1.0), NumLit(2.0)), NumLit(1.0), Break)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))

#         input = """
# func main()
# begin
#     dynamic x
#     number i <- 1
#     for i until i < 10 by [[1, 2], [3, 4]]
#         break
# end
# """
#         expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0))), Break)"""
#         self.assertTrue(TestChecker.test(input, expect, 499))
