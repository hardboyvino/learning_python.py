"""
Remove the zeros from filename such spam0042.txt
"""

# import the libraries required
import re, os, shutil

# create the regex pattern to be searched
double_zeros = re.compile(r"(0{2,})")

# loop over every file to see which filenames match the regex
for filename in os.listdir():
    matches = double_zeros.search(filename)

# if the filename does not match then skip
    if matches == None:
        continue

# replace the matched portion with a blank
    else:
        new_filename = double_zeros.sub("", filename)

# create a new file with the new name in the same folder
    shutil.copy(filename, new_filename)
