# write python program to read last n lines of file.

f = open(f"myfile2.txt","r")

num_line=int(input("Enter your number :"))

for i in range(1,num_line-1):
    num_line-=1
    print(f.readline())