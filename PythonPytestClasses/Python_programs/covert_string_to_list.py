# By using split() --built-in function

input_string = "MOnday tuesday wednesday thursday friday saturday"
days = input_string.split()
print(days)


#write a program to print all numbers from o to 6
#except 3 and 6 numbers in the list
for i in range(7):
    if i ==3 or i==6:
        continue
    print(i)

#without using continue
for i in range(7):
    if i !=3 and i !=6:
        print(i)
