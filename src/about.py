import json

def about():
    fileObject= open("json/about.json","r")
    jsonContent = fileObject.read()
    obj_about = json.loads(jsonContent)
    print("Bonjour je suis",obj_about['nom'],obj_about['prenom'],", j'ai",obj_about['age'],"ans.\nJe suis passionee par l'informatique depuis 2018.\nActuellement, je suis ",obj_about['situation'],"a",obj_about['ville'],".\nVoici mon lien github :\x1b[38;5;41m\x1b[4m",obj_about['github'],"\x1b[0m")