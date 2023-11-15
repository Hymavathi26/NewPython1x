# #EX2:
#
# class MyClass:
#     def My_method(self,x):
#         print("my method1",x)
#
#     def My_method(self,x,y):
#         print("My_method2",x+y)
#
# obj_myclass=MyClass()
# obj_myclass.My_method(1,5)
# obj_myclass.My_method(3,7)
#
# #EX3:
#
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("welcome"+ " " +name )
#         else:
#             print("welcome")
#
# human=Human()
# human.sayhello()       #welcome
# human.sayhello("hyma")


# #EX4:
class Browser:
    def __init__(self,browser):
        self.browser=browser

    def  OpenBrowser(self,browser="Chrome"):
        print("write the code to open the browser",browser)

b=Browser("Firefox")
b.OpenBrowser()

