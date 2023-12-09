# Password Generator

A simple Python script to generate secure and customizable passwords. The Password Generator allows you to create passwords with options for uppercase, lowercase, numbers, and special characters. The generated password can be copied to the clipboard for easy use.

## Features

- Customizable password length
- Options to include uppercase, lowercase, numbers, and special characters
- Secure and randomized password generation
- Copy password to clipboard functionality

## Usage

1. Run the script.
2. Enter the desired password length and character preferences.
3. Receive a secure password, copied to your clipboard.

## How to Use

```python
# Example usage in your Python script
from password_generator import PasswordGenerator

gp = PasswordGenerator()
password = gp.generatePassword(upper_case=True, lower_case=True, numbers=True, special_chars=True, length=12)
print(password)
