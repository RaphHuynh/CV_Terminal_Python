import json

def projet():
    fileObject=open("json/projet.json","r")
    jsonContent=fileObject.read()
    obj_projet=json.loads(jsonContent)
    for i in range(3):
        print("\t\x1b[38;5;26m-",obj_projet["projets"][i]["nom"],"\x1b[0m\n",obj_projet["projets"][i]["description"],"\x1b[38;5;124m\n",obj_projet["projets"][i]["techno"],"\x1b[38;5;41m\n",obj_projet["projets"][i]["accessibilite"],"\n")