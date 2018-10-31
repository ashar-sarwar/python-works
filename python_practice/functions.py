def greet_user(username):

 print("Hello, " + username.title() + "!")

greet_user('jesse')

def des_animal(type,name):
    print("The animal is " + type + " and we call it " + name + "." )

des_animal('dog','charlie')
des_animal(type='cat',name='micky') #another way of calling
des_animal(name='vicky',type='cat') # correct because python knows where the values belong

print("\n")

def info(first,last):
  full=first + " " + last
  return full

message=info('ashar','sarwar')
print(message.title())

print("\n")

def build_person(first_name, last_name, age=''):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 if age:
  person['age'] = age
 return person

musician = build_person('jimi', 'hendrix',27)
print(musician)



def myname(first,last):
    fullname=first + last
    return fullname.title()

while True:
    print("Naam bata")
    print("q daba kalti hone k liye")

    f_name=input("enter first name")
    if f_name=='q':
     break
    l_name=input("enter second name")
    if l_name=='q':
     break

    formatted=myname(f_name,l_name)
    print(formatted)

print("\n")

def greet(users):
    for user in users:                           # list elements are now in users and we get it by
     msg="hello " + user.title() + " !"          # executing a loop
     print(msg)

username=['ana','peter','cameron']    # here we pass a list to the function
greet(username)