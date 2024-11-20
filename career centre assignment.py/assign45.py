# write python script to check if a given key is already exists in a dictionary.

dict= {'a':1,'b':2,'c':3,'d':4}
key_check=input("Enter your key choice:")

# check if te key exist in the dictionary 
if key_check in dict:
    print(f"the key '{key_check}' exist in dictionary")
else:
    print(f"the key {key_check} does not exist in dictionary.")