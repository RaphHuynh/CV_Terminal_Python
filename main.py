#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-

from curses import echo
import os, urllib.request, json

import sys;
sys.path.insert(1, "./src");
from formation import formation ;
from experiences import experiences;
from hobbies import hobbies;
from projet import projet;
from about import about;

#fonction pour clear le terminal
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#fonction switch
def switch(command):
    if command=="about":
        about();
    elif command=="experiences":
        experiences();
    elif command=="projets":
        projet();
    elif command=="formations":
        formation();
    elif command=="hobbies":
        hobbies();
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