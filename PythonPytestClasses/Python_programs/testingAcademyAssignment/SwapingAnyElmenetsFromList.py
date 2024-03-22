mylist = [10, 15, 50, 19, 90]  # index start from 0
print(mylist)
pos1, pos2 = 1, 3  # position1= 1 index and position2= 3 index
# mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]   #interchange the values using index
# print(mylist)


#Approx 2 : using pop()
first_ele=mylist.pop(pos1)   #15 delete
second_ele=mylist.pop(pos2-1)   #10 50 19 90
mylist.insert(pos1,second_ele)
mylist.insert(pos2,first_ele)
print(mylist)


