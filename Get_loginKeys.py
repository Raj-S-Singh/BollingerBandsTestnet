import json    
def get_Accountinfo():
    file=open("keys.json","r")
    Dict_Keys=json.load(file)


    api_key = Dict_Keys["API Key"]
    api_secret = Dict_Keys["API Secret"]
    return api_key,api_secret