# simply
list1 = [1, 2, 4, 7, 9, 23, 6, 7, 78, 90, 23]
print('smallest element in the list is:',max(list1))
print("largest element in the list is:",min(list1))


# whenever we check large number need to check list should not empty
list=[12,13,4,5,67,89]
#check if the list is not empty
if list:
    max_number=max(list)
    print("largest num in the list",max_number)
else:
    print("List is empty")

#by using sort
mylist=[25,67,89,70,60,1,56,4]
mylist.sort()
print(mylist)
print('smallest number in the list is:',mylist[0])
print('largest number in the list is:',mylist[-1])

#find maximum and minimum number in arry
array=[1,2,3,4,50,12,40]
#imagin first value is the max
max=array[0]
n=len(array)          #to find total elements in a list
for i in range(1,n):
    if array[i]>max:
        max=array[i]
print("maximum value is:",max)



#min value
array=[1,2,3,4,50,12,40]
#imagine first value is the max
min=array[0]
n=len(array)          #to find total elements in a list
for i in range(1,n):
    if array[i]<min:
        min=array[i]
print("minimum value is:",min)

