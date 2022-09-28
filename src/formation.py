import json

def formation():
    fileObject=open("json/formations.json","r")
    jsonContent=fileObject.read()
    obj_forma=json.loads(jsonContent)
    for i in reversed(range(3)):
        print("\n\x1b[38;5;26m",obj_forma["formations"][i]["nom"],"\x1b[0m\n\t",obj_forma["formations"][i]["date"],":",obj_forma["formations"][i]["lieu"])
        if(obj_forma["formations"][i]["mention"]!=None):
            print("\t Mention :",obj_forma["formations"][i]["mention"])