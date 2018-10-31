#from classes import hotel                   #we must do the import stuff at start else the whole model is executed
                                            #in accordance to the calling of functions or whatever other stuff was
class Car():                                # done there

 def __init__(self, make, model, year):
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0

 def get_descriptive_name(self):
  long_name = str(self.year) + ' ' + self.make + ' ' + self.model
  return long_name.title()

 def read_odometer(self):
  print("This car has " + str(self.odometer_reading) + " miles on it.")

 def update_odometer(self, mileage):
  if mileage >= self.odometer_reading:
   self.odometer_reading = mileage
  else:
   print("You can't roll back an odometer!")

 def increment_odometer(self, miles):
  self.odometer_reading += miles


class electric(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=354

    def battery_time(self):
        print("Battery is of " + str(self.battery) + "KWH")

my=electric("tesla","AK47",2017)
print(my.get_descriptive_name())
my.battery_time()

#  attributes and methods can not be of same name as I had earlier
# named the function battery but didnt work because i already had
# an attribute with that name  --> Type error: 'int' object is not callable

class user():
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def describe(self):
        print("first:" + self.first + "\n" + "last:" + self.last )

    def greet(self):
        print("Aur jani kesa hai")

class admin(user):
    def __init__(self,first,last):
        super().__init__(first,last)
        self.privileges=["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for bahram in  self.privileges:
            print(bahram)


jani=admin("apu","khote")
jani.show_privileges()
jani.describe()


print("\n")

#bakchodi=hotel("queta baloch chai"," paratha chole")
#b(akchodi.describe_hotel()

#in order to import every class from module write:
# from module_name import*