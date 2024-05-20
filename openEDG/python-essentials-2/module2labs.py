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
        return line  

def paliOrNot(line):
    return line
              



#caesarCypher("The die is cast", 25)
#caesarCypherInput("Hello")