class car:
    def __init__(self,company,model,color,price):
        self.company=company
        self.model=model
        self.color=color
        self.price=price

    def start_car(self):
        print("car from company",self.company,"having model",self.model,"has started")

    def stop_car(self):
        print("car from company", self.company, "having model", self.model, "has stoped")

    def get_car_details(self):
        print("company of the car ",self.company)
        print("model of the car ",self.model)
        print("color of the car ",self.color)
        print("price of the car ",self.price)

obj1=car("kia","honda","black","4500000")
obj1.start_car()
obj1.stop_car()
obj1.get_car_details()



