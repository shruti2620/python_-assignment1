# write python program to combine values in python list of dictionary.

data=[
        {'item' : 'item1' , 'amount' : 400},
        {'item' :  'item2', 'amount': 300},
        {'item' : 'item1' , 'amount': 750} 
      ]

combined_data={}

for entry in data:
    item=entry['item']
    amount=entry['amount']

if item in combined_data:
    combined_data[item] += amount
else:
    combined_data[item] = amount

print("Combined data:", combined_data)







