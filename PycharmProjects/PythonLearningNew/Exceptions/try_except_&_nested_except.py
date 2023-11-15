try:
    num1=int(input("Enter a number:\n"))
    num2=int(input("Enter a number2:\n"))
    result=num1/num2
except ValueError:         #if i try to give string like "hyma" is invalid input
    print("Invalid input")

except ZeroDivisionError:
    print("num2 is zero")
else:
    print(f'result is {result}')
finally:           #The finally block is always executed, performing cleanup tasks.
    print("I will be always executed")
