# how can you get random number in python.

"method 1"

import random 
l1=[10,2,34,56,7,89,76,65]
random_integer=random.choice(l1)
print(random_integer)

"method 2"

import random 

random_integer=random.randint(1,50)
print(random_integer)