# from collections import Counter
#
# def count_occurance(input_string):
#     occurance = Counter(input_string)
#     for char, count in occurance.items():
#         print(f'{char}:{count} occurance')
#
# input_string = input("Enter string:\n")
# count_occurance(input_string)

#without using collections
def letter_cout_occurance(input_string):
    input_string=input_string.lower()
    #initialize an empty dictionary to store letters count
    letter_count = {}
    #itearte through each charactor in the string
    for char in input_string:
        #chech if the charactor is string
        if char.isalpha():
            #letter_count.get(char, 0): This part retrieves the current count of the letter from the letter_count dictionary. If the letter is not already in
            # the dictionary, it returns the default value 0
            letter_count[char]=letter_count.get(char,0)+1
    return letter_count

input_string=input("Enter input string:\n")
result=letter_cout_occurance((input_string))
#display the result
for char,count in result.items():
    print(f'{char}:{count} occurance')




