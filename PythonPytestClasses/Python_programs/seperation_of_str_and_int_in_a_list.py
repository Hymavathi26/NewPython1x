names=[]
numbers=[]
input_list=[1,234,567,88993,"hymavathi","raju","chaitra",2356,45]
for i in input_list:
    if type(i) == str:
        names.append(i)
    elif type(i) == int:
        numbers.append(i)
print(f'seperation of names: {names}')
print(f'seperation of numbers:{numbers}')

#using function
def seperation_str_int_list(mixed_list):
    str_list=[]
    int_list=[]
    for i in mixed_list:
        if type(i)==str:
            str_list.append(i)
        elif type(i)==int:
            int_list.append(i)

    return str_list,int_list
mixed_list=[1,45,6,78,987,"hyma","raj","chaitra",456]
strings,integers=seperation_str_int_list(mixed_list)
print(f'seperation of string:{strings}')
print(f'seperation of integers:{integers}')


#search an element in a list
if "hymavathi" in input_list:
    print("hyma is present in the list")
else:
    print("hyma is not include in the list")

#Write a Python program to count the number of strings in a
# list where the string length is 2 or more and the first and last
#   characters are the same.
def count_valid_string(Input_string):
    count = 0
    for char in input_string:
        if len(char) >= 2 and char[0] == char[-1]:
            count += 1
    return count


input_string = ["radar", "level", "hyma", 'raj']
string_list = count_valid_string(input_string)
print(f"count valid string:{string_list}")

list=[1,2,3,4]
ele=3
if ele in list:
    print("Element in list")
else:
    print("Element not in list")



