print("enter number")
n=int(input())
number=0
for num in range(1,n+1):
    a=num+1
    number=(num/a)+number

print(float(number))