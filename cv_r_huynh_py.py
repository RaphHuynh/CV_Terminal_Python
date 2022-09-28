#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-

import os, requests, urllib

#fonction pour clear le terminal
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#fonction switch
def switch(command):
    if command=="about":
        return "about"
    elif command=="experiences":
        return "experiences"
    elif command=="projets":
        return "projets"
    elif command=="formations":
        return "formations"
    elif command=="hobbies":
        return "hobbies"
    elif command=="cv pdf":
        return urllib.request.urlretrieve('http://math.univ-toulouse.fr/~besse/Wikistat/pdf/st-intro.pdf', "cv_raphaelle_huynh.pdf")
    elif command=="clear":
        return clearConsole()
    elif command=="exit":
        return quit()
    else:
        return "► \x1b[38;5;220mabout\x1b[0m : \n► \x1b[38;5;220mexperiences\x1b[0m : \n► \x1b[38;5;220mprojets\x1b[0m : \n► \x1b[38;5;220mformations\x1b[0m : \n► \x1b[38;5;220mhobbies\x1b[0m : \n► \x1b[38;5;220mcv_pdf\x1b[0m : \n► \x1b[38;5;220mclear\x1b[0m : \n► \x1b[38;5;220mexit\x1b[0m : \n"

print("                         ______     __    __")
print("                        /\  ___\   /\ \  / /")
print("                        \ \ \____  \ \ \/ /")
print("                         \ \_____\  \ \__/")
print("                          \/_____/   \/_/\n")
print("                          Raphaelle HUYNH\n")

print("Bienvenue sur mon CV \x1b[38;5;220m:)\x1b[0m Pour afficher la liste des commandes tappez \x1b[38;5;220mcommand\x1b[0m.\nPour valider les commandes appuyer sur Enter.\n")

while True:
    command=raw_input("\x1b[38;5;8mRaphaelle Huynh ~$\x1b[0m")
    print("")
    print(switch(command))