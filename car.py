class Car():
    def __init__(self):
        self.colour = "purple"
        self.brand = "VW"
        self.hight = "2.5m"
        self.length = "5m"
        self.width = "3m"

    def drive(self):
        print("The",self.colour,"car is driving very fast!")
    def brake(self):
        print("The",self.colour,"car has slowed to a stop!")
    def honk(self):
        print("The",self.colour,"car has honked the horn very loudly!")

car1 = Car()
car1.drive()
car1.honk()
car1.brake()

#create a blueprint for a dog (funtions and propaties)