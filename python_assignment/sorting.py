from audioop import reverse
from operator import itemgetter
list = []
print("You can enter information about 3 people only")


for p in range(1,4):

    s = input("Enter name, age,height=")
    if not s:
        continue
    else:
        list.append(tuple(s.split(",")))

print (sorted(list, key=itemgetter(0,1,2)))
