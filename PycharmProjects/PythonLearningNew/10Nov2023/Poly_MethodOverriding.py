#Metod overriding--same func name in the parent and child class
#child always overide the parent methods
#super()--call my immediately parent function when both method names are same

class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal sound.")

class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound()
        print("Dog sound.")

# animal=Animal()   #create instance of class animal class
# animal.sound()
#
# dog=Dog()         #create instances of class for Dog class
# dog.sound()

# or by using super() we invoke parent methods from child

obj_dog=Dog()
obj_dog.sound()