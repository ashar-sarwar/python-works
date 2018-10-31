print("Give possible rabbits and chickens solution")
for chicken in range(1,36):
    for rabbit in range(1,36):
        if ((4*rabbit) + (2*chicken))==94  and  (rabbit+chicken)==35:
            print("\n" + "There are " + str(rabbit) + " rabbits and " + str(chicken) +" chickens")

