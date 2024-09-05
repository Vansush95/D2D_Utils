import random
import string
import os
import time
import pyfiglet

# Function to generate a password
def generate_password(length, include_numbers, include_special):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special else ''
    
    # Ensure the password includes both uppercase and lowercase
    password_characters = lowercase + uppercase + digits + special_chars
    
    # Generate the password with at least one uppercase and lowercase character
    password = [
        random.choice(lowercase),
        random.choice(uppercase)
    ]
    
    password += random.choices(password_characters, k=length-2)
    random.shuffle(password)
    
    return ''.join(password)

# Function to store the password in a hidden file
def store_password(username, password):
    # Get the home directory
    home_directory = os.path.expanduser("~")
    # Define the hidden file path
    file_path = os.path.join(home_directory, ".passwords.txt")
    
    # Save the username and password to the hidden file
    with open(file_path, "a") as file:
        file.write(f"Username: {username}\nPassword: {password}\n\n")
    
    print(f"Password saved in hidden file: {file_path}")

# Function to display the cool banner with greetings
def display_banner():
    banner = pyfiglet.figlet_format("AngeL God", font="slant")
    print(banner)
    print("👼 Welcome, AngeL God! The protector of passwords! 👼\n")

    # Greeting in 5 different languages
    greetings = {
        "English": "Hello, AngeL God!",
        "Japanese": "こんにちは、天使の神様！",
        "French": "Bonjour, AngeL Dieu !",
        "Spanish": "¡Hola, Dios Ángel!",
        "German": "Hallo, Engel Gott!"
    }
    
    for language, greeting in greetings.items():
        print(f"{language}: {greeting}")
    
    print("\nLet's protect some passwords today!\n")

def main():
    # Display the cool banner and greetings
    display_banner()
    
    # Ask for username
    username = input("Enter the username: ")
    
    # Ask for password length
    while True:
        try:
            length = int(input("Enter the password length (12-20): "))
            if 12 <= length <= 20:
                break
            else:
                print("Please enter a number between 12 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask if the user wants numbers
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    
    # Ask if the user wants special characters
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    # Generate the password
    password = generate_password(length, include_numbers, include_special)
    
    # Display the generated password
    print(f"Generated Password: {password}")
    
    # Store the password in a hidden file
    store_password(username, password)
    
    # Farewell message
    print("\n🌟 Mission complete, AngeL God! Your passwords are safely stored. 🌟")
    time.sleep(1)
    print("👋 Goodbye, mighty protector of secrets! Until next time! 👋")

if __name__ == "__main__":
    main()
