def get_day_type(day):
    weedays=["Monday","Tuesday","Wedneday","Thursday","Friday"]
    weekends=["Saturday","Sunday"]

    try:
        if day in weedays:
            print(f'{day} in weekdays')
        elif day in weekends:
            print(f'{day} in weekends')
        else:
            #raise ValueError("invalid day entered, plz entered valid day")
            print("invalid day entered, plz entered valid day")
    except ValueError as e:
        print(e)

user_input=input("Enter a day of the week:\n")
user_input=user_input.title()

get_day_type(user_input)

#instead of namedtuple we can use class methods to implemet program

class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name,self.age,self.gender})")



person2 = Person2("Pramod", 23, "M")
person2.print_details()


#we can execute main functionn by using below code
def this_is_main_func_as_per_python_now():
    print("Hello from main")


if __name__ == "__main__":        #this line to exe code
    this_is_main_func_as_per_python_now()