class  Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def bark(self):
        print("Dogs bark")
d=Dog()
d.sound()
d.bark()