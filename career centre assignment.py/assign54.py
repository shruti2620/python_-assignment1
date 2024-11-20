# wite python program to create a dictionary from a string.

data_string= "a:1, b:2, c:3, d:4,e:5, f:6"

# split the string by comma to seperate key value pair 
key_value_pair= data_string.split(",")

# create the new dict by splitting each key value pair by colon 
final_dict= {pair.split(":")[0]:int(pair.split(":")[1]) for pair in key_value_pair}

print(final_dict)