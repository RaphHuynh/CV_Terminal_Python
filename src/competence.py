import json

def competence():
    fileObject=open("json/competence.json","r")
    jsonContent=fileObject.read()
    obj_comp=json.loads(jsonContent)
    print("\x1b[38;5;220m\x1b[4mCompetences :\n\x1b[0m\n\t\x1b[38;5;220mLangages :\x1b[0m","\n")
    print("\t\tWeb :\n\n\t\t\t",obj_comp["competence"][0]["langage"][0]["web"],"\n")
    print("\t\tMobile :\n\n\t\t\t",obj_comp["competence"][0]["langage"][0]["mobile"],"\n")
    print("\t\tProgrammation Objet :\n\n\t\t\t",obj_comp["competence"][0]["langage"][0]["poo"],"\n")
    print("\t\tAutre :\n\n\t\t\t",obj_comp["competence"][0]["langage"][0]["autre"],"\n")
    print("\t\x1b[38;5;220mFrameworks et Bibliotheques :\x1b[0m","\n")
    print("\t\t",obj_comp["competence"][0]["framework"],"\n")
    print("\t\x1b[38;5;220mAutres :\x1b[0m","\n")
    print("\t\t",obj_comp["competence"][0]["autre"])