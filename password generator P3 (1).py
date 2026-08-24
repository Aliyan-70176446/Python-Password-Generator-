"""
Project 3: Random Password Generator
DecodeLabs - Python Industrial Training Kit

Generates a cryptographically secure random password using the
`secrets` module (not `random`, which is predictable) and Python's
built-in `string` module for character classification.
"""

import string
import secrets


def get_password_length():
    """
    Phase 1: Input validation.
    Keeps asking until the user provides a valid positive integer,
    so the program never crashes on bad input.
    """
    while True:
        user_input = input("Enter desired password length (min 8 recommended): ")
        try:
            length = int(user_input)
            if length <= 0:
                print("Length must be a positive number. Try again.")
                continue
            return length
        except ValueError:
            print("That's not a valid number. Please enter an integer.")


def generate_password(length):
    """
    Phase 2: Build the character pool and generate the password.

    - Uses string.ascii_letters + string.digits (letters and numbers only,
      no symbols) instead of manually typing character sets.
    - Uses secrets.choice() instead of random.choice() because `random`
      relies on the deterministic Mersenne Twister PRNG, which is
      predictable and unsafe for security-sensitive data.
    - Builds the password with ''.join() over a list comprehension
      instead of string concatenation (+=) in a loop, since strings
      are immutable and repeated concatenation is O(N^2).
    """
    char_pool = string.ascii_letters + string.digits

    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password


def main():
    print("=== DecodeLabs Secure Password Generator ===")
    length = get_password_length()

    password = generate_password(length)

    print("\nYour generated password:")
    print(password)


if __name__ == "__main__":
    main()