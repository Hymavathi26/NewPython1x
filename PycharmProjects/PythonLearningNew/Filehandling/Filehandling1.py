#file handling:How to read a files and write text into files
# and update existing data bu using file handling concept

#open a file
#file_object=open("hymadat.txt","mode")

#modes
# 'r'-->for reading file (default)
# 'w'-->for writing (create a new file or truncates an existing one)
# 'a'--> for  appending (adding data into] a file)
# 'b'-->for binary mode
# '+'-->for updating (reading & writing)

#read a file
# read entire content:content=file_object.read()
# line=file_object.readline()  for single line
# lines=file_object.readlines()  for multiple lines in a list

#writing to a file
# writing string=file_object.write(string)
# writing multiple lines=file_object.writelines(list_of_string)

#close a file:
# syntax:file_obj.close()

with open("Hymadata.txt",'r') as  file:
    content=file.read()
    print(content)
    # print(file.read())
#or use exceptions also

try:
    with open("Hymadata1.txt",'r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as error:
    print(error)