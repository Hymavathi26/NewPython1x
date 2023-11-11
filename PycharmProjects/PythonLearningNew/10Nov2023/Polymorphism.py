#polymorphism-->one base can have many form (oop)
#person()-->hyma,raj-->talk()--hyma can talk english and raj can talk telugu

class shape:
    def area(self):
        print("area of the shape")

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class circle(shape):
    def __init__(self,radies):
        self.radies=radies

    def area(self):
        return 3.14*self.radies*self.radies

shape1=rectangle(3,4)
print(shape1.area())

shape2=circle(5)
print(shape2.area())

shape3=shape
shape3.area(4)

