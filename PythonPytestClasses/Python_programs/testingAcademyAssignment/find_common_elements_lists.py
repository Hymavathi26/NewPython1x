list1=["hyma","raj","chaitra","paru"]
list2=["raj","prabha","sree","ricky"]
# Find the common elements using set intersection
combination_of_lists=set(list1) & set(list2)
print("common string in lists",combination_of_lists)

#by using function
def common_string_in_lists(list1,list2):
#convert list into set for efficient intersetion check
        set1=set(list1)
        set2=set(list2)
        return bool(set1.intersection(set2))

list1=[1,2,3,4,5]
list2=[10,11,7,8,9]
common_elements=common_string_in_lists(list1,list2)
print("list has atleast one common elements",common_elements)