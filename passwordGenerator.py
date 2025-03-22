import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Define the characters to use
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (8-128): "))
            if length < 8 or length > 128:
                print("Password length must be between 8 and 128.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt the user to specify the complexity of the password
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()