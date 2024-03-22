# # 5!=1*2*3*4*5=120
#
# factorial=1
# num=5
# if num<0:
#     print("Factorial does not exit for neative numbers")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:     #here we need find factorial of given number
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f'factorial of {num} is : {factorial}')
#
# #python recurssive approach
# #5*(5-1)*(4-1)*(3-1)*(2-1)=120----it looks descend order
# # 5 * 4 * 3 * 2 * 1 * = 120
# def factorial(n):
#     if (n==0) or (n==1):
#         return 1
#     else:
#         return n * factorial(n-1)  #5 * 4 * 3 * 2 * 1
#
# num = 5
# print("factorial of", num,"is",factorial(num))
#
# #Ternary operator With recurssive
# def factorial(n):
#     return 1 if (n==0 or n==1) else n*factorial(n-1)
#
# num = 5
# print("factorial of", num,"is",factorial(num))
#
#
# #By using function
# def factorial(num):
#     result=1
#     if num<0:
#         print("invalid input")
#     elif num==0:
#         print("factorial of  zero is always one")
#     else:
#         for i in range(1,num+1):
#             result*=i
#         print("factorial of number is :",result)
#     return result
# number=int(input("Enter number"))
# result=factorial(number)
# print(f'factorial of {number} is : {result}')
#
#
#
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
number=int(input("Enter number"))
print("factorial is:",fact(number))

