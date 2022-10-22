# class Person:
#     def __init__(self, name):         Constructor anashei
#         self.name = name

#     def talk(self):
#         print(f"I'm talking, and my name is {self.name}")


# p = Person("Juan de boca")
# p.talk()

# b = Person("Bob Smith")
# b.talk()


class Mammal:
    def walk(sekf):
        print("walk")


class Dog(Mammal):  # inheritance
    def bark(self):
        print("Woof")


class Cat(Mammal):
    def meow(self):
        print("Meow")


class Human(Mammal):
    pass  # nedeed for empty classes


d = Dog()
c = Cat()
h = Human()

d.bark()
d.walk()
c.meow()
h.walk()
