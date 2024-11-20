# write python script to concatenate following dictionaries to create a new one.

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict3={'e':5,'f':6}
dict4={'g':7,'h':8}

# concatenate dictionary
new_dict= {k: v for d in (dict1,dict2,dict3,dict4) for k,v in d.items()}
print(new_dict)