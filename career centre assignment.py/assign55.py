# write python function to calulate the factorial of a number (a non negative integer).


number=int(input("Enter your number :"))
f=1
for i in range(1,number+1):
    f*=i
    print(f)
