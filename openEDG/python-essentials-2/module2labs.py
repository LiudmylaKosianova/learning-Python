def mysplit(strng):
    #
    # put your code here
    #
    mylist = []
    if len(strng) == 0 or strng.isspace():
        return mylist
    
    listElement = ""
    for char in strng:
        if char != 32:
            listElement =listElement + char
        else:
            mylist.append(listElement)
            listElement = ""
    return mylist
        

    
        


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
