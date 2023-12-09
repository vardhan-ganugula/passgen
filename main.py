import random
import string
import pyperclip



class PasswordGenerator:
    def __init__(self):
        self.chars = ''
        self.response = ''
        
    def generatePassword(self, upper_case=True, lower_case=True, numbers=True, special_chars=True,length=10):
        if upper_case:
            self.chars += string.ascii_uppercase
        if lower_case:
            self.chars +=string.ascii_lowercase
        if numbers:
            self.chars +=string.digits
        if special_chars:
            self.chars +=string.punctuation
        if length <8:
            self.response = "Password must be atleast of 8 characters"
            return self.response
        if not self.chars:
            self.response = "At least one char should be selected"
            return self.response
        password = "".join(random.sample(self.chars, length))
        return password
    
def main():
    print("""       
 ____                ____            
|  _ \ __ _ ___ ___ / ___| ___ _ __  
| |_) / _` / __/ __| |  _ / _ \ '_ \ 
|  __/ (_| \__ \__ \ |_| |  __/ | | |
|_|   \__,_|___/___/\____|\___|_| |_|

Created by Ganugula Vardhan
""")
    try:
        length = int(input("Enter the password Length : "))
    except ValueError:
        print("Please enter a valid integer.")
    uppercase = input("Include uppercase ? (y/n) : ").lower()
    lowercase = input("Include lowercase ? (y/n) : ").lower()
    number = input("Include number ? (y/n) : ").lower()
    special_chars = input("Include special_chars ? (y/n) : ").lower()
    gp = PasswordGenerator()
    password = gp.generatePassword(upper_case=uppercase, lower_case=lowercase, numbers=number, special_chars=special_chars, length=length)
    if length==len(password):
        print(f" Your Password is : \033[1;32m {password} \033[1;37m")
        print("Password copied to clip board")
        pyperclip.copy(password)
    else:
        print("\033[1;31m " + password + "\033[1;37m")


if __name__ == "__main__":
    main()
    input()

