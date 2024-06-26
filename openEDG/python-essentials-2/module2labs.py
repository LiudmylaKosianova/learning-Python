def mysplit(strng):
    #
    # put your code here
    #
    mylist = []
    if len(strng) == 0 or strng.isspace():
        return mylist
    #print(f"strng length: {len(strng)}")
    strng = strng.strip()
    strng = strng + ' '
    listElement = ""
    #print(f"strng length: {len(strng)}")
    for char in strng:
        if char != ' ':
            listElement = listElement + char
        else:
            mylist.append(listElement)
            listElement = ""  
      
    return mylist

def ledInputCheck():
    digits = input("Enter a positive integer to display: ")
    if not digits.isdigit():
        print("Wrong input!")
        return -1
    digitsInt = int(digits)
    if digitsInt < 0:
        print("Wrong input!")
        return -1
    return digits

def ledDisplay(a):
    if a == -1: return
    n0 = ["###", "# #", "# #", "# #", "###"]
    n1 = ["  #", "  #", "  #", "  #", "  #"]
    n2 = ["###", "  #", "###", "#  ", "###"]
    n3 = ["###", "  #", "###", "  #", "###"]
    n4 = ["# #", "# #", "###", "  #", "  #"]
    n5 = ["###", "#  ", "###", "  #", "###"]
    n6 = ["###", "#  ", "###", "# #", "###"]
    n7 = ["###", "  #", "  #", "  #", "  #"]
    n8 = ["###", "###", "###", "###", "###"]
    n9 = ["###", "# #", "###", "  #", "###"]
    ledN = []
    for lst in (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9):
        ledN.append(lst)

    # listInputDigits = []
    # for char in a:
    #     number = int(char)
    #     listInputDigits.append(number) 
    
    line = 0
    while line < 5:
        for char in a:
            digit = int(char)
            print(ledN[digit][line]," ", end="")
        line += 1
        print("")


#ledDisplay(ledInputCheck())

"""
Scenario

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case)
and all non-alphabetical characters should remain untouched.

Your task is to write a program which:
    - asks the user for one line of text to encrypt;
    - asks the user for a shift value (an integer number from the range 1..25 - note: 
      you should force the user to enter a valid shift value 
      (don't give up and don't let bad data fool you!)
    - prints out the encoded text.

    Test data
Sample input:

abcxyzABCxyz 123
2

Sample output:

cdezabCDEzab 123

Sample input:

The die is cast
25

Sample output:

Sgd chd hr bzrs
"""
def caesarLineInput():
    line = input("Enter the line: ")
    lineCheck = line.replace(' ','')
    if len(lineCheck) == 0:
        print("I can't cypher this line.")
        return -1
    return line

def caesarCypherInput(line):
    if line == -1: return -1    
    mistake = True
    while mistake:
        try:
            cypher = input("Enter the cypher number from the range 1..25: ")
            cypherInt = int(cypher)
            mistake = cypherInt < 1 or cypherInt > 25
        except:
            print("This is not an integer number")
            mistake = True
    print(f"Thank you, I will take the cypher \"{cypherInt}\" and incrypt \"{line}\"")
    return cypherInt

def caesarCypher(line, cypher):
    if line == -1: return -1
    lineList = line.split()
    print(lineList)
    elementC = ""
    lineListC = []
    for element in lineList:
        for char in element:
            if char.isalpha():
                charC = ord(char) + cypher
                if ord(char)<=90 and charC > 90:
                    charC = 65 + (charC-91)
                elif ord(char)<=122 and charC > 122:
                    charC = 97 + (charC-123)
                elementC += chr(charC)
                #elementC += (str(charC))+"*"
            else:
                elementC += char
        lineListC.append(elementC)
        elementC = ""
    cc = " ".join(lineListC)
    return cc

def paliInput():
    line = input("Enter a line: ")
    line = line.replace(' ','')
    if len(line)==0:
        return -1
    else:
        return line.lower() 

def paliOrNot(line):
    listOriginal = list(line)
    listReversed = listOriginal[::-1]
    if listOriginal == listReversed:
        print("It's a palindrome")
        return True
    else:
        print("It's not a palindrome")
        return False
    
def paliOrNot2(line):
    lineReversed = ""
    for i in range(len(line)-1,-1,-1):
        lineReversed += line[i]
    return line == lineReversed

"""
Scenario
An anagram is a new word formed by rearranging the letters of a word, 
using all the original letters exactly once. For example, 
the phrases "rail safety" and "fairy tales" are anagrams, 
while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent

"""
def createDi(line):
    line = line.replace(' ','')
    line = line.lower()
    di = {}
    for char in line:
        if char not in di:
            di[char] = 1
        else:
            di[char] +=1
    return di

def anagrams(line1, line2):
    
    di1 = createDi(line1)
    di2 = createDi(line2)
    if not di1 or not di2:
        return False
    else:
        return di1 == di2

"""
Scenario
Some say that the Digit of Life is a digit evaluated using somebody's birthday. 
It's simple - you just need to sum all the digits of the date. 
If the result contains more than one digit, 
you have to repeat the addition until you get exactly one digit. 
For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.
"""
def digit(birthdate):
    digit = 0
    for char in birthdate:
        digit += int(char)
    while digit > 9:
        strDigit = str(digit)
        digit = 0
        for char in strDigit:
            digit += int(char)
    return digit


"""
Scenario
Let's play a game. 
We will give you two strings: 
one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no 
(as there are neither the letters "d", "o", or "g", in this order)
"""

def hidden(word, combo):
    
    for char in word:
        if char not in combo:
            return "no"
        
    firstLetter = combo.index(word[0])
    tail = combo[firstLetter:]
    for char in word:
        if char in tail:
            tail = tail[tail.index(char):]
        else:
            return "no"
    return "yes"        
     
"""
Scenario
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. 
The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") 
of the table must contain all digits from 0 to 9.


Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits 
(check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
"""
def lineIsValid(line):
    #line should be sudoku valid
    rowList = list(line)
    rowList.sort()
    digitList = [str(x) for x in range(1,10,1)]     
    return rowList == digitList

def inputIsValid(input):
    #input should be a string containing only digits from '1' to '9'
    if len(input) != 9 or not input.isdigit():
        return False
    return True

def boardIsSudoku(board):
    #board is a list of nine strings
    sudoku = True
    for row in board:
        if not lineIsValid(row):
            return False    
    
    for i in range(9):
        column = ""
        for j in range(9):
            column += board[j][i]
        if not lineIsValid(column):
            return False
    
    miniBoards = []
    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(3):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""

    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(3,6,1):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""
    miniBoard = ""
    count = 0
    for i in range(9):
        for j in range(6,9,1):
            miniBoard += board[i][j]
            count += 1
            if count == 9:
                miniBoards.append(miniBoard)
                count = 0
                miniBoard = ""
    
    for line in miniBoards:
        if not lineIsValid(line):
            return False
    return True
    
print(boardIsSudoku(["295743861",
                          "431865927", 
                          "876192543", 
                          "387459216",
                          "612387495",
                          "549216738",
                          "763524189",
                          "928671354",
                          "154938672"]))

"""
The function should:

accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
if the user enters a string that is not an integer value, 
the function should emit the message 
Error: wrong input, and ask the user to input the value again;

if the user enters a number which falls outside the specified range, 
the function should emit the message 
Error: the value is not within permitted range (min..max) and ask the user to input the value again;

if the input value is valid, return it as a result.
"""
    
def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    wrong = True
    while wrong:
        try:
            a = int(input(prompt))
            if a > min and a < max:
                return a
            else:
                raise Exception
        except ValueError:
            print("Wrong input")
        except:
            print(f"The value is not within permitted range ({min}..{max})")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)


 
        





    


