import csv

temp_data=[]
id_update=2
#new_update=33

with open("mydata.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)
temp_data[2][2]=33
print(temp_data)



with open('mydata.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)


