import unittest
from TestUtils import TestParser
## MSSV : 2110242
class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Test 200 """
        input = """func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_201(self):
        """Test 201 """
        input = """func main() return 1
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_202(self):
        """Test 202 """
        input = """number a = 1
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_203(self):
        """Test 203 """
        input = """number a,b,c = 1
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_204(self):
        """Test 204 """
        input = """string a = \"string\"
        number b,c = 1.e-10
        bool d = false
        bool e = true
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_205(self):
        """Test 205 """
        input = """number a[3]
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_206(self):
        """Test 206 """
        input = """number a[5,4,3,2,1]
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_207(self):
        """Test 207 """
        input = """var i <- 2110242.e2110242
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_208(self):
        """Test 208 """
        input = """var i <- \"this is string\"
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_209(self):
        """Test 209 """
        input = """var i <- \"this is \\n \\t string\"
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_210(self):
        """Test 210 """
        input = """var i <- \"this is \\n \\i string\"
""" 
        expect = "this is \\n \\i"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_211(self):
        """Test 211 """
        input = """var i <- \"this is string
""" 
        expect = "this is string"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_212(self):
        """Test 212 """
        input = """var i <- true
        var a <- \"this is \\n \\b \\t \\r string\"
        number a,b,c
        string d
        number e = 2110242.e2110242
        dynamic f 
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_213(self):
        """Test 213 """
        input = """var i <-""" 
        expect = "Error on line 1 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_214(self):
        """Test 214 """
        input = """number a = 15.234e13 ##this is comment \n""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_215(self):
        """Test 215 """
        input = """number a = 15.234e-13 #this is comment \n""" 
        expect = "#"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_216(self):
        """Test 216 """
        input = """func main() return a[3 + foo(2)]
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_217(self):
        """Test 217 """
        input = """func main(){}""" 
        expect = "{"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_218(self):
        """Test 218 """
        input = """func main()""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_219(self):
        """Test 219 """
        input = """func main() return""" 
        expect = "Error on line 1 col 18: <EOF>"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_220(self):
        """Test 220 """
        input = """func main(number a[3],string b, bool c)
begin
a[3+ foo()] <- a[b[2,3] + 4]
c = false
b = \" this is string\"
return a or b or c
end
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_221(self):
        """Test 221 """
        input = """func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_222(self):
        """Test 222 """
        input = """number _array[5] <- [1,2,3,4,5]""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_223(self):
        """Test 223 """
        input = """number two_side_array[2, 3] <- [[1, 2],[4, 5]]""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_224(self):
        """Test 224 """
        input = """number two_side_array[2, 3] <- [[true, false],[false, true]]
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_225(self):
        """Test 225 """
        input = """number two_side_array[2, 3] <- [[\"true\", \"false\"],[\"false\", \"true\"]]""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_226(self):
        """Test 226 """
        input = """number two_side_array[2, 3] <- [[10.e10, 20.e20],[0, 3.]]""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_227(self):
        """Test 227 """
        input = """number two_side_array[2, 3] <- [[foo(), bar()],[false or true, a and b]]""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_228(self):
        """Test 228 """
        input = """func main() return 1 ## This is a comment""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_229(self):
        """Test 229 """
        input = """func main(number a) 
        begin
        var i <- 0
        i = i * i
        return ((i*5 + 1) or (i*5 - 1)) 
        end
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_230(self):
        """Test 230 """
        input = """bool a[3)""" 
        expect = "Error on line 1 col 8: )"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_231(self):
        """Test 231 """
        input = """var i < - 5""" 
        expect = "Error on line 1 col 6: <"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_232(self):
        """Test 232 """
        input = """var i == 5""" 
        expect = "Error on line 1 col 6: =="
        self.assertTrue(TestParser.test(input,expect,232))
    def test_233(self):
        """Test 233 """
        input = """var i <- 5 
        string a = \"this is string\"
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_234(self):
        """Test 234 """
        input = """func isEven(number x)## Function to check even number
    begin
    return (x % 2 = 0)
    end
func main()
    begin
    number x <- readNumber()
    if (isEven(x)) writeString("Yes")
    else writeString("No")
    end
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_235(self):
        """Test 235 """
        input = """func isSquare(number x)
begin
var root <- sqrt(x)
return (root * root = x)
end

func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("x is a prime number")
elif (isSquare(x)) writeString("x is a perfect square")
else writeString("x is neither a prime number nor a perfect square")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_236(self):
        """Test 236 """
        input = """func factorial(number x)
begin
if ((x = 0) or (x = 1)) return 1
else return x * factorial(x - 1)
end

func main()
begin
number x <- readNumber()
writeString("The factorial of x is: ")
writeNumber(factorial(x))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_237(self):
        """Test 237 """
        input = """func main()
begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
aPI <- 3.14
a[3] <- value * aPi
end        
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_238(self):
        """Test 238 """
        input = """func quickSort(number a[10], number low, number high) ## QUICK SORT
begin
    if (low < high)
        begin
        number pi <- partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)
        end
end

func partition(number a[10], number low, number high)
begin
    number pivot <- a[high]
    number i <- (low - 1)
    number j = low 
    for j until j <= high - 1 by 1
    begin
    if (a[j] < pivot)
    begin
    i <- i + 1
    swap(a[i], a[j])
    end
    end
    swap(a[i + 1], a[high])
    return (i + 1)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_239(self):
        """Test 239 """
        input = """func selectionSort(number a[10], number n)
begin
var i <- 0
for i until i < n by 1
begin
    number min_idx <- i
    var j <- i + 1
    for j until j < n by 1
    begin
    if (a[j] < a[min_idx])
        min_idx <- j
    end
    swap(a[min_idx], a[i])
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_240(self):
        """Test 240 """
        input = """func bubbleSort(number a[10], number n)
begin
var i <- 0
for i until i < n - 1 by 1
begin
    var j <- 0
    for j until j < n - i - 1 by 1
    begin
    if (a[j] > a[j + 1])
        swap(a[j], a[j + 1])
    end
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_241(self):
        """Test 241 """
        input = """func main(number a[10], number n)
begin
var n <- 10
var i <- 0
for i until i < n by 1
begin
a[i] <- i * n + a[i] 
end
return 0
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_242(self):
        """Test 242 """
        input = """func main(number a[10], number n) 
var n <- 10
var i <- 0
for i until i < n by 1
a[i] <- i * n + a[i] 
return 0
"""
        expect = "Error on line 2 col 0: var"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_243(self):
        """Test 243 """
        input = """func main() return 0
        var i <- 0
        number a
        readnumber(a)
        writeNumber(a)
        ## This is a comment

        """
        expect = "Error on line 2 col 18: \n\n"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_244(self):
        """Test 244 """
        input = """func main()
        begin
        var i <- 0
        number a
        readnumber(a)
        writeNumber(a)
        if a > 0 writeNumber(a)
        elif a = 0 
            a = a + 1 
        else 
            writeNumber(a)
        ## This is a comment
        end
        """
        expect = "Error on line 9 col 14: ="
        self.assertTrue(TestParser.test(input,expect,244))
    def test_245(self):
        """Test 245 """
        input = """func main()
        begin
        var i <- 0 number a[10]
        ## This is a comment
        end
        """
        expect = "Error on line 3 col 19: number"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_246(self):
        """Test 246 """
        input = """func main()
        begin
        var i <- 0
        number a[10]
        for i until i < 10 by 1
        begin
            if (i % 2 = 0)
                a[i] <- i ##Assign a[i] by i 
            else
                a[i] <- 0
        end
        ## This is a comment
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_247(self):
        """Test 247 """
        input = """func main()
        begin
        i <- 0 ## test comment
        number a ## test comment
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_248(self):
        """Test 248 """
        input = """func main()
        begin
        i <- 0 ## test comment number a ## test comment
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_249(self):
        """Test 249 """
        input = """func main() ## test comment
        begin ## test comment
        i <- 0 ## test comment
        number a ## test comment
        end ## test comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_250(self):
        """Test 250 """
        input = """## test comment"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_251(self):
        """Test 251 """
        input = """
        """
        expect = "Error on line 1 col 0: \n\n"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_252(self):
        """Test 252 """
        input = """func decrease(number n) return n - 1
        func main()
        begin
        number a[10] <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        var i <- 0
        for i until i < 10 by 1
        begin
            if a[i] % 3 = 1
                a[i] <- decrease(a[i]) ## Decrease a[i] by 1
            else
                if i < 5
                    a[i] <- decrease(decrease(a[i])) ## Decrease a[i] by 2
                elif i = 5
                    a[i] <- 5
                elif ((i > 5) and (i < 7))
                    a[i] <- 0
                else
                    break
        end
        var j <- 0
        for j until j < 10 by 1 writeNumber(a[j]) ## print array 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_253(self):
        input = """func main()
        begin
        var i <- 0
        number a[3,3] <- [[1,2,3],[3,4,5],[4,5,6]] ## Define Matrix 3x3
        for i until i < 3 by 1
        begin
            var j <- i
            for j until j < 3 by 1
                writeNumber(a[i,j]) ## Print the Matrix
        end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_254(self):
        input = """func main()
    begin
    var i <- 0
    number a[3,3] <- [[1,2,3],[3,4,5],[4,5,6]]
    number b[3,3] <- [[7,8,9],[10,11,12],[13,14,15]]
    number c[3,3] <- [[0,0,0],[0,0,0],[0,0,0]]
    for i until i < 3 by 1
    begin
        var j <- 0
        for j until j < 3 by 1
        begin
            var k <- 0
            for k until k < 3 by 1
                c[i,j] <- c[i,j] + a[i,k] * b[k,j]
        end
    end
    for i until i < 3 by 1
    begin
        var j <- 0
        for j until j < 3 by 1
            writeNumber(c[i,j])
    end
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_255(self):
        input = """func main()
        begin
        number i = 1
        string a = \"HELLO\" 
        string b = readString()
        if a == b 
            print("TRUE")
            break 
        else print("FALSE")
        end
        """
        expect = "Error on line 9 col 8: else"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_256(self):
        input = """func main()
        begin
        number i = 1
        string a = \"HELLO\" 
        string b = readString()
        if a == b
        begin 
            print("TRUE")
            break 
        end
        else 

        begin
            print("FALSE")
            return 0
        end 
        return 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_257(self):
        input = """func main()
        begin
        string s <- \"The quick brown fox jumps over the lazy dog\"
        string longestWord <- \"\"
        string word <- \"\"
        var n <- length(s)
        var i <- 0
        for i until i < n by 1
        begin
            if s[i] != \" \"
                word <- word + s[i]
            else
            begin
                if length(word) > length(longestWord)
                    longestWord <- word
                word <- \"\"
            end
        end
        if length(word) > length(longestWord)
            longestWord <- word
        writeString(longestWord)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_258(self):
        """test 258"""
        input = """func main()
        begin
        string s
        s <- readString() 
        var n <- length(s)
        dynamic isPalindrome <- true
        var i <- 0
        for i until i < n / 2 by 1
        begin
            if s[i] != s[n - i - 1]
                isPalindrome <- false
        end
        if isPalindrome
            writeString("The string is a palindrome.")
        else
            writeString("The string is not a palindrome.")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_259(self):
        """test 259"""
        input = """func main()
        begin
        string s <- "Hello, World!"
        var n <- length(s)
        string reversed <- \"\"
        var i <- n - 1
        for i  until i >= 0 by -1
            reversed <- reversed + s[i]

        writeString(reversed)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_260(self):
        """test 260"""
        input = """func main()
        begin
        string s <- "Hello, World!"
        var n <- length(s)
        string reversed <- \"\"
        var i <- n - 1
        for i  until i >= 0 by -1
            reversed <- reversed + s[i]

        writeString(reversed)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_261(self):
        """test 261"""
        input = """func toTitleCase(string s)
    begin
    var result <- \"\"
    var n <- length(s)
    var i <- 0
    for i until i < n by 1
    begin
        if (i = 0) or (s[i - 1] == \"\")
            result <- result + toUpper(s[i])
        else
            result <- result + toLower(s[i])
    end
    return result
    end

func main()
    begin
    string s <- \"hello, world! hello, Copper!\"
    string titleCase <- toTitleCase(s)
    writeString(titleCase)
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_262(self):
        """test 262"""
        input = """func caesarCipher(string s, number shift)
begin
    var result <- \"\"
    var n <- length(s)
    var i <- 0
    for i until i < n by 1
    begin
        if (isAlpha(s[i]))
        begin
            string base
            if isUpper(s[i]) base <- \"A\" 
            else  base <-\"a\"
            var offset <- (ord(s[i]) - ord(base) + shift) % 26
            result <- result + chr(ord(base) + offset)
        end
        else
            result <- result + s[i]
    end
    return result
end

func main()
    begin
    string s <- \"Hello, World!\"
    var shift <- 3
    string cipherText <- caesarCipher(s, shift)
    writeString(cipherText)
    end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_263(self):
        """test 263"""
        input = """func findMostFrequent(number arr[15])
    begin
    var n <- length(arr)
    var maxCount <- 0
    var index <- -1
    var i <- 0
    for i until i < n by 1
    begin
        var count <- 0
        var j <- 0
        for j until j < n by 1
        begin
            if (arr[i] = arr[j]) count <- count + 1
        end
        if count > maxCount
        begin
            maxCount <- count
            index <- i
        end
    end
    return arr[index]
    end

func main()
    begin
    number arr[5] <- [1, 3, 2, 1, 4]
    var mostFrequent <- findMostFrequent(arr)
    writeNumber(mostFrequent)
    end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_264(self):
        """test 264"""
        input = """func countOccurrences(string s, string word)
    begin
    var count <- 0
    var n <- length(s)
    var i <- 0
    for i until i < n by 1
    begin
        if substring(s, i, length(word)) == word
            count <- count + 1
    end
    return count
    end

func findMostFrequentWord(string s, string words)
    begin
    var maxCount <- 0
    var mostFrequent <- \"\"
    var n <- length(words)
    var i <- 0
    for i until i < n by 1
    begin
        var count <- countOccurrences(s, words[i])
        if count > maxCount
        begin
            maxCount <- count
            mostFrequent <- words[i]
        end
    end
    return mostFrequent
    end

func main()
    begin
    string s <- "apple banana apple orange apple grape banana apple"
    string words[4] <- ["apple", "banana", "orange", "grape"]
    var mostFrequent <- findMostFrequentWord(s, words)
    writeString(mostFrequent)
    end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_265(self):
        """test 265"""
        input = """func countOccurrences(string s, string sub)
    begin
    var count <- 0
    var n <- length(s)
    var i <- 0
    for i until i < n by 1
    begin
        if substring(s, i, length(sub)) == sub
            count <- count + 1
    end
    return count
    end

func main()
    begin
    string s <- "Hello, World! Hello!"
    string sub <- "Hello"
    var count <- countOccurrences(s, sub)
    writeNumber(count)
    end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_266(self):
        """test 266"""
        input = """func main()
        begin
        bool a[5] <- [true, false, true, false, true]
        number i = 0
        for i until i < 5 by 1
            begin
                if a[i] == true begin
                    writeString(\"true\")
                end
                else continue

            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_267(self):
        input = """func fibonacci(number n)
    begin
    if n <= 1
        return n
    var a <- 0
    var b <- 1
    var i <- 0
    for i until i <= n by 1
    begin
        var c <- a + b
        a <- b
        b <- c
    end
    return b
    end

func main()
    begin
    var n <- 10
    var fib <- fibonacci(n)
    writeNumber(fib)
    end
    """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 267))
    def test_268(self):
        input = """func main()
    begin
    var i <- 0
    begin ## intend to use begin without for loop
        writeString(\"Hello\")
        i <- i + 1
    end
    end
    """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 268))
    def test_269(self):
        input = """func gcd(number a, number b)
    begin
    if b > a
    begin
        var temp <- a
        a <- b
        b <- temp
    end
    var t <- b
    for t until t > 0 by -1
    begin
        if (a % t == 0) and (b % t == 0)
            return t
    end
    return 1
    end

func lcm(number a, number b)
    begin
    return a * b / gcd(a, b)
    end

func main()
    begin
    dynamic a <- 48
    dynamic b <- 18
    var result <- lcm(a, b)
    writeNumber(result)
    end
    """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 269))
    def test_270(self):
        input = """func main()
        for 0_ until 0_ < 10 by 1 ## test for loop
        begin
            writeString(\"Hello\")
        end
        """
        output = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.test(input, output, 270))
    def test_271(self):
        input = """## test for loop
        for _0 until _0 < 10 by 1
        begin
            writeString(\"Hello\")
        end
        """
        output = "Error on line 1 col 16: \n\n"
        self.assertTrue(TestParser.test(input, output, 271))
    def test_272(self):
        input = """func length(number arr[30])
        begin
        var count <- 0
        var i <- 0
        for i until i < length(arr) by 1
        begin
            count <- count + 1
        end
        return count
        end

func interpolationSearch(number arr[30], number x)
    begin
    var low <- 0
    var high <- length(arr) - 1
    var pos <- 0
    var i <- 0
    for i until i < high by 1
    begin
        if (low <= high) and (x >= arr[low]) and (x <= arr[high])
        begin
            var pos <- low + ((x - arr[low]) * (high - low)) / (arr[high] - arr[low])
            if arr[pos] == x
                return pos
            elif arr[pos] < x
                low <- pos + 1
            else
                high <- pos - 1
        end
    end
    return -1
    end

func main()
    begin
    number arr[5] <- [10, 20, 30, 40, 50]
    var x <- 40
    var index <- interpolationSearch(arr, x)
    writeNumber(index)
    end
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 272))
    def test_273(self):
        input = """func binarySearch(number arr[20], number left, number right,number x)
    begin
    if right >= left
    begin
        var mid <- left + (right - left) / 2
        if arr[mid] == x
            return mid
        else if arr[mid] > x
            return binarySearch(arr, left, mid - 1, x)
        return binarySearch(arr, mid + 1, right, x)
    end
    return -1
    end

func main()
    begin
    number arr[5] <- [1, 2, 3, 4, 5]
    var x <- 3
    var index <- binarySearch(arr, 0, length(arr) - 1, x)
    writeNumber(index)
    end
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 273))
    def test_274(self):
        input = """func linearSearch(number arr[30], number x)
    begin
    var n <- length(arr)
    for var i <- 0 until i < n by 1
    begin
        if arr[i] == x
            return i
    end
    return -1
    end

func main()
    begin
    number arr[5] <- [1, 3, 2, 1, 4]
    var x <- 2
    var index <- linearSearch(arr, x)
    writeNumber(index)
    end
        """
        output = "Error on line 4 col 8: var"
        self.assertTrue(TestParser.test(input, output, 274))
    def test_275(self):
        input = """func main()
        begin var i<-5         
        end
        """
        output = "Error on line 2 col 14: var"
        self.assertTrue(TestParser.test(input, output, 275))
    def test_276(self):
        input = """func main()
        begin 
        end
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 276))
    def test_277(self):
        input = """func main()
        begin 
        func body(string s, string b)
        func body(string s, string b)
        begin ## intend to test func declaration in a func
        end
        end
        """
        output = "Error on line 3 col 8: func"
        self.assertTrue(TestParser.test(input, output, 277))
    def test_278(self):
        input = """func main()
        begin 
        ##end
        """
        output = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, output, 278))
    def test_279(self):
        input = """func main()
        ##begin 
        end
        """
        output = "Error on line 3 col 8: end"
        self.assertTrue(TestParser.test(input, output, 279))
    def test_280(self):
        input = """func main()
        begin ##test if without expr behind
            if continue continue
            else return 1
        end
        """
        output = "Error on line 3 col 15: continue"
        self.assertTrue(TestParser.test(input, output, 280))
    def test_281(self):
        input = """func main()
        begin ##test if without expr behind
            if else return 1
        end
        """
        output = "Error on line 3 col 15: else"
        self.assertTrue(TestParser.test(input, output, 281))
    def test_282(self):
        input = """func main()
        begin ##test if without expr behind
            if a return 1
            else if b return 2

            return 0
        end

        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 282))
    def test_283(self):
        input = """func main()
        begin 
        if a = b ##test if without block stmt
            a <- b + 1
            continue
        else
            return 0
        end
        """
        output = "Error on line 6 col 8: else"
        self.assertTrue(TestParser.test(input, output, 283))
    def test_284(self):
        input = """func main()
        begin 
        if a = b 
            begin
                a <- b + 1
                continue
            end
        elif a > b
            begin
                if a - b = 4
                    begin
                        a <- b * 123.e45
                        return 1
                    end
                elif a - b = 3
                    return 2
                else return 3
            break
            end ## test break
        elif a + b = 10
            return 4
        else
            return 0
        end
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 284))
    def test_285(self):
        input = """func main(var i <- 0, var j <- 0) ## test func with var decl"""
        output = "Error on line 1 col 10: var"
        self.assertTrue(TestParser.test(input, output, 285))
    def test_286(self):
        input = """func main() begin 
        end"""
        ouput = "Error on line 2 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, ouput, 286))
    def test_287(self):
        input = """if a = b ## Statement must be in a block
            begin
            a <- b + 1
            continue
            end
        elif a > b
            if a - b = 4
                a <- b * 123.e45
                return 1
            elif a - b = 3
                return 2
            else return 3
        elif a + b = 10
            return \"string\"
        else
            return 0
        """
        ouput = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, ouput, 287))
    def test_288(self):
        input = """func main()
        begin break end ## end a statement is an \\n character"""
        ouput = "Error on line 2 col 14: break"
        self.assertTrue(TestParser.test(input, ouput, 288))
    def test_289(self):
        input = """func arithmeticSum(number a,number  d, number n)
    begin
    var sum <- 0
    var term <- a
    var i <- 0
    for i until i < n by 1
    begin
        sum <- sum + term
        term <- term + d
    end
    return sum
    end

func main()
    begin
    ## test comment
    var a <- 1
    var d <- 2
    var n <- 10
    var sum <- arithmeticSum(a, d, n)
    writeNumber(sum)
    end
    """
        ouput = "successful"
        self.assertTrue(TestParser.test(input, ouput, 289))
    def test_290(self):
        input = """func infiniteGeometricSum(number a, number r)
    begin
    if abs(r) < 1
        return a / (1 - r)
    return "The series does not converge."
    end

func main()
    begin
    var a <- 1
    var r <- 0.5
    var sum <- infiniteGeometricSum(a, r)
    writeNumber(sum)
    end
        """
        ouput = "successful"
        self.assertTrue(TestParser.test(input, ouput, 290))
    def test_291(self):
        input = """func checkScores()
    begin
    number scores[10] <- [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
    var i <- 0
    for i until i < length(scores) by 1
    begin
        if scores[i] >= 90
        begin
            writeString(\"Student \" + (i+1) + \": Excellent\")
            continue
        end
        if scores[i] >= 80
        begin
            writeString(\"Student \" + (i+1) + \": Good\")
            continue
        end
        if scores[i] >= 70
        begin
            writeString(\"Student \" + (i+1) + \": Fair\")
            continue
        end
        writeString(\"Student \" + (i+1) + \": Average\")
    end
    end

func main()
    begin
    checkScores()
    end
        """
        ouput = "successful"
        self.assertTrue(TestParser.test(input, ouput, 291))
    def test_292(self):
        input = """func main(foo(),bar(),number a[15], bool b[20], string c[3],fooi(a)) return 1"""
        ouput = "Error on line 1 col 10: foo"
        self.assertTrue(TestParser.test(input, ouput, 292))
    def test_293(self):
        input = """func main(100e100) return 1"""
        ouput = "Error on line 1 col 10: 100e100"
        self.assertTrue(TestParser.test(input, ouput, 293))
    def test_294(self):
        input = """func main(\"\")"""
        ouput = "Error on line 1 col 10: "
        self.assertTrue(TestParser.test(input, ouput, 294))
    def test_295(self):
        input = """func return()"""
        ouput = "Error on line 1 col 5: return"
        self.assertTrue(TestParser.test(input, ouput, 295))
    def test_296(self):
        input = """func foo()
        begin
        begin
        begin
        end
        begin
        end
        end
        end
        """
        ouput = "successful"
        self.assertTrue(TestParser.test(input, ouput, 296))
    def test_297(self):
        input = """func foo()
        begin
        dynamic i
        i <- readNumber()
        begin 
            if i > 0
                begin
                    if i % 2 == 0
                        begin 
                        if i % 3 == 0
                            begin
                            return 0
                            end
                        else break
                        end
                    else continue
                end
            else 
             begin
                begin
                return 1
                end
             end 
        end
        end
        """
        ouput = "successful"
        self.assertTrue(TestParser.test(input, ouput, 297))
    def test_298(self):
        input = """"""
        ouput = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, ouput, 298))
    def test_299(self):
        input = """func func()
        begin
        return 1
        end
        """
        ouput = "Error on line 1 col 5: func"
        self.assertTrue(TestParser.test(input, ouput, 299))
