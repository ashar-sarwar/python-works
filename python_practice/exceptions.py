
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
 first_number = input("\nFirst number: ")
 if first_number == 'q':
    break
 second_number = input("Second number: ")
 if second_number == 'q':
    break
 try:
    answer = int(first_number) / int(second_number)
 except ZeroDivisionError:
    print("You can't divide by 0!")
 else:
    print(answer)
#Handling the FileNotFoundError Exception

try:
    with open('alice.txt') as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print("File does'nt exists")

else:
    print(contents)

filename='alice.txt'

try:
    with open(filename) as file_object:
        contents=file_object.read()

except:
    print('file does not exist')

else:
    words=contents.split()
    print("the file has " + str(len(words)) + " words in it")





