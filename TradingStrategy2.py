import numpy as np
from talib._ta_lib import BBANDS
import random
##NOTE TO UPDATE THE TIME LIST
class Trading_Strategy2:
    def __init__(self,dict_trade):
        self.list_trade=dict_trade['list_trade']
        self.BBands=[]
        #self.list_tradeTime=dict['list_tradeTime']
        self.trade_nature=""
        self.tradeEnterPrice=0
        self.tradeExitPrice=0
        self.tradeCurrPrice=0
        self.tradeCurrStoploss=0
        print("HELLO")
        self.tradeRecords={'Trade Enter Price':[],'Profit/Loss':[],'Trade Exit Price':[],'Trade Entry Time':[],'Trade Exit Time':[]}
        self.trade_LongStoploss=float(input("Enter the Stoploss for the long trade=>"))
        self.trade_ShortStoploss=float(input("Enter the Stoploss for the short Trade=>"))


    
    def __str__(self):
        return 'curr Price=>'+str(self.tradeCurrPrice)+'\tstoploss Price=>'+str(self.tradeCurrStoploss)


    def Calculate_BBands(self,list_trade):
        BBands=[]
        trade_array=np.asarray(list_trade)
        tuple_BBands=BBANDS(trade_array,20,2)
        for i in range(0,len(tuple_BBands)):
            BBands.append(tuple_BBands[i].tolist())
        return BBands


    def trade_Check(self,new_trade):
        self.BBands=self.Calculate_BBands(self.list_trade)
        self.list_trade.append(new_trade)
        self.tradeCurrPrice=new_trade

         #when current price in between two bands then donot pursue any trade
        if new_trade<self.BBands[0][-1] and self.tradeEnterPrice==0 and new_trade>self.BBands[2][-1]:
            return 'Currently Pursuing No trade'


        # Check Whether the current price is greater than the current value of Upper Band
        elif new_trade>self.BBands[0][-1] and self.tradeEnterPrice==0:
            
            self.tradeEnterPrice=new_trade
            print('Short Trade Entered at=>',self.tradeEnterPrice)
            self.trade_nature="SHORT"
            self.tradeRecords['Trade Enter Price'].append(self.tradeEnterPrice)
            self.tradeCurrStoploss=self.trade_LongStoploss*self.tradeEnterPrice
            print('Stoploss price=>',self.tradeCurrStoploss)
            return('Enter the trade')


        #Check whether the current price is lower than the current value of lower band
        elif new_trade<self.BBands[2][-1] and self.tradeEnterPrice==0:

            self.tradeEnterPrice=new_trade
            self.trade_nature="Long"
            print('Long Trade Entered at=>',self.tradeEnterPrice)
            self.tradeRecords['Trade Enter Price'].append(self.tradeEnterPrice)
            self.tradeCurrStoploss=self.trade_ShortStoploss*self.tradeEnterPrice
            print('Stoploss Price=>',self.tradeCurrStoploss)
            return('Enter the trade')

       #For an ongoing long trade Exit the trade whenever the price falls below the stoploss or update the stoploss to trail the current price
        elif self.trade_nature=="LONG":
            if new_trade<self.tradeCurrStoploss:
                print("Trade Exit at=>",new_trade)
                self.tradeExitPrice=new_trade
                return 'Exit Trade'
            if new_trade*self.trade_LongStoploss>self.tradeCurrStoploss:
                self.tradeCurrStoploss=new_trade*self.trade_LongStoploss
        
        #for an ongoing short trade Exit the trade whenever the price rises above the stoploss or update the stoploss to trail the current price
        elif self.trade_nature=="SHORT":
            if new_trade>self.tradeCurrStoploss:
                print("Trade Exit at=>",new_trade)
                self.tradeExitPrice=new_trade
                return 'Exit Trade'
            if new_trade*self.trade_ShortStoploss<self.tradeCurrStoploss:
                self.tradeCurrStoploss=new_trade*self.trade_ShortStoploss
        

        #for any ongoing trade if the price falls within the bollinger bands then exit the trade
        # elif new_trade<self.BBands[0][-1] or new_trade>self.BBands[2][-1]:
            # self.tradeExitPrice=new_trade
            # print("Trade Exit at=>",new_trade)
            # return 'Exit Trade'            
        self.Update_BBands(new_trade)
                       

    def Update_BBands(self,new_trade):
        newBBands=self.Calculate_BBands(self.list_trade[-20:])
        for i in range(len(self.BBands)):
            self.BBands[i].append(newBBands[i][-1])


      
# l=[]
# for i in range(20):
#     l.append(random.random()*40.000)
# obj=Trading_Strategy({'list_trade':l})
# print(obj)
# Bands=obj.Calculate_BBands(l)
# print(obj.list_trade,Bands)



# while i<100:
#     newtrade=random.random()*100.000
#     print('newtrade',newtrade)
#     status=obj.trade_Check(newtrade)
#     print(status)
#     if status=='Exit Trade':
#         obj.tradeEnterPrice=0
#         obj.tradeExitPrice=0
#         obj.tradeCurrStoploss=0 
#     i+=1
