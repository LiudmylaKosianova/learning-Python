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

print("\n*** List comprehension ***\n")
squares = [x**2 for x in range(10)]
print(squares)
evens = [x for x in squares if x % 2 == 0]
print(evens)

#2D list: temperature measurements: every hour every day
temps = [ [0.0 for h in range(24)] for d in range(31)]

for d in range(31):
    print(temps[d])

#3D list: a hotel consists of 3 building, 15 floors each.
#         There are 20 rooms on each floor. Info is the room occupied/free

rooms = [[[False for r in range(20)]for f in range(15)]for t in range(3)]

for t in range(3):
    print("Tower", t, "\n")
    for f in range(15):
        print("Floor", f, "\n")
        print("\t", rooms[t][f])

"""
List comprehension:
[expression for element in list if condition]

Loop equivalent:
for element in list:
    if condition:
        expression
"""