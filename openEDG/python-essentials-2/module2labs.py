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

def ledDisplay(a):
    n0 = ["###", "# #", "# #", "# #", "###"]
    n1 = ["  #", "  #", "  #", "  #", "  #"]
    n2 = ["###", "  #", "###", "#  ", "###"]
    n3 = ["###", "  #", "###", "  #", "###"]
    n4 = ["# #", "# #", "###", "  #", "  #"]
    n5 = ["###", "#  ", "###", "  #", "###"]
    n6 = ["###", "#  ", "###", "# #", "###"]
    n7 = ["###", "  #", "  #", "  #", "  #"]
    n8 = ["###", "###", "###", "###", "###"]
    n9 = ["###", "# #", "###", "  #", "  #"]
    
