
print("The formula is f(n)=f(n-1)+100, where f(0)=1 \n enter n=")

n=int(input())

a={}

a[0]=1


for number in range(1,n+1):
    a[number]=a[number-1]+100

print("Ans=",(a[number]))

