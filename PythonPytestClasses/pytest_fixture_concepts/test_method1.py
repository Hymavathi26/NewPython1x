#Run a specific method before each test method in a class
import pytest


# class Test:
#
#     @pytest.fixture(scope="function",autouse=True)
#     def myfixture(self):
#         print("myfixture is called")
#
#     def test_method1(self):
#         print("method1 is called")
#
#     def test_method2(self):
#         print("method2 is called")

#Run a specific method before all the test method in a class
class Test:

    @pytest.fixture(scope='class',autouse=True)
    def myfixture1(self):
        print("myfixture1 is called")

    def test_method1(self):
        print("method1 is called")

    def test_method2(self):
        print("method2 is called")
