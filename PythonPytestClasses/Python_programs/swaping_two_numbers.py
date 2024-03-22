# can we store two values ina dict
# dict1 = {'name': ['hyma'], 'age': 26}
# print(dict1)
# dict1['name'].append("raju")
# print(dict1)
#
# # list compressions
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [x for x in list1 if x % 2 == 0]
# print('list1', list1)
# print('list2', list2)
#
# # what is lambda function
# # lambda is nothing but ananimas function that is passing any number
# # of arguments without afuncion name and it expresed in one line
# x = lambda a, b, c: a * b * c
# print(x(2, 3, 4))
#
# # swap between two numbers
# num1 = int(input("Enter num1 value:\n"))
# num2 = int(input("Enter num2 value:\n"))
#
# temp = num1
# num1 = num2
# num2 = temp
# # or we can use without temp variable also
#
# # num1,num2=num2,num1
# print(f'after swaping num1 value is {num1}')
# print(f'after swaping num2 value is {num2}')
#
# #Swaping first and last elements in a list by using temp varibale
# list=[10,30,20,50,70,60]
# size=len(list)       #6
#
# temp=list[0]
# list[0]=list[size-1]
# list[size-1]=temp
#
# print("after swaping first and last elemnet in a list",list)

# without using temp variable
mylist = [3, 5, 7, 8, 9, 10]
# size=len(mylist)
# print("before swaping mylsi values",mylist)
# # mylist[0],mylist[size-1]=mylist[size-1],mylist[0]
# #or
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print("after swaping list values",mylist)

# approach 3 :Using tuple
# get = (mylist[-1], mylist[0])  # return 10  3      #packing
# mylist[0], mylist[-1] = get  # Her list[0] is 10 and list[-1] is 3 from tuple
# print("list after swapingg",mylist)

# Approach 4:   using * operand
# mylist1 = [10, 20, 30, 40, 10, 60]
# start, *middle, end = mylist1
# print(start)              #start :print first variable in a list  10
# print(*middle)            #*middle: print all middle variables  20 30 40 10
# print(end)                #print last variable in a list : 60

# mylist1 = [end, *middle, start]  # swaping first and last elements in a list
# print("list after swaping", mylist1)

# approach5 : using pop() built in function
mylist1 = [10, 20, 30, 40,60]
first = mylist1.pop(0)  # delete 10
last = mylist1.pop(-1)  # delete 60

mylist1.insert(0,last)     #0 indext ,last variable :Last value stored in 0 index   ---inserting initial values
#mylist1.insert(4,first)    #insert last values   or append
mylist1.append(first)       #append values are added in th last in a list
print("list after swaping", mylist1)