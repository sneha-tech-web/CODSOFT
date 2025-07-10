import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # All possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the list
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()