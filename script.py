import secrets
import random
import string

def generate_password(length=15, min_upper=1, min_digits=1, min_punct=1, exclude_punct=None):
    if length < min_upper + min_digits + min_punct:
        raise ValueError("Password length must be at least " + str(min_upper + min_digits + min_punct))

    chars = list(string.ascii_lowercase)
    password = []

    # Generate required number of uppercase letters, digits, and punctuation characters
    password.extend(secrets.choice(string.ascii_uppercase) for _ in range(min_upper))
    password.extend(secrets.choice(string.digits) for _ in range(min_digits))

    # Generate punctuation characters, excluding any specified by the user
    if min_punct > 0:
        punct_chars = set(string.punctuation)
        if exclude_punct:
            punct_chars.difference_update(exclude_punct)
        punct_chars = list(punct_chars)
        password.extend(secrets.choice(punct_chars) for _ in range(min_punct))

    # Generate remaining characters randomly from all character types
    remaining_length = length - min_upper - min_digits - min_punct
    char_types = [chars, string.digits, punct_chars]
    for _ in range(remaining_length):
        char_type = random.choice(char_types)
        password.append(random.choice(char_type))

    # Shuffle the password characters to ensure randomness
    random.SystemRandom().shuffle(password)

    return ''.join(password)

# Prompt the user to enter the desired password length
while True:
    length_input = input("Enter the desired password length (between 8 and 30 characters): ")
    if length_input.isdigit() and 8 <= int(length_input) <= 30:
        length = int(length_input)
        break
    else:
        print("Invalid length. Please enter a value between 8 and 30.")

# Prompt the user to specify any special characters to exclude
exclude_punct = None
while True:
    punct_input = input("Enter any special characters to exclude (comma-separated, or 'none'): ")
    if punct_input.lower() == "none":
        exclude_punct = None
        break
    else:
        exclude_punct = set(punct_input.split(","))
        if not all(char in string.punctuation for char in exclude_punct):
            print("Invalid characters specified. Please enter a comma-separated list of valid punctuation characters to exclude.")
        else:
            break

# Generate the password with the specified length and requirements
print(generate_password(length, min_upper=1, min_digits=1, min_punct=1, exclude_punct=exclude_punct))