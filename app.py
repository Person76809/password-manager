import json
from stdiomask import getpass

# Define the filename for storing passwords
PASSWORD_FILE = 'passwords.json'

# Load existing passwords or create a new dictionary
try:
    with open(PASSWORD_FILE, 'r') as f:
        passwords = json.load(f)
except FileNotFoundError:
    passwords = {}

# Prompt the user for a service and password
service = input('Enter the service name: ')
username = input('Enter the username: ')
password = getpass('Enter the password: ')

# Store the password in the dictionary
passwords[service] = {'username': username, 'password': password}

# Save the updated password dictionary to the file
with open(PASSWORD_FILE, 'w') as f:
    json.dump(passwords, f)

# Print a confirmation message
print('Password for {} has been saved.'.format(service))
