# write python program to get a string made of te first 2 and last 2 character from the given string.
# if the string length is less than 2, return instead of the empty string.

string = input("Enter a string:")
if len(string)<2:
        print()
else:
        print(string[:2] + string[-2:])

print()



