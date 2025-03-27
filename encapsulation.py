class Car:
    def __init__(self, model, year, odometer, color):
        self.model = model
        self.year = year
        self._odometer = odometer # first level of protecting attributes, using _
        self.__color = color # next level of making attributes private, using __

    def describe_car(self):
        print(self.year, self.model)
    
    def read_odometer(self):
        print("Odometer:", self._odometer, "miles")
    
    def car_color(self):
        print("Color:", self.__color)

my_car = Car('Audi', 2022, 150000, "Black")

my_car.describe_car()
my_car.read_odometer()

my_car._odometer= 2000  #modify the value in car odometer
my_car.__color= "White" # this shows encapsulation, attributes can be edited inside the class
my_car.read_odometer()
my_car.car_color()

