# write python script to sort (ascending or descending) a dictionary by value.

sample_dict = {'apple':1,'mango':5,'banana':8,'watermelon':6}

# sort dictionary by values in ascending order 
ascending_dict= dict(sorted(sample_dict.items(),key=lambda item: item[1]))
print("ascending order:", ascending_dict)

# sort dictionary by values in descending order 
descending_dict=dict(sorted(sample_dict.items(),key=lambda item: item[1],reverse=True) )
print("descending order:",descending_dict)