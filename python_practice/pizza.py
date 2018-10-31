def make_pizza(*topping):                                # this way we can add as many elemets as possible
    print("Making pizza with following toppings\n") # this method allows us to pack elements in tuple even if
    for toppings in topping:                        # you pass only 1 element
        print("-" + toppings)

