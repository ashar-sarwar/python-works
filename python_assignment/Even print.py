line=(input("enter a line"))       # we can also write >> line=list(input("enter a line"))
p=""
for even in line[::2]:
    p=p+even

print(p)
