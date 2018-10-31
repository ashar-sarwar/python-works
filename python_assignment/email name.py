a=list(input())
b=[]

for char in a:
    if(char=='@'):
      break

    else:
        b.append(char)

d="".join(b)
print(d)