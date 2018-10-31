#9-4 number served .....page 204 of pdf

class hotel():
    def __init__(self,name,cuisine):
        self.name=name
        self.khappa=cuisine
        self.number_served=0

    def describe_hotel(self):
        print("jani hotel chicken hai ")
        print("bohut baap intazam hai idhar ko")

    def open_hotel(self):
        print("jani hotel khula hai")

    def set_number_served(self,serve):
        self.number_served=serve

    def inc_number_served(self,served):
        self.number_served+=served

    def served(self):
        print("Customer served: " + str(self.number_served))


scene=hotel("Darbar","karahi")
scene.set_number_served(10)
scene.served()
scene.inc_number_served(20)
scene.served()
