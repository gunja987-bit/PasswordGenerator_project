import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = "!@#$%^&*()" if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        raise ValueError("No character sets selected!")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("==== Password Generator ====")
    try:
        length = int(input("Enter password length (e.g., 12): "))
        count = int(input("How many passwords to generate? "))

        use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols (!@#$...)? (y/n): ").lower() == 'y'

        print("\nGenerated Password(s):")
        for _ in range(count):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            print(pwd)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
