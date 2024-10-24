''' Ex 6 - Brute Force Attack'''

pwd = "12345"
attempt = 0
user = input("Enter password: ")

while not user == pwd and attempt < 4:
    #while value is not equal to pwd value and attempt is lesser than 4
    print("Invalid password please try again")  #print a message indicating user to enter again
    attempt += 1 #number of attempt is increased 
    print(f"you have {attempt}/5 attempts left") #statement informing user of the number of attempts 
    user = input("Enter password: ") #user input password again 
if attempt == 4 and user!= pwd: #if number of attempts reach last and user input value is not equal to pwd value 
    print("""Access Denied, Authorities have been alerted 
          ESCAPE WHILE YOU CAN!!""") #print access denied 
elif user == pwd:
    print("Password is Correct, Access granted") #else if user value is equal to pwd value print password is correct





