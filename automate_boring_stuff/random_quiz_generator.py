"""
Program to generate 35 random tests with the answers on another sheet
"""

# --- IMPORT IMPORTANT MODULES
import random


# --- DICTIONARY WITH STATES AND CAPITALS
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}


for quiz in range(1, 2):
    # --- SHUFFLE THE ORDER OF THE STATE NAMES
    state_dict = list(capitals)
    random.shuffle(state_dict)

    # --- WRITE ALL THE STATES AND CAPITALS INTO A TEXT FILE
    with open("quiz.txt", "w") as filename:
        for key, value in capitals.items():
            filename.write("%s - %s\n" % (key, value))

    # --- RANDOM QUESTION FOR EACH STUDENT
    with open(f"quiz {quiz}.csv", "w") as file:
        file.write("WELCOME TO THE QUIZ\n\nSTUDENT NAME:\n\n")
        for state in state_dict:
            file.write("What is the capital of %s?\n" % (state))

    with open(f"quiz answers {quiz}.csv", "w") as file:
        file.write("WELCOME TO THE QUIZ ANSWERS\n\n")
        for state in state_dict:
            file.write("What is the capital of %s? %s\n" % (state, capitals[state]))
