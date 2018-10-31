with open('pi.txt') as file_object:
    contents=file_object.read()
    print(contents)
'''
with open('Documents\Pandas.txt') as file_object:
    contents=file_object.read()
    print(contents) #error because by this method it looks only inside
                    #the folder we are working now(pycharm projects)
'''


#Just put r before your normal string it converts normal
# string to raw string
filepath = r'C:\Users\Ashar Sarwar\Documents\Pandas.txt'
with open(filepath) as file_object:
    contents=file_object.read()
    print(contents)
'''
with open('pi.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#if we want to work outside th 'with open' scope we can do the
#following

with open('pi.txt') as file_object:
    lines=file_object.readlines()

for line in lines:
    print("yoyo")
    print(line.rstrip())
'''


