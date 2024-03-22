# lst1 = [1, 2, [3, 4, [5, 6, 7], 8], 10]
def list1(input_list):
    l=[]
    for i in input_list:
       #print(i,type(i))
       if type(i) is list:
           l.extend(list1(i))
       else:
           l.append(i)
    return l
lst1 = [1, 2, [3, 4, [5, 6, 7], 8], 10]
print(list1(lst1))










