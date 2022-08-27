import json

def main():

    greet_user()

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify_username(username)     
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

def verify_username(username):
    """Verify the user is last user to operate the program."""
    while(True):
        print(f"Is your username {username}? ", end="")
        verify_username = input("(y/n) ")
        if verify_username == "Y" or verify_username == "y":
            print(f"Welcome back {username}!")
            break
        elif verify_username == "N" or verify_username == "n":
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
            break
        else:
            print("Kindly enter a y or n.")
            

if __name__ == "__main__":
    main()