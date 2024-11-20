# write python program to find the second smallest number in a list.


number=[1,2,3,4,5,6,7,8,9,8,6,4,2]
sort = sorted(set(number))
if len(sort)>=2:
    second_smallest=sort[1]
    print(second_smallest)
else:
    print("list does not have unique element.")