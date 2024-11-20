# write python program to check multiple keys exists in dictionary.

dict={
        "name" : 'shruti',
        "subject" : 'python',
        "score": 98

      }

key_check=["name","subject","score"]

if all(key in dict for key in key_check):
    print("all keys exixt in dictionary")
else:
    print("All key does not exist.")