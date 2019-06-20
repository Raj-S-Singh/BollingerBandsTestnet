import requests
import time
import json
import TradingStrategy as TS
import set_APIHeaders as sAH

list_data_trade=[]
link_api=' https://api.delta.exchange'
path='/chart/history'

query='?symbol=BTCUSD&from='+str(int(time.time()-7200))+'&to='+str(int(time.time()))+'&resolution=1'


url=link_api+path+query
r = requests.get(url)
#r=requests.get('https://api.delta.exchange/products')
#, headers = headers)
r=r.json()


print(len(r['t']))
for i in r['t']:
      print(time.ctime(i))
# with open('data.json', 'w', encoding='utf-8') as outfile:
#     json.dump(r, outfile, ensure_ascii=False, indent=2)