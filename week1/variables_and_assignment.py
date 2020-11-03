# Integer
a = 2
print(a)
# Output: 2
# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)
# Output: None
a, b, c = 1 , 2 , 3
print(a, b, c)
# Output: 1 2 3
a = b = c = 1 # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1
b = 2 # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1 # so output is as expected.