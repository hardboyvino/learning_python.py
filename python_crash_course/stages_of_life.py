age = 35

if age < 2:
    person = "a baby"
elif age < 4:
    person = "a toddler"
elif age < 13:
    person = "a kid"
elif age < 20:
    person = "a teenager"
elif age < 65:
    person = "an adult"
elif age >= 65:
    person = "an elder"

print(f"You are {person}.")
