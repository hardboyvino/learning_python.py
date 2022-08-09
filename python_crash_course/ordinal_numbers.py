numbers = [num  for num in range(1, 13)]


for number in numbers:
    if number == 1:
        position = "st"
        print(f"You are {number}{position}.")
    elif number == 2:
        position = "nd"
        print(f"You are {number}{position}.")
    elif number == 3:
        position = "rd"
        print(f"You are {number}{position}.")
    elif number < 10:
        position = "th"
        print(f"You are {number}{position}.")