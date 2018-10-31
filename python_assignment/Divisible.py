def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i = i + 1
        if j%7==0:

            yield j;

for i in putNumbers(100):
    print (i)

'''def createGenerator():
   mylist = range(3)
   for i in mylist:
       yield i*i

mygenerator = createGenerator() 
for i in mygenerator:
     print(i)'''