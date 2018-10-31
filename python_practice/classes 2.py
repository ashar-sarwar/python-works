class Car():
    def __init__(self,model,name,year):
        self.name=name
        self.model=model
        self.year=year
        self.odo_reading=0

    def info(self):
        print(str(self.year) + " " + self.name.title() + " " + self.model )
        print("My car has ran about " + str(self.odo_reading) + " miles")


my_car=Car("VXLi","suzuki cultus", 2008)
my_car.odo_reading=94
my_car.info()