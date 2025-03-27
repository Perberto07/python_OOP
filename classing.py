class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def honk(self):
            print("honk honk")


my_car = Car('Honda', 'Black')

#print(my_car.brand)
#print(my_car.color)
#my_car.honk()

def greet():
     print("Welcome".upper())
     
prices = [55,68,70]
x=5
city="london"
is_open =True

print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))