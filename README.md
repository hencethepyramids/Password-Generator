Password Generator
This script generates a random password with a specified length and requirements.

Requirements
At least one uppercase letter
At least one digit
At least one punctuation character (excluding any specified by the user)
The remaining characters are randomly chosen from all character types
Usage
Run the script using a Python interpreter.
Enter the desired password length (between 8 and 30 characters).
Enter any special characters to exclude (comma-separated, or 'none').
The script will generate a password that meets the specified requirements and print it to the console.
Dependencies
Python 3.x
secrets module (included in Python 3.6 and later)
random module (included in Python standard library)
string module (included in Python standard library)
Notes
The password is generated using the secrets module to ensure cryptographically strong randomness.
The password is shuffled using random.SystemRandom().shuffle() to further ensure randomness.
The user can specify any number between 8 and 30 for the password length.
The user can specify any number of uppercase letters, digits, and punctuation characters to include in the password.
The user can specify any number of punctuation characters to exclude from the password.
The remaining characters are randomly chosen from all character types.
The password is generated with a minimum length of 8 characters, including at least one uppercase letter, one digit, and one punctuation character.
The password is generated with a maximum length of 30 characters.
The password is generated with a maximum of 10 uppercase letters, 10 digits, and 10 punctuation characters.
The remaining characters are randomly chosen from all character types.
The password is generated with a minimum of 1 character from each character type.
The password is generated with a maximum of 26 characters from the lowercase character type.
The password is generated with a maximum of 10 characters from each of the other character types.
The password is generated with a minimum of 1 character from each character type.
Example
Enter the desired password length (between 8 and 30 characters): 12 Enter any special characters to exclude (comma-separated, or 'none'): , 5&Jt9$7Lp

License
This project is licensed under the MIT License - see the LICENSE file for details.
