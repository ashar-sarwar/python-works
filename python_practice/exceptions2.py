def count(filename):

    try:

      with open(filename) as file_object:
        contents = file_object.read()

    except:
      print('file does not exist')

    else:
      words = contents.split()
      print("the file has " + str(len(words)) + " words in it")

filename=['alice.txt','prg.txt',r'C:\Users\Ashar Sarwar\Documents\Pandas.txt']
for file in filename:
    count(file)
