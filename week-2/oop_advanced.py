# an Animal base class with a speak() method, and Dog and Cat subclasses that override speak() with their own sounds
# class animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#             print ("animal sound")


# class cat(animal):
#      def speak(self):
#           print(self.name , "meow")

# class dog (animal):
#      def speak(self):
#           print(self.name, "woof")

# cat1= cat("aaaaaa")
# dog1= dog("bbbbb")

# cat1.speak()
# dog1.speak()

from abc import ABC, abstractmethod
import math
class shape(ABC):
    def __init__(self):
        self.pi= 3.14

    @abstractmethod
    def area(self):
         pass
        


class rectangle(shape):
     def __init__(self, height, width):
          self.height =height
          self.width= width
          
     def area(self):
          return self.height * self.width
     
     def __str__(self):
          return f"rectangle value {self.height, self.width}"
          

class circle (shape):
     def __init__(self,radius):
          self.radius= radius

     def area(self):
          return math.pi * (self.radius ** 2)
     


c1= circle(5)
r1= rectangle(4,4)

print(c1.area())
print(r1.area())
print(r1)






