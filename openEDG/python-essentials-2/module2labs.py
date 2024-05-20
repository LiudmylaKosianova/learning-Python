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
def ceasarInputLine():
    line = input("Enter the line: ")
    lineCheck = line.replace(' ','')
    if (len(lineCheck) == 0) or (not lineCheck.isalpha):
        print("I can't cypher this line.")
        return -1
    return line