# write te python programm that swap two numbers with temperary variable and without temperary variable

" using temperory variable"
a = 3   # initial value of a 
b = 6    # initial value of b 
c = a  # store value of a in c 
a = b   # assign value of b to a 
b = c  # assign value of c (original to a) to b 
print(a,b)   # output te swapped value of a and b

"without using temperory variable"
a = 3 
b = 9
b = b-a # substract a from b and store a result in b
a = a +b # add the new value of b to a 
b = a - b   # substract new value of b from a to get original value of a 
print(a,b)  # output the swapped value of a and b 