# write python program to count the number of string where the string length is 2 or more and 
# the first and last character are same from the given list in string.

strings = ['121','abc','xyz','123','cba']
count = 0 
for s in strings:
    if len(s)>=2 and s[0]==s[-1] :
            count+=1
           
print("count of string with length 2 or more and same first and last character :",count)
