def main():
    while True:
        try:
            password = input("Enter a password: ")
            if len(password) < 8 or len(password) > 20:
                raise ValueError("Password must be between 8 to 20 characters long.")
            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter.")
            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter.")
            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one number.")
            if not any(char in "!@#$%&*" for char in password):
                raise ValueError("Password must contain at least one symbol from the set: !@#$%&*.")
            
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                raise ValueError("Passwords do not match.")
            
            print("Password successfully set!")
            break
        
        except ValueError as error:
            print(f"Invalid password: {error}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
