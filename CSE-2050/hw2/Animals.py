class Animal:
    def __init__ (self, name):
        self.name = name

    def speak (self):
        return f'{self.name} says Growl!'

    def reply (self):
        return self.speak()


class Mammal (Animal):
    def __init__ (self, name):
        super(Mammal, self).__init__(name)
        self.name = name

    def speak (self):
        return f'{self.name} says RAHHHH!'


class Cat (Mammal):
    def __init__ (self, name):
        super(Cat, self).__init__(name)
        self.name = name

    def speak (self):
        return f'{self.name} says Meow!'


class Dog (Mammal):
    def __init__ (self, name):
        super(Dog, self).__init__(name)
        self.name = name

    def speak (self):
        return f'{self.name} says Woof!'

class Primate (Mammal):
    def __init__ (self, name):
        super(Primate, self).__init__(name)
        self.name = name

    def speak (self):
        return f'{self.name} says Oooga Booga!'

class Computer_Scientist (Primate):
    def __init__ (self, name):
        super(Computer_Scientist, self).__init__(name)
        self.name = name



if __name__ == "__main__":
    test = Mammal('Mammal')
    test2 = Animal('Animal')
    test3 = Cat('Cat')
    test4 = Dog('Dog')
    test5 = Primate('Primate')
    test6 = Computer_Scientist('Computer Scientist')
    assert test.speak() == 'Mammal says RAHHHH!'
    assert test2.speak() == 'Animal says Growl!'
    assert test3.speak() == 'Cat says Meow!'
    assert test4.speak() == 'Dog says Woof!'
    assert test5.speak() == 'Primate says Oooga Booga!'
    assert test6.speak() == 'Computer Scientist says Oooga Booga!'