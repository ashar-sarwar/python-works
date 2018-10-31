



def print_design(uncomplete,complete):
    while uncomplete:
      design=uncomplete.pop()
      print("Printing " + design)
      complete.append(design)


def show_design(complete):
    print("The following are models stored")
    for completes in complete:
        print(completes)


uncomplete=['maths','eng','chem']
complete=[]

print_design(uncomplete[:],complete)    # if we want to keep the original list intact then we call this way
show_design(complete)                # in this way no changes will be there in the original list

print("\n")
def pizza(*topping):                                # this way we can add as many elemets as possible
    print("Making pizza with following toppings\n") # this method allows us to pack elements in tuple even if
    for toppings in topping:                        # you pass only 1 element
        print("-" + toppings)


pizza('bihari tikka')
print("\n")
pizza('pepperoni','cheese delight','fajita sensation')


print("\n")

def user(first, last , **user_info):
    profile={}
    profile['first']=first
    profile['second']=last
    for key,value in user_info.items():
        profile[key]=value

    return profile

info=user('albert', 'einstein', location='princeton',field='physics')
print(info)

