import random
import string


def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number < 0:
                print("Please enter a number that is 0 or greater.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_password(num_letters, num_symbols, num_numbers):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_characters = []

    for _ in range(num_letters):
        password_characters.append(random.choice(letters))

    for _ in range(num_symbols):
        password_characters.append(random.choice(symbols))

    for _ in range(num_numbers):
        password_characters.append(random.choice(numbers))

    random.shuffle(password_characters)

    password = ""

    for character in password_characters:
        password += character

    return password


def check_password_strength(password):
    length = len(password)

    has_lowercase = False
    has_uppercase = False
    has_number = False
    has_symbol = False

    for character in password:
        if character.islower():
            has_lowercase = True
        elif character.isupper():
            has_uppercase = True
        elif character.isdigit():
            has_number = True
        else:
            has_symbol = True

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_lowercase:
        score += 1
    if has_uppercase:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("Welcome to the Secure Password Generator!")

    while True:
        num_letters = get_valid_number("How many letters would you like in your password?\n")
        num_symbols = get_valid_number("How many symbols would you like?\n")
        num_numbers = get_valid_number("How many numbers would you like?\n")
        num_passwords = get_valid_number("How many passwords would you like to generate?\n")

        total_length = num_letters + num_symbols + num_numbers

        if total_length < 8:
            print("\nWarning: Passwords under 8 characters are considered weak.")
            print("Try using at least 8 total characters.\n")

        print("\nGenerated Passwords:")

        for password_number in range(1, num_passwords + 1):
            password = generate_password(num_letters, num_symbols, num_numbers)
            strength = check_password_strength(password)

            print(f"{password_number}. {password} | Strength: {strength}")

        repeat = input("\nWould you like to generate more passwords? (yes/no): ").lower()

        if repeat != "yes":
            print("Exiting Secure Password Generator.")
            break


main()
