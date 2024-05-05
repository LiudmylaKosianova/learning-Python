"""
reverse the elements in the list
"""

list1 = [1, 22, 3, 44]
length1 = len(list1)

print(list1)

for i in range(length1//2):
    list1[i], list1[length1-i-1] = list1[length1-i-1], list1[i]

print("Reversed list:\n", list1)