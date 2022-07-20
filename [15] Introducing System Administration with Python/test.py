# add user

import os

def new_user(): 
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)

new_user()

'''all program success running with python3 [128].py in ubuntu CLI (Command Line Interface)'''