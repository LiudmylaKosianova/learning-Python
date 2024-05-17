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


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
