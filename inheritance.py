class Animals:
    def __init__(self, name):
        self.name = name
    def ability(self):
        print("move")

class Cat(Animals):
    def __init__(self, name, breed, age):
        super().__init__(name)#super is used if you like to add more attributes other than the attributes of the parent class
        self.breed = breed
        self.age = age
    def Meow(self):
        print("meow meow")
    def ability(self):
        super().ability()
        print("climb")
    
my_cat=Cat('Kuting', 'pinoy cat', 10)
#print(my_cat.name)
#print(my_cat.breed)
#print(my_cat.age)
#my_cat.ability()
#my_cat.Meow()

class Dog(Animals):
    def bark(self):
        print("WOf Wof")

my_dog=Dog("Raul")
#print(my_dog.name)
#my_dog.ability() #the dog inheret the animals baheviour
#my_dog.bark()

animals =[my_cat, my_dog]

for animal in animals:
    animal.ability()