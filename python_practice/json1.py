#named another script json.py and it turns out it tried to load the
#custom json.py file as a module. dumps method is obviously not
#available there.
#Renaming the json.py script to something else (json2.py) got rid
#of the issue.

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
  json.dump(numbers, f_obj)

with open(filename) as file_obj:
    num=json.load(file_obj)

print(num)

#remembering names

filename='user.json'
try:
    with open(filename) as file_obj:
        username=json.load(file_obj)

except FileNotFoundError:
    username=input("Enter your name")
    with open(filename,'w') as file_obj:
        json.dump(username,file_obj)

    print("Apan tera naam agli baar yad rakhega ")

else:
    print("Hello, " + username.title() + "!" )



