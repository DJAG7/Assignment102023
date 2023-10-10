#Object to search for special characters using the search function
import re
#Function to Validate the password. Uses Nested If-Else statements to assess the requirements
def check_password_strength(user_input):
    if len(user_input) >= 8:
        if any(char.isupper() for char in user_input) and any(char.islower() for char in user_input):
            if any(char.isdigit() for char in user_input):
                special_characters = r'[!@#$%^&*(),.?":{}|<>]'
                if re.search(special_characters, user_input):
                    print("Your password is correct")
                    return True
                else:
                    print("Your password does not have the required amount of special characters")
            else:
                print("Your password does not meet the required amount of Digits/Numerical Characters")
        else: 
            print("Your password does not meet the required amount of Capital and Small Letters")
    else:
        print("Your password is less than 8 Characters in Length")
        return False

#Intiates the password variable. 
password = "not generated"

#Iterates entering and re-entering of the password if the password is not as per requirements. Asks user to re enter password to confirm 
while password == "not generated":
    user_input = input("Please enter your password. \n Requirements for the password are as follows: \n  Minimum length: The password should be at least 8 characters long. \n  Contains both uppercase and lowercase letters. \n  Contains at least one digit (0-9) \n  Contains at least one special character (e.g., !, @, #, $, %). \t")
    password_validate = check_password_strength(user_input)
    if password_validate == True:
        user_input2 = input("Your password meets requirements. \n \n \n  Please Re-enter password to confirm \t ")
        if user_input2==user_input:
            password=user_input
            print("Password has been saved. \n ")

#Gives the user feedback on the strength of the password
if password_validate == True:
    if len(password) >= 12:
        print("Password is strong")
    elif len(password) >=10:
        print("Password is Medium")
    else:
        print("Password meets requirements but is weak")
