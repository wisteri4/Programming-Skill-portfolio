'''EX 5 - Days of the Month'''

month = {1: "31", 
         2: "28", 
         3: "31", 
         4: "30", 
         5: "31",
         6: "30",
         7: "31",
         8: "31",
         9: "30",
         10: "31",
         11: "30",
         12: "31"} 
#Dictionary where the month's numbers are keys and its values are the number of days 

num_month = int(input("Input your month number: ")) #Asks user to input their month number in integer
if num_month == 2: #if value is 2 
    leap = input("Is the year leap year? ") #Ask user if year is leap year 
    if leap == "yes": #If value is true 
       month[2] = 29 #Modify value key 2 to 29 
       print ("Number of days are",month[2],"in that month") #Print the modified value 
    elif leap == "no":#Else if value is not modified 
        print ("Number of days are",month[2],"in that month") #Print initial value of key 2 as 28 days
elif num_month > 12: #else if input given is greater than the month number 12
    print("Invalid Input, please try again from 1 to 12 ") #print input is invalid statement 
else: #else if input given does not apply to any of the above 
    print(f"There are {month[num_month]} days in that month") #then print the number of days within the statement 

