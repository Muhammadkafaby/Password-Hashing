import os
import secrets
import argon2
import re
from getpass import getpass

# Initialize Argon2 hasher
ph = argon2.PasswordHasher()

def hash_password(password: str) -> str:
    # Hash the password using Argon2
    hashed_password = ph.hash(password)
    return hashed_password

def verify_password(stored_password: str, provided_password: str) -> bool:
    try:
        # Verify the password using Argon2
        ph.verify(stored_password, provided_password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

def generate_random_password(length: int = 12) -> str:
    # Generate a random password
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def check_password_strength(password: str) -> (bool, str):
    # Check the strength of the password
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*()-_=+]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is strong."

def menu():
    while True:
        print("\nMenu:")
        print("1. Hash a password")
        print("2. Verify a password")
        print("3. Generate a random password")
        print("4. Check password strength")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = getpass("Enter the password to hash: ")
            hashed_password = hash_password(password)
            print(f"Hashed Password: {hashed_password}")
        elif choice == '2':
            stored_password = getpass("Enter the stored hashed password: ")
            provided_password = getpass("Enter the password to verify: ")
            is_valid = verify_password(stored_password, provided_password)
            print(f"Password is valid: {is_valid}")
        elif choice == '3':
            try:
                length = int(input("Enter the length of the random password: "))
                random_password = generate_random_password(length)
                print(f"Random Password: {random_password}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            password = getpass("Enter the password to check strength: ")
            is_strong, message = check_password_strength(password)
            print(message)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()