# classes

numbers = [1,2,3]
# pascal naming convention for calling classes like Classes
# objects are the instance for a classes, since classes are used to create a blueprint for creating an object
class Point:
    def __int__(self, x, y):
        # self is a reference to the current object
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')

#point1 = Point("10", "20")
#print(point1.y)

#a constructor is a function called at the point of creating an object point1.x = 10 point1.y = 20 print(point1.x) point1.draw()

class Person:
      def __init__(self, name, x):
          self.name = name
          self.x = x
          # THE FUNCTION IS A METHOD
      def talk(self):
          print(f'my name is {self.name}')
john = Person("john smith",22)
print(john.talk())
#note that each object is an instance to the person class

# inheritance --- is used to limit code
class Mammal:
      def walk(self):
          print('dog')
class Cat(Mammal):
      pass
class Dog(Mammal):
      pass
dog1 = Dog()
print(dog1.walk())

