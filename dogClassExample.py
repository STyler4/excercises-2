class Dog:
    def __init__(self, name, age, colour):  # Method called whenever we create a new dog instance
        self.name = name
        self.age = age
        self.colour = colour
        print(name)

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age


# creating different dog objects
dog1 = Dog(name="Spot", age="7", colour="black")
dog2 = Dog(name="Jazz", age="5", colour="white")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(17)
dog2.change_age(9)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
