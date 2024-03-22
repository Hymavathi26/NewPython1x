# class animal:
#     def animal_fun(self):
#         print("call animal function")
#
# class dog(animal):
#     def dog_fun(self):
#         print("call dog function")
#
# Dog=dog()
# Dog.animal_fun()
# Dog.dog_fun()


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def get_species_details(self):
        print(self.name+ "is a "+self.species)

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(name,'dog')
        self.name=name
        self.breed=breed
    def get_breed_details(self):
        print(self.name+ "belongs to" +self.breed)

dog=Dog("tommy","Buldog")




