num=int(input("Enter number:\n"))
count = 0
if num<0:
    print("enter valid input")
else:
    for i in range(1,num+1):
        if num%i==0:
            count+=1
if count == 2:
    print("Number is prime")
else:
    print("Number is not prime")

# find given umber is prime or not
# 1.given number should (greaterthan) > 1
# 2.the num which has only two factors --1 and itself number
# num = 5
# count = 0
# if num > 1:
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1        #counting factors of number
#     if count==2:
#         print("Number is prime")
#     else:
#         print("Number is not prime")

# def prime_number(num):
#     count = 0
#     if number < 0:
#         print("invalid input")
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#     if count == 2:
#         print("prime number")
#
#     else:
#         print("not prime number")
#
# number = int(input("enter number"))
# prime_number(number)

#print 0 to 20 prime numbers
def is_prime(num):
    if num<2:
      return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
               return False
        return True
print("Prime numbers between 0 to 20")
for number in range(21):
    if is_prime(number):
        print(number)




