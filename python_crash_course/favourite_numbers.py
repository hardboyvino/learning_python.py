favourite_numbers = {"chandler": 3, "monica": 7, "joey": 69, "rachel": 100}

for key, value in favourite_numbers.items():
    print(f"{key.title()}'s favourite number is {value}")

for key in sorted(favourite_numbers.keys()):
    print(key.title())

for value in sorted(favourite_numbers.values()):
    print(value)