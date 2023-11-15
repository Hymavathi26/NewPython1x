# #Abstractct method is does not have any implementation by susing subclass we can implemet
# #and we use one decorator before method @abstractormethod
#
# #Abstraction--HIding the details and showing what is required
# # #Do you know how tha engine is started and gear is managed
# # #hiding the implementation and show only the important details
# #
# # #ABC--Abstraction base class
# # #whenever we work with ABC, we import abstractmethod and ABC classes from abc module
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     # def __init__(self,name):
#     #     self.name=name
#
#     @abstractmethod         #This decorator indicates it is incomplete implementation
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#        return "Bow Bow"
#
# class Cat(Animal):
#     def sound(self):
#         return "meow meow"
#
# #animal=Animal()
# #("animal can speakl")
#
#  #dog=Dog()
# # print(dog.sound())
# #
#  #cat=Cat()
# # print(cat.sound())
#
# list_animal=[Dog(),Cat()]
# #iterate list of animals through looping
# for animals in list_animal :
#      print(animals.sound())
#
# Example2:
# create polygon by using abc--create subclass like triangle,pentgon,Hexagon and Quadrilateral
# Each of these dubclass overrides the "Side" method and provide its own implementation
# and priting the number of sides it has

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def Side(self):
        pass


class Triangle(Polygon):
    def Side(self):
        print("Triangle have three sides")


class Pentagon(Polygon):
    def Side(self):
        print("Pentagon have have 5 sides")


class Hexgon(Polygon):
    def Side(self):
        print("Hexgon have 6 sides")


class Quadrilateral(Polygon):
    # @abstractmethod
    def Side(self):
       print("Quadrilater have 4 sides")

# class Rectangle(Quadrilateral):
#     def Side_length(self):
#         print("Quadrilater have 4 sides")

triangle=Triangle()
triangle.Side()

pentagon=Pentagon()
pentagon.Side()

hexogon=Hexgon()
hexogon.Side()

quadrilater=Quadrilateral()
quadrilater.Side()

# rectangle=Rectangle()
# rectangle.Side_length()

#adding instances to a list here getting  error
# obj_Shapes = [triangle, pentagon, hexogon,rectangle]
#
# for shapes in obj_Shapes:
#     if isinstance(shapes,Polygon):
#         shapes.Side()
# else:
#      if isinstance(shapes,Quadrilateral):
#         shapes.Side_length()

