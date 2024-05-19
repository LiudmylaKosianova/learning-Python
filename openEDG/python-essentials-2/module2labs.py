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
