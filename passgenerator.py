import random
import string
length = int(input("Enter length of password:"))
#length of password
chars = string.digits+string.ascii_lowercase+string.ascii_uppercase
#character to generate password
password = ""
#store password
for c in range(length):
    password = password + password.join(random.sample(chars, 1))
    print(password)
    print("final password generated:", password)
   
