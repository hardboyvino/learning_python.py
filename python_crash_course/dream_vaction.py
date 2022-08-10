dreams = {}

while True:
    # Get user input
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    # Add to dictionary
    dreams[name] = response

    # Ask if there are others, if no then end the loop
    again = input("Other respondants? (yes/no) ")

    if again == "no":
        break
for name, response in dreams.items():
    print(f"{name}\t-\t{response}.")
