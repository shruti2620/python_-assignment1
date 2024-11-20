# write the python programm to get te fibonacci series from the range 

num = int(input("Enter a number :"))
f=0
s=1
print(f"{f} {s}",end=" ") 
for i in range(2,num):
    t = f + s 
    f = s
    s = t 
    print(f"{t}",end=" ")