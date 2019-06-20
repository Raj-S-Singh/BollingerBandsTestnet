import requests
import time
import json

import TradingStrategy2 as TS
import set_APIHeaders as sAH
import Interact_with_API as iAPI

balance=1000

obj_interact=iAPI.interact_with_API("GET INITIAL DATA")
r=obj_interact.get_json_from_request()


tradepriceslist=[]
tradetimelist=[]


tradepriceslist=tradepriceslist + r['c'][-20:]
tradetimelist=tradetimelist + r['t'][-20:]

print(tradepriceslist[-1])

dict_trade={'list_trade':tradepriceslist,'list_tradeTime':tradetimelist}
obj=TS.Trading_Strategy2(dict_trade)
Bands=obj.Calculate_BBands(tradepriceslist)
print(Bands)

obj_interact=iAPI.interact_with_API("GET CURRENT DATA")


while True:
      r=obj_interact.get_json_from_request()
      print(r)
      print(time.ctime())
      
      if r['close']!=tradepriceslist[-1]:
            status=obj.trade_Check(r['close'])
            print(obj)
            if status=='Enter the trade':
                  obj.tradeRecords['Trade Entry Time'].append(time.ctime(r['timestamp']))
                  
            if status=='Exit Trade':
                  quantity=balance/obj.tradeEnterPrice

                  
                  if obj.trade_nature=="LONG":
                        profit=(obj.tradeExitPrice-obj.tradeEnterPrice)*quantity
                  elif obj.trade_nature=="SHORT":
                        profit=(obj.tradeEnterPrice-obj.tradeExitPrice)*quantity



                  obj.tradeRecords['Trade Exit Price'].append(obj.tradeExitPrice)
                  obj.tradeRecords['Profit/Loss'].append(profit)
                  obj.tradeRecords['Trade Exit Time'].append(time.ctime(r['timestamp']))

                  obj.tradeEnterPrice=0
                  obj.tradeExitPrice=0
                  obj.tradeCurrStoploss=0 
            
            tradetimelist.append(r['timestamp'])
      print(dict_trade)
      print(obj.BBands)
      with open('data.json', 'w', encoding='utf-8') as outfile:
          json.dump(dict_trade, outfile, ensure_ascii=False, indent=2)
          json.dump(obj.tradeRecords, outfile, ensure_ascii=False, indent=2)
      time.sleep(60)
# swap the long and short strategies