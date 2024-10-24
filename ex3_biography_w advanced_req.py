''' EX-3 Biography'''

name1 = input("Enter your first name: ")  
hometown = input("Enter your hometown: ")
#User input for first name, second name, hometown and store the input in variables

age = input("Enter your age: ")
#user input age 
if age == int: #if value is integer 
    print (f'Hello! my name is {name1}, I am {age} years old and I live in {hometown}')
#print the variables in one sentence using F-string using the stored variables in the placeholder
else: #else if value is string
    print (f'Hello! my name is {name1}, I am {age} years old and I live in {hometown}')
#print string value within the statement

