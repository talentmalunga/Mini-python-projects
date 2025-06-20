import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Random Password Generator")
length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(length))
