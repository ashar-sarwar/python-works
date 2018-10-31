filename='pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi=''
for line in lines:
    pi+=line.rstrip()

print(pi)
print(len(pi))

filename='pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi=''
for line in lines:
    pi+=line.strip()

print(pi)
print(len(pi))

print(pi[:20])

#is your birthday in pi?

filename='pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi=''
for line in lines:
    pi+=line.rstrip()

print(len(pi))

birthday=input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi:
    print("exists in 1st million digits of pi")

else:
    print("Does'nt exists in 1st million digits of pi")




