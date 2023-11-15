#factorial program:
def factorial(input_string):
    if input_string < 0:
        print("Invalid")
    else:
        factorial=1
        for i in range(1,input_string+1):
            factorial*=i
    print(f"Factorial of {input_string} is:{factorial}")
input_string=int(input("Enter number:\n"))
factorial(input_string)

#Fabinnacci
def fabonacci_series(Input_number):
    a,b=0,1
    if Input_number<0:
        print("Invalid inuput")
    else:
        for i in range(2,Input_number+1):
            print(a,end=" ")
            a,b=b,a+b      #0,1,1

Input_number=int(input("ENter number: \n"))
fabonacci_series(Input_number)
