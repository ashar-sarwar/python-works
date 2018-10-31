#This method has two leading underscores and two trailing underscores,
#a convention that helps prevent Python’s default method names
#from conflicting with your method names.

#Every method call associated with a class automatically passes self, which
#is a reference to the instance itself; it gives the individual instance access to
#the attributes and methods in the class.

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title() + " is sitting")

    def roll(self):
        print(self.name.title() + " is rolling")


my_dog=Dog("willie",10)
your_dog=Dog("tommy",7)

print("My dog name is " + my_dog.name.title())
print("Your dog's name is "+ your_dog.name.title())
print("\n")
my_dog.sit()
your_dog.roll()

class hotel():
    def __init__(self,namee,cuisine):
        self.name=namee
        self.khappa=cuisine

    def describe_hotel(self):
        print("jani hotel chicken hai ")
        print("bohut baap intazam hai idhar ko")

    def open_hotel(self):
        print("jani hotel khula hai")


my_hotel=hotel("queta sadaqat", "anda paratha")
print(my_hotel.name + " " + my_hotel.khappa)
my_hotel.describe_hotel()
my_hotel.open_hotel()

