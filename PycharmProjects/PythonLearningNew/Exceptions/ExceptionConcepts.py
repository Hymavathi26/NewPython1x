#Exceptions
#abnormal event during the execution of program
# 1. try: The code that might raise an exception is placed inside the try block.
"""2. except: If an exception occurs in the try block, the corresponding
 except block is executed. You can have multiple except blocks to
 handle different types of exceptions."""
#3.The code in the else block is executed if no exceptions occur in the try block
#4.finally: The code in the finally block is always executed, whether an exception
# occurred or not.
#Error:specific code that vmigh be having some issues

print("Insert the card")
try:
    a=10/0       #
except Exception as e:       #here we can give only "except" also
    print(f"Zero value error")
    print(e)           #print exceptionerrron like-->division by zero
print("Take the card")


