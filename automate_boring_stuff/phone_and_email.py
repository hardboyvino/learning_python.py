"""
Find all the numbers and email addresses on a clipboard.
"""

import pyperclip, re

working_text = str(pyperclip.paste())

# --- CREATE REGEX FOR PHONE NUMBERS --- #
phone_regex = re.compile(
    r"""(
            (\d{3}|\(\d{3}\))?                  # AREA CODE
            (\s|-|\.)?                          # SEPARATOR
            (\d{3})                             # FIRST 3 DIGITS
            (\s|-|\.)                           # SEPARATOR
            (\d{4})                             # LAST 4 DIGITS
            (\s*(ext|x|ext.)\s*(\d{2, 5}))?     # EXTENSION
            )""",
    re.VERBOSE,
)

# --- CREATE REGEX FOR EMAIL ADDRESSES --- #
email_regex = re.compile(r"(\w+@\w{3,}\.\w{2,3})(\.\w{2})?")


# --- FIND ALL MATCHES FOR BOTH REGEXES
mo_phone = [groups[0] for groups in phone_regex.findall(working_text)]

# --- COPY ALL REGEX TO CLIPBOARD --- #
# final_regex = pyperclip.copy(mo_phone)
final_regex = [groups[0] for groups in email_regex.findall(working_text)]

# --- PRINT A SAMPLE --- #
for phone in mo_phone:
    print(f"{phone}")
for regex in final_regex:
    print(f"{regex}")

# --- MESSAGE IF NO PHONE NUMBER OR EMAIL ADDRESS IS FOUND --- #
