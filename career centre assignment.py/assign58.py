# write python function that check passed string is palindrome or not.

l1=["java","python","mom","pop","naman"]

l2=list(filter(lambda word: word==word[::-1],l1 ))
print(l2)