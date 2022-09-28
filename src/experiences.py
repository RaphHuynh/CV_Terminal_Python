import json

def experiences():
    fileObject=open("json/experiences.json","r")
    jsonContent=fileObject.read()
    obj_exp=json.loads(jsonContent)
    for i in range(1):
        print("\t\x1b[38;5;26m-",obj_exp["experiences"][i]["nom"],":",obj_exp["experiences"][0]["lieu"],"\x1b[0m\n",obj_exp["experiences"][i]["description"],"\n",obj_exp["experiences"][i]["duree"],"\x1b[38;5;124m\n",obj_exp["experiences"][i]["techno"],"\x1b[38;5;41m\n",obj_exp["experiences"][i]["type"],":",obj_exp["experiences"][0]["poste"],"\x1b[0m\n")