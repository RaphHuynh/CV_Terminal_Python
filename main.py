#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-

from curses import echo
import os, urllib.request, json

#fonction pour clear le terminal
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#fonction switch
def switch(command):
    if command=="about":
        fileObject= open("about.json","r")
        jsonContent = fileObject.read()
        obj_about = json.loads(jsonContent)
        print("Bonjour je suis",obj_about['nom'],obj_about['prenom'],", j'ai",obj_about['age'],"ans.\nJe suis passionee par l'informatique depuis 2018.\nActuellement, je suis ",obj_about['situation'],"a",obj_about['ville'],".\nVoici mon lien github :\x1b[38;5;41m\x1b[4m",obj_about['github'],"\x1b[0m")
        return ""
    elif command=="experiences":
        return "experiences"
    elif command=="projets":
        return "projets"
    elif command=="formations":
        return "formations"
    elif command=="hobbies":
        return "hobbies"
    elif command=="cv pdf":
        return "a venir\n" #urllib.request.urlretrieve('lien a venir', "cv_raphaelle_huynh.pdf")
    elif command=="clear":
        return clearConsole()
    elif command=="exit":
        return quit()
    else:
        return "- \x1b[38;5;220mabout\x1b[0m : \n- \x1b[38;5;220mexperiences\x1b[0m : \n- \x1b[38;5;220mprojets\x1b[0m : \n- \x1b[38;5;220mformations\x1b[0m : \n- \x1b[38;5;220mhobbies\x1b[0m : \n- \x1b[38;5;220mcv_pdf\x1b[0m : \n- \x1b[38;5;220mclear\x1b[0m : \n- \x1b[38;5;220mexit\x1b[0m : \n"

print("                         ______     __    __")
print("                        /\  ___\   /\ \  / /")
print("                        \ \ \____  \ \ \/ /")
print("                         \ \_____\  \ \__/")
print("                          \/_____/   \/_/\n")
print("                          Raphaëlle HUYNH\n")

print("Bienvenue sur mon CV \x1b[38;5;220m:)\x1b[0m Pour afficher la liste des commandes tappez \x1b[38;5;220mcommand\x1b[0m.\nPour valider les commandes appuyer sur Enter.\n")

while True:
    command=input("\x1b[38;5;8mRaphaelle Huynh ~$\x1b[0m")
    print("")
    print(switch(command))