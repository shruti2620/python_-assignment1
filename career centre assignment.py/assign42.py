# how will you create a dictionary using tuple in python.
 
"Method 1"
tuple_list= (('a',1),('b',2),('c',3),('d',4))
dictionary=dict(tuple_list)
print(dictionary)

"Method 2"
# using with key value pair

keys=('a','b','c')
value=0

dictionary={key: value for key in keys}
print(dictionary)