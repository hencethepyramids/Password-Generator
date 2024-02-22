# Password Generator

A simple password generator in Python. The user can choose the length of the password, and specify any special characters to exclude.

## Usage

1. Run the script in a Python environment.
2. Enter the desired password length when prompted. The length must be between 8 and 30 characters.
3. Enter any special characters to exclude, separated by commas. If no characters should be excluded, enter 'none'.

## Example

```python
import secrets
import random
import string

def generate_password(length=15, min_upper=1, min_digits=1, min_punct=1, exclude_punct=None):
    # ... (same code as in your script)

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