# how do you tranverse through a dictionary object in python.

dict={
         "name" : "shruti",
         "subject" : "python",
        "score" : 89
      }

print(dict)

# to loop for only keys 
for key in dict:
    print(key)

for key in dict.keys():
    print(key)

# to loop for only values 
for value in dict.values():
    print(value)

# to loop for both key and values
for key,value in dict.items():
    print("key:",key,"value:",value)

