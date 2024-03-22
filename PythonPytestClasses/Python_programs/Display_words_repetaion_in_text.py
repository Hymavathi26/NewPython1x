'''str1=input("Enter string1 value:\n")
n=int(input("Enter a count:\n"))

str1=str1.split()
print(str1)
count=dict()
for word in str1:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)
word_list=[]
for key in count:
    if count[key]>=n:
        word_list.append(key)
if len(word_list)>0:
    print(word_list)
else:
    print("NA")'''

#by using counter
from collections import Counter
def display_word_repetation(input_string):
    # # Split the input string into words
    words=input_string.split()

    # # Count the occurrences of each word
    word_count=Counter(words)

    # # Display the result
    for word,count in word_count.items():
        print(f'word "{word}" occurs "{count}" times.')

input_string=input("Enter input string:\n")
display_word_repetation(input_string)

#without using Counter
# def display_word_repetation(input_string):
#     words=input_string.split()
#     word_count=[]
#
#     for word in words:
#         current_word=word_count.get(word,0)
        




