import GenerateSignature as GS
import Get_loginKeys as GLK
import time


def set_APIHeaders(method,path,query):
    method = method
    timestamp = str(int(time.time()))
    path = path
    query = query

    
    api_key,api_secret=GLK.get_Accountinfo()
    signature_data = method + timestamp + path + query
    signature = GS.generate_signature(api_secret, signature_data)

    

    headers = {
    'Accept': 'application/json',
    'api-key': api_key,
    'signature': signature,
    'timestamp': timestamp
    }
    return headers