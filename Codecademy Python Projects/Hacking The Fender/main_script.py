# Import those that are needed
import csv
import json

# Create an empty list for compromised users
compromised_users = []

# Open the passwords file and read the ocntents inside
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  # Add all the compromised users into the compromised users list
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

# Open the compromised users file in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Write the username of each username thats been compromised and format with a comma and space to split the usernames
  for compromised_user in compromised_users:
    compromised_user_file.write(f"{compromised_user}, ")

# Open json file in write mode
with open('boss_message.json', 'w') as boss_message:
  # Create a dictionary
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  # Write out the dictionary into boss message 
  json.dump(boss_message_dict, boss_message)

# Open new passwords in write mode 
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)

# AI Review - Your code reads passwords.csv, collects compromised usernames, writes them to compromised_users.txt, emits a JSON boss message, and writes the Slash Null signature into new_passwords.csv.
# It follows the project tasks and runs without syntax errors.
# Code uses clear flow with with blocks and descriptive variable names. The comments help explain each step.
# Uses streaming file I/O and avoids loading everything into memory beyond the compromised list. However, there are minor inefficiencies in string handling for output formatting.