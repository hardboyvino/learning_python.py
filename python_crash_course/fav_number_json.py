import json

# --- ASK USER FOR FAVOURITE NUMBER STORED AS AN INT --- #
fav_number = int(input("What is your favourite number? "))

# --- DEFINE FILENAME --- #
filename = "favourite_number.json"

# --- WRITE THE FAVOURITE NUMBER INTO A FILE --- #
with open(filename, "w") as file_object:
    json.dump(fav_number, file_object)

# --- READ FILE FOR FAVOURITE NUMBER AND PRINT IN A STATEMENT --- #
with open(filename) as file_object:
    favourite_number = json.load(file_object)
    print(f"I know your favourite number is {favourite_number}.")

