# Dictionary of users and their favourite languages
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

# Loop through the dictionary to create the keys and value lists
for name, languages in favorite_languages.items():
    # Considering some value lists might only contain 1 value
    if len(languages) == 1:
        # Print a special message if the value list len in 1
        print(f"{name.title()}'s favourite language is: ", end="")
        for language in languages:
            print(language.title(), end=".\n\n")

    # If value list len is more than 1
    if len(languages) > 1:
        print(f"{name.title()}'s favourite languages are: ", end="")
        # Print all the values except the last item with commans between them
        for language in languages[:-1]:
            print(language.title(), end=", ")
        # Print the last item with a fullstop and a 2 new lines so there is a visible empty line between each output
        for language in languages[-1:]:
            print(language.title(), end=".\n\n")
