# write python programe to find the highest 3 values in dictionary.

dict= {'a':5,'b':25,'c':100,'d':200,'e':400,'f':500}

highest_value= sorted(dict.values(),reverse=(True))[:3]
print("highest 3 value:", highest_value)