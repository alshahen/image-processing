fruits = [ "apple" , "banana" , "cherry" ]
print(fruits)
# Output: ['apple', 'banana', 'cherry']
print(fruits[ 0 ])
# Output: apple
#print from 1 to 3
fruits = [ "apple" , "banana" , "cherry" , "lemon" , "grape" ]
print(fruits[ 0 : 3 ])
# Output : ['apple', 'banana', 'cherry']
# start from index 0 to n-1
#add new element to list
fruits.append( "orange" )
print(fruits)
# Output: ['apple', 'banana', 'cherry', 'orange']
#remove element from list
fruits.pop( 1 )
print(fruits)
# Output: ['apple', 'cherry', 'orange']
#nested list
fruits = [
"apple" ,
"banana" ,
[ "cherry" ],
[ "lemon" , "grape" ]
]
print(fruits)
# Outputs: ['apple', 'banana', ['cherry'], ['lemon', 'grape']]
#add new element to nested list
fruits[ 2 ].append( "orange" )
print(fruits)
# Output: ['apple', 'banana', ['cherry', 'orange'], ['lemon', 'grape']]
#remove element from nested list
fruits[ 3 ].pop( 1 )
print(fruits)
# Output: ['apple', 'banana', ['cherry', 'orange'], ['lemon']]