import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char)for _ in range(length))

    return password

def main():
    length = int(input("Enter the desired length of password: "))

    password = generate_password(length)

    print("Generated Password:",password)

if __name__ == "__main__":
    main()