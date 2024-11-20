# write python program that takes two lists and returns true if they have atleast one common member.

def common_member(list1,list2):
    print(set(list1)&set(list2))

l1= [1,2,3]
l2= [3,4,5]
l3= [6,7,8]
print(common_member(l1,l2))
print(common_member(l2,l3))