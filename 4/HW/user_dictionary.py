#10-13 and 10-14
from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def user_builder(user_name, location, phone_number):
    return {
        "user_name": user_name,
        "location": location,
        "phone_number": phone_number
    }

def get_new_user(path):
    """Prompt for a new user."""
    user_name= input("What is your name? ")
    location = input("Where do you live? ")
    phone_number = input("What is your phone number? ")
    user = user_builder(user_name, location, phone_number)
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {user['user_name']}!")
    print(f"I know you live in {user['location']}.")
    print(f"Your phone number is {user['phone_number']}.")
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        same_user= input(f"Hello. Are you {user['user_name']} ?\n (Y/n): ").lower()
        if same_user == 'y':
            print(f"Welcome back, {user['user_name']}!")
            print(f"I know you live in {user['location']}.")
            print(f"Your phone number is {user['phone_number']}.")
        else:
            get_new_user(path)
    else:
        get_new_user(path)
greet_user()