"""
A mad libs program that reads in text files and lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB or VERB appears in the text file.
"""
import re

file = "madlibs.txt"


with open(file, "w") as filename:
    filename.write("""The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.""")

# --- READ THE FILES CONTENT INTO A STRING
with open(file, "r") as filename:
    sentence = str(filename.read())
    print(sentence)

# # --- READ THE TEXT BACK LOOKING FOR THE 4 KEYWORDS ONE AT A TIME
grammar = re.compile(r"ADJECTIVE|ADVERB|NOUN|VERB")


# --- KEEP DOING THIS TILL THERE IS NO MORE KEYWORD IN THE STRING
while True:
    # --- SEARCH FOR THE FIRST OCCURENCE OF ANY OF THE KEYWORDS
    mo = grammar.search(sentence)
    # print(mo.group())

    # --- IF THERE ARE NO KEYWORDS BREAK OUT OF LOOP
    if mo == None:
        break

    # --- FOR INDEFINITE ARTICLES SAKE
    elif mo.group() == "ADJECTIVE" or mo.group() == "ADVERB":

        # --- REQUEST A REPLACEMENT
        print("Enter an %s: " % (mo.group().lower()))
        # word = input()

        # # --- SUBSTITUTE THE KEYWORD OCCURENCE WITH THE REPLACEMENT WORD
        # # --- ASSIGN THE RESULTING STRING INTO THE ORIGINAL VARIABLE
        # sentence = grammar.sub(word, sentence, 1)

    elif mo.group() == "NOUN" or mo.group() == "VERB":
        # --- REQUEST A REPLACEMENT
        print("Enter a %s: " % (mo.group().lower()))
        # word = input()
        # sentence = grammar.sub(word, sentence, 1)


with open(file, "w") as filename:
    filename.write(sentence)
