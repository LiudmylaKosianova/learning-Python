"""
reverse the elements in the list
"""

list1 = [1, 2, 3, 4, 5, 6]
length1 = len(list1)

print(list1)

for i in range(length1//2):
    list1[i], list1[length1-i-1] = list1[length1-i-1], list1[i]

print("Reversed list:")
print(list1)
#list.reverse()

"""
Bubble sort. O(n^2).
"""
print("\n* * * Bubble sort * * *\n")
print("List to be sorted:")
print(list1)
flag = True

while flag:
    flag = False
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            flag = True

print("Sorted with Bubble sort")
print(list1)
#list.sort()

print("\n*** slice ***\n")
blueBells = [1, 21, 5, 14, 10]
print(blueBells, " blueBells")
#newBlueBells = blueBells[1:-1]
#newBlueBells = blueBells[:-1]
#newBlueBells = blueBells[1:]
newBlueBells = blueBells[:]
print(newBlueBells, " newBlueBells")
#del newBlueBells
del newBlueBells[1:3]
#del newBlueBells[:]
print(newBlueBells)
print(21 in newBlueBells)
print(21 not in newBlueBells)