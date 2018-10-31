pizza=['bihari tikka','cheesomatic','afghani love']
friend_pizza=pizza[:]

pizza.append('double cheese')
friend_pizza.append('pepperoni')

print("My favorite pizzas are:")
for value in pizza:
    print(value)

print("My friend favorite pizzas are:")
for value in friend_pizza:
    print(value)
