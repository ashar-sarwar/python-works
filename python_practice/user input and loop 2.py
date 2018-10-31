number=0

while number<10:
    number+=1
    if number%2==0:
        continue
    else:
        print(number)

#Moving Items from One List to Another

unconfirmed=['alice','henry','diego']
verified=[]

while unconfirmed:
    user=unconfirmed.pop()

    verified.append(user)

for user in verified:
    print(user)