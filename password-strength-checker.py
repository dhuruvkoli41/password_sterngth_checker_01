# password sterngth checker --
#conditions fro strong password -
#1. minimum 8 charators 
#2. digit,upper case,lower case
#3. special charactor 

import re # used to identify the special charactors --
special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
def check_passsword_strength(password):
  # here we check length of password-
    if len(password)<8:
        return "Weak! password must be atleast having 8 charcters"
  
  # using isdigit that help to find that the char are num or not 
    if not any(char.isdigit() for char in password):
        return "Weak! password must contain a digit !!"

  # using isupper to find any upper case latter in password -  
    if not any(char.isupper() for char in password):
        return "Weak! password must contain an upper case latter "

  # using islower to find the lower case latter in password -  
    if not any(char.islower() for char in password):
        return "Weak! password mut contain a lower case latter "

  # using re.search for the special charactors -  
       
    if not any(char in special_chars for char in password):
        return "Weak! password must contain a Special character "

  # final check !!   
    return " Strong: Your password is secured & strong inuff!!  "
      

def password_checker():  # main code to execute !!
    print("Welcome to the password strength checker!")

    while True:
        password = input("Enter your password (or type 'exit' to Quit ):")

        if password.lower() == 'exit':
            print("Thank you for using this tool !")
            break

        result = check_passsword_strength(password) # calling of the checker function 
        print(result)

        # Run the password checker tool - 
if __name__ == "__main__": #used to run this first i the whole code 
            password_checker()



