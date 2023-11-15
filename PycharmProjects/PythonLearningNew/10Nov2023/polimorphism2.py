#polimorphism by using function

def add(x,y,z=0):
    return x+y+z

print(add(1,2))
print(add(1,4,6))

#by using class and metod
class India:
    def Capital(self):
        print("Delhi is the capital of INDIA. ")

    def Language(self):
        print("Hind is the most widely spoken language of India.")

    def Type(self):
        print("India is developing country.")

class USA:
    def Capital(self):
        print("\nWashingtyone is the capital of USA.")

    def Language(self):
        print("English is the primary languge of USA.")

    def Type(self):
        print("USA is the developed country.")

#create instance of class
obj_ind=India()
obj_usa=USA()

#create for loop to iterate through tuple of objects
for country in (obj_ind,obj_usa):
    country.Capital()
    country.Language()
    country.Type()

#polymorphism with inheritance and method overriding
class Animal:
    def speak(self):
        #raise NotImplementedError("subclass must implemented this method.")
        return "speak"
class Dog(Animal):
    def speak(self):
        return "Bow bow"

class cat(Animal):
    def speak(self):
        return "meow meow"

# obj_animal=Animal()
# print(obj_animal.speak())
#
# obj_dog=Dog()
# print(obj_dog.speak())
#
# obj_cat=cat()
# print(obj_cat.speak())

#or create a list of animinal objects
animal = [Dog(),cat()]

#call the speak method on each object
for animals in animal:
    print(animals.speak())




