# write python program to append text to a file and display the text.


f = open("name.txt","a")
for i in range(1,6):
    name = input("Enter your name :")
    subject = input("Enter your subject :")
    score=int(input("Enter you score :"))
    f.write("\n Name = "+name+" your score is :"+str(score) )

f.close()