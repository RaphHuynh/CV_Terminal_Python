import json

def hobbies():
    fileObject=open("json/hobbies.json","r")
    jsonContent=fileObject.read()
    obj_hob=json.loads(jsonContent)
    print("\x1b[38;5;220m\x1b[4mHobbies :\x1b[0m\n")
    for i in range(4):
        print("\t-",obj_hob["hobbies"][i])