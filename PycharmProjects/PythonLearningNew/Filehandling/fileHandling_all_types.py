#textfile:
with open("Hymadata.txt",'r') as file:
    content=file.read()
    print(content)


#csv file
import csv

with open("mydata.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)



