''' EX8 - Simple Search '''

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #create the list of names

userin = input("Enter a name: ") #allow user to input name
if userin in names: #if the input is in the list of names 
    print(userin, "is in the list") #print the input value in statement
else: #else if any value given is not in the list
    print("Invalid Input") #print invalid input 

