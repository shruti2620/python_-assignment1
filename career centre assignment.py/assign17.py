# write python function to reverse a string if its length is multiple of 4.

string = input("Enter a string :")
if len(string)%4 ==0:
        print(string[0:-1])
else:
        print(string)

