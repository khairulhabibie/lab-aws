# remove user

import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r " + username)

remove_user()

'''all program success running with python3 [128].py in ubuntu CLI (Command Line Interface)'''