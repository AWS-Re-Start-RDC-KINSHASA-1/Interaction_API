
import os
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Indiquez le nom de l'utilisateur à ajouter: ")
        print("Utiliser username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)
