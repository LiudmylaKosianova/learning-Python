multipleLine = '''line n 1
line n 2'''
print(len(multipleLine))
a = 'a'
b = 'b'
a2 = a*2
ab = a + b
print(a, b, a2, ab)

# I can check the code of a character

char1 = 'F'
char2 = 'Ф' # Ukrainian character 
print(ord(char1))
print(ord(char2))

point1 = 70
point2 = 1060
print(chr(point1))
print(chr(point2))
print(chr(ord('F')) == 'F')

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

print('[' + 'gamma'.center(20, '*') + ']')

s1 = "Where are the snows of yesteryear?"
s2 = s1.split()
s3 = sorted(s2)
print(s3)