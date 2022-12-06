"""
Walk through a folder and file files greater than 1kb and print their names
"""

# import libraries required
import os

# walk return a tuple
for folder, subsfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if os.path.getsize(filename) > 1000:

            # print the sentence with the file name and size in kb (bytes divided by 1000) to 2 decimal places
            print(f"The file {filename} is {os.path.getsize(filename)/1000:.2f}kb in size.")

        # say the file is too small
        else:
            print(f"File {filename} is too small.")
