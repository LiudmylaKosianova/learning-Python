"""
Task: remove all the number repetitions from the list, the numbers should appear only once
"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#
# Write your code here.
#
twin_list = []
for element in my_list:
    if element not in twin_list:
        twin_list.append(element)
my_list = twin_list
print("The list with unique elements only:")
print(my_list)
