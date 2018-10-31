magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)

for value in range(1,5):
 print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

million=[value for value in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))