"""
Counts the number of occurrences of the given element in the given list
"""
def howMany(list, element):
    if len(list) == 0: return 0
    count = 0
    for x in list:
        if x == element: count +=1
    return count

"""
Finds the max number in the given list.
If the list is empty, returns -1.
"""
def findMax(list):
    if len(list) == 0: return -1

    max = list[0]
    for x in list:
        if x > max: max = x
    return max

"""
Keeps track of every occurrence of the max number in the given list.
Returns a list that contains every occurrence of the max number.
Uses the findMax function.
If the list is empty, returns null.
"""

def maxList(list):
    if len(list) == 0: return None

    maxList = []
    maxNumber = findMax(list)
    for x in list:
        if x == maxNumber:
            maxList.append(x)
    return maxList

"""
Puts all of the zeros in the given array, at the end of the given list.
Updates the list itself.
Maintains the order of the non-zeros.
     
Example(s):
     * For a defined list {0, 1, 0, 2, 0, 3, 0, 5};
     * Calling swapZero(list) would change the list to be: {1, 2, 3, 5, 0, 0, 0, 0};
"""
def swapZero(list):
    lenList = len(list)
    if lenList == 0: return list

    zeros = howMany(list, 0)
    if zeros == 0: return list  
    
    #add zeros at the end
    for x in range(zeros):
        list.append(0)
    
    #delete the initial zeros
    count = 0
    for x in range(lenList):        
        if list[x] == 0:
            del list[x]
            count += 1
        if count == zeros:
            break        
        
    return list







