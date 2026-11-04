import random
import string

# Combine letters, digits, and punctuation characters
characters = string.ascii_letters + string.digits + string.punctuation

# Randomly choose 12 characters from the pool
password = "".join(random.choice(characters) for i in range(12))

print(f"Your secure random password is: {password}")