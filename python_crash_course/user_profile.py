def user_profile(first_name, last_name, **other_details):
    """Print all the details of a user."""
    user_details = {}
    user_details[first_name] = first_name.lower()
    user_details[last_name] = last_name.lower()
    for key, value in other_details.items():
        user_details[key] = value

    print(f"The user {first_name.title()} {last_name.title()} also has the following details:")
    for key, value in user_details.items():
        if key != first_name and key != last_name:
            print(f"- {key.title()}\t{value.title()}")

user_profile("aLbert", "einStEin", location="lAgos", salary="$1,000,000")