from collections import Counter

def count_characters(Input_string):
    #using counter to ciunt the eac characters in th estring
    occurances=Counter(Input_string)
    #Display the result
    for char, count in occurances.items():
        print(f'{char}: {count} occurance')

Input_string=input("Enter string: \n")
#call the function
count_characters(Input_string)
print("Length of input string is :",len(Input_string))

