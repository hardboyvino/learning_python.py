"""
Add a prefix to the start of every filename and move a copy to a new folder.
"""

# import libraries required
import shutil, os

# define additional text
before_text = "spam_"

# path for new files folder
path = os.path.join(os.getcwd(), "test_files")

# check if folder exists, if not, create a folder for the new files
if not os.path.exists("test_files"):
    os.makedirs(path)

# get the filename
for filename in os.listdir():
    if filename == "17-03-1989.csv":

        # add the new text to the front of the filename for all the files in the folder
        new_filename = f"{before_text}{filename}"

        # move a copy of the files to the new folder
        shutil.copy(filename, os.path.join(path, new_filename))
