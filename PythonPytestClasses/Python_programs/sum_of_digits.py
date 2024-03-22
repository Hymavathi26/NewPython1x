def sum_of_digit(number):
    sum=0
    for digit in number:
        sum=sum+int(digit)
    return sum
input_string=input("Enter number:\n")
result = sum_of_digit(input_string)
print("sum of digits :",result)

#sum of digits in a list
# list=[1,2,3,4,5]
# sum=0
# for digit in list:
#     sum=sum+int(digit)
# print("sum of digits in a list:",sum)

#using sum builtin function
# list1=[1,4,6,9,10]
# sum_list=sum(list1)
# print("Sum of digits in a list:",sum_list)


array=[1,2,3,4,5,]
print(sum(array))    #return 15
#if i want to update array
print(sum(array,10))       #return 25
#if minus 10 from array
print(sum(array,-10))       #return 5


#by using reduce

# from functools import reduce
# num_list=[20,30,40,50,70]
# SumOfList=reduce(lambda x,y:x+y,num_list)
# print("sum of all numbers in the list is",SumOfList)

