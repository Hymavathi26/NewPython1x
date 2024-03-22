def fabonacci_series(n):
    a, b = 0, 1
    if n < 0:
        print("Enter valid input")
    else:
        for i in range(2, n + 1):
            print(a, end=' ')
            a, b = b, a + b



number = int(input("Enter number:\n"))
fabonacci_series(number)




