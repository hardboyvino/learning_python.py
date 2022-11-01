"""
An insecure password locker program.
"""

PASSWORDS = {"email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
            "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
            "luggage": "12345"}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python password.py [account name]")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} is {PASSWORDS[account]}. Password is copied to clipboard")
else:
    print("No such password exists.")
    sys.exit()
