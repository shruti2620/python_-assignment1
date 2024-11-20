# write python programm to get the factorial number of given numbers


num = int(input("Enter your number :")) 
f=1
for i in range(1,num+1):
    f*=i
    print(f)