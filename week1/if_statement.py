a = 33
b = 200
if b > a:
    print( "b is greater than a" )
# multi-line indentation
if b > a:
    print( "b is greater than a" )
    b = b - 100
    a = a + 100
    print(a)
    print(b)
# use or , and
a = 33
b = 200
if b > a and a < 100 :
    print( "b is greater than a and a less than 100" )
# else
a = 33
b = 200
if b < a:
    print( "a is greater than b" )
else:
    print( "a is less than b" )