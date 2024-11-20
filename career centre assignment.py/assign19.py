# write python function to insert a string in the middle of the string.

string= input("Enter a string :")
string_insert = input("Enter string to insert :")
middle_index=len(string)//2
result=string[:middle_index] + string_insert + string[middle_index:]

print(string[:middle_index] +" "+ string_insert +" " + string[middle_index:])

