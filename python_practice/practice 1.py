#10-7
q=True
while(q==True):
 first=input("enter first number")
 second=input("Enter second number")

 try:
  answer=int(first)-int(second)

 except:
  print("You just entered a string.\nEnter again \n")

 else:
  print(answer)
  q=False

#10-10 common words

with open('edu.txt') as file_object:
    file=file_object.read()

print(file.lower().count('the'))

