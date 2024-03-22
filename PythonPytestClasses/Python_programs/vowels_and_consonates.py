# write a program to find given number is alphabet or not

# chr=input("Enter input character:\n")
# if "A"<=chr<="Z" or "a"<=chr<="z":
#     print(f'given number is alphabets')
# else:
#     print("Not alphabets")

# write program to find vowels in string
'''def found_vowels(input_string):
    vowels = "AEIOUaeiou"
    found_vowels = ""
    #found_vowels=[]
    for char in input_string:
        if char in vowels:
            found_vowels += char
            #found_vowels.append[char]
    return found_vowels

input_string = input("ENter a string:\n")
vowel_list = found_vowels(input_string)
print("found vowels in a string:", vowel_list, sep=" ")
#print(f"found vowels in a string:{','.join(vowel_list)}")

#count vowels in a string
def count_vowels(input_string):
    vowels="AEIOUaeiou"
    vowel_count=0
    for char in input_string:
        if char in vowels:
            vowel_count+=1
    return vowel_count
input_string=input("Enter a string:\n")
total_vowels=count_vowels(input_string)
print("count_of vowels in a string:",total_vowels)

to find vowels and consonates in a sting
def find_vowels_and_consonates(input_string):
    vowels="aeiouAEIOU"
    vowel_count=0
    consonate_count=0
    for char in input_string:
        if char in vowels:
            vowel_count+=1
        else:
            consonate_count+=1
    return vowel_count,consonate_count
input_string=input("Enter a string:\n")
vowels,consonates=find_vowels_and_consonates(input_string)
print(f"count of vowels :{vowels}")
print(f"count of consonates:{consonates}")'''

#remove voels in a string
input_string=input("Enter a string:\n")
vowels="AEIOUaeiou"
found_consonate=''
for char in input_string:
    if char.isalpha():
      if char  not in vowels:
         found_consonate+=char
print("consonates in a string are:",found_consonate)

#by using lambda
input_string=input("enter a string")
vowels="AEIOUaeiou"
found_vowels=filter(lambda char:char in vowels,input_string)
print(list(found_vowels))

# Program to find and display vowels in a string

# Function to find vowels in a string
def find_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define the string of vowels

    found_vowels = filter(lambda char: char in vowels, input_string)

    return found_vowels

# Input: string
input_string = input("Enter a string: ")

# Find and display vowels
vowel_list = list(find_vowels(input_string))
print(f"Vowels in the string: {', '.join(vowel_list)}")

