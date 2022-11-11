"""
Multiclipboard - Python program to keep track of multiple pieces of text saving each text in a keyword.
"""

import sys, pyperclip


keywords = {"yes": "me", "no": "you"}
dict_keys = list(keywords)
first_argument = sys.argv[1].lower()

# --- IF ARGUMENT IS SAVING A KEYWORD TO THE DICTIONARY
if first_argument == "save" and len(sys.argv) == 3:
    keywords[sys.argv[2]] = str(pyperclip.paste())

# --- IF ARGUMENT IS REQUESTING LIST OF ALL KEYWORDS
elif first_argument == "list" and len(sys.argv) == 2:
    keywords_lists = str(dict_keys)
    pyperclip.copy(keywords_lists)

# --- IF ARGUMENT IS LOADING KEYWORD CONTENTS
elif first_argument in dict_keys and len(sys.argv) == 2:
    pyperclip.copy(keywords[first_argument])

# --- NOTIFY USER OF HOW TO USE PROGRAM PROPERLY
else:
    print("Usage for saving:\npython filename save 'keyword'\n\nUsage for list of keywords:\npython filename list\n\nUsage for loading clipboard:\npython filename 'keyword'")
