# import win32com.client
# import time

# excel_file = r'C:\Users\Adeniyi Babalola\Documents\GitHub\Master Data Scientist\learning_python.py\automate_boring_stuff\Places.xlsx'
# password_file = r'C:\Users\Adeniyi Babalola\Documents\GitHub\Master Data Scientist\learning_python.py\automate_boring_stuff\passwords.txt'

# excel = win32com.client.Dispatch('Excel.Application')

# password_list = []

# # extract passwords from file and load to list object
# with open(password_file, 'r', encoding='utf-8') as pwd:
#     passwords = pwd.readlines()
#     for password in passwords:
#         password_list.append(password.replace('\n', ''))


# for password in password_list:
#     try:
#         wb = excel.Workbooks.Open(excel_file, False, True, None, password)
#         wb.Unprotect(password)
#         print('Successfully Password: ', password)
#         excel.DisplayAlerts = False
#         excel.Quit()
#         time.sleep(1)
#         quit()
#     except:
#         print('Bad Passwords: ', password)
#         continue

import subprocess

info = subprocess.run("netsh wlan show profile", capture_output=True).stdout.decode()
temp = info.split()
print(info)