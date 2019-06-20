import json
import requests
import time

class interact_with_API:
    def __init__(self,request):
        self.request_CODE=request
        file=open('info_API.json','r')
        self.datastore=json.load(file)


    def get_json_from_request(self):
        
        if self.request_CODE=='GET CURRENT DATA':
            url=url=self.datastore['Endpoint URL']+self.datastore['path']['currentdata']+"?symbol="+self.datastore['query']['symbol']
            data_request=requests.get(url)
            data_json=data_request.json()
            return data_json

        elif self.request_CODE=='GET INITIAL DATA':
            
            url=self.datastore['Endpoint URL']+self.datastore['path']['initialdata']+"?symbol="+self.datastore['query']['symbol']+"&from="+str(int(time.time()-7200))+'&to='+str(int(time.time()))+'&resolution=1'
            data_request=requests.get(url)
            data_json=data_request.json()
            return data_json
        
        