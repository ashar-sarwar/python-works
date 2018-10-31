filename='prg.txt'
with open(filename,'w') as file_object:
    file_object.write("programming is love \n")
    file_object.write("tyt cheex hai programming \n")

#we should know that when we open file in 'w' mode,
# then pthon deletes that file and makes a new file fro scratch

# to avoid loosing the previous data on file, we use 'a' mode
#which allows both read and write

#we need to add \n because without it, python would write both
# statements in a single line
with open(filename) as file_object:
    line=file_object.read()

print(line)

