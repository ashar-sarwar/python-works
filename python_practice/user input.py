height = input("How tall are you, in inches? ")
height = int(height)    #typecasting because pyhon interpretes the input as string so we need to convert it
if height >= 36:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")

print("\n")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message=""
while message!='quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

print("\n")

active=True

while active:
    message=input(prompt)

    if message=='quit':
        active=False

    else:
        print(message)




