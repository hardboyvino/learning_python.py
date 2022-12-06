"""
Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY
"""

# import libraries required
import shutil, os, re

# create the test file
with open("03-17-1989.csv", "w") as f:
    f.write("I am the best in the world!")

try:
    os.unlink("17-03-1989.csv")
except FileNotFoundError:
    pass

# create regex patter to be searched for
date_pattern = re.compile(r"^(.*?)(([01])?\d)-(([0123])?\d)-((19|20)\d\d)(.*)$")

# loop through current working directory (cwd) for all the filenames
for filename in os.listdir():
    # search each filename in the cwd for the re pattern
    date = date_pattern.search(filename)

    # if no pattern is found in the filename then restart for loop
    if date == None:
        continue

    # get the relevant groups from the search conducted
    else:
        prefix = date.group(1)
        mm = date.group(2)
        dd = date.group(4)
        yyyy = date.group(6)
        extension = date.group(8)

    # print the new filename
    print(f"The new file name is: {prefix}{dd}-{mm}-{yyyy}{extension}")

    # get name of new file with european style naming
    new_filename = f"{prefix}{dd}-{mm}-{yyyy}{extension}"

    # move the filename to a new location but with the new name
    shutil.move(filename, new_filename)
