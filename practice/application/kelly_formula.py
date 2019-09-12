

import math

from pandas import DataFrame, Series
import re
import xlrd
import pandas as pd
import numpy as np

class Stock(object):

    nextIdNum = 0  # identity card

    def __init__(self, name):
        self.name = name
        # self.cash = None
        self.market = None
        self.company = None
        self.each_hand = None
        self.price = None
        self.volume = None
        self.idNum = Stock.nextIdNum
        self.currency_properities = 'HKD'

        Stock.nextIdNum += 1
    def  get_name(self):
        return self.name
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    def set_eachhand(self, stock_num):
        self.each_hand = stock_num
    def get_eachhand(self):
        return self.each_hand
    def set_currency(self, currency):
        self.currency_properities = currency
    def get_currency(self):
        return self.currency_properities

    # def set_cash(self, cash):
    #     self.cash = cash
    def set_company(self, company):
        self.company = company
    def set_volume(self, volume):
        self.volume = volume

    def set_market(self, market):
        self.market = market

    def getIdnum(self):
        return self.idNum
    def __str__(self):
        return self.name + ':\n'\
               +'the price is '+str(self.price)

class Account(object):
    def __init__(self):
        self.stocks = []
        self.own_stocksnum = {}
        self.own_stockscash = {}
        self.isSorted = True

    def addstock(self,stock):
        if stock in self.stocks:
            raise ValueError('Duplicate student')

        self.stocks.append(stock)
        self.own_stocksnum[stock] = 0
        self.own_stockscash[stock] = 0

        self.isSorted = False

    def setstock_num(self,stock,num):
        try:
            self.own_stocksnum[stock] = num
        except:
            raise ValueError('Stock not in mapping')
    def setstock_cash(self,stock,acc):
        try:
            self.own_stockscash[stock] = acc
        except:
            raise ValueError('Stock not in mapping')

    def getstocks(self):
        # if self.isSorted == False:
        #     self.stocks.sort()
        #     self.isSorted = True
        for s in self.stocks:
            yield s
    # def getstocks(self):
    #     if self.isSorted == False:
    #         self.stocks.sort()
    #         self.isSorted = True
    #     return self.stocks[:]

    def getown_stock_num(self,stock):
        try:
            return self.own_stocksnum[stock]
        except:
            raise ValueError('Stock no in mapping')
    def getown_stock_cash(self,stock):
        try:
            return self.own_stockscash[stock]
        except:
            raise ValueError('Stock no in mapping')
#




class Trade(object):

    def __init__(self, account, stock_name):
        self.account = account
        self.stock_name = stock_name
        self.own_stocks = account.getown_stock_num(stock_name)
        self.stock_value = self.own_stocks * stock_name.get_price()
        self.stock_cash = account.getown_stock_cash(stock_name)
        self.value = self.stock_cash + self.stock_value
        self.operate_stock = 0


    def change_money(self, money):
       self.stock_cash += money
       self.account.setstock_cash(self.stock_name,self.stock_cash)
    # def operate_stock(self, stock_num):
    #     self.own_stocks += stock_num
    #     # self.operate_stock = stock_num
    #     self.account.setsstock_num(self.stock_name, self.own_stocks)
    def change_stock(self, stock_num):
        self.own_stocks += stock_num
        self.operate_stock = stock_num
        self.account.setstock_num(self.stock_name,self.own_stocks)

    def kelly_operate(self, price):
        value =  price * self.own_stocks + self.stock_cash
        operate_stock = (value/2.0) / price - self.own_stocks
        if abs(operate_stock * price) >= 18 and abs(operate_stock) >= self.stock_name.get_eachhand() :
            self.operate_stock = operate_stock // self.stock_name.get_eachhand() * self.stock_name.get_eachhand()
        else:
            self.operate_stock = 0
        self.own_stocks += self.operate_stock
        stock_value = self.own_stocks * price
        self.stock_cash = value - stock_value
        self.account.setstock_cash(self.stock_name, self.stock_cash)
        self.account.setstock_num(self.stock_name, self.own_stocks)

    def get_stockcash(self):
        return self.stock_cash

    def get_stocknum(self):
        return self.own_stocks
    def get_operatestock(self):
        return self.operate_stock
    def get_stockname(self):
        return self.stock_name
    def get_currency(self):
        return self.stock_name.get_currency()



def tradeReport(trade):

    report = ''
    if trade.get_operatestock() != 0:
        if trade.get_operatestock() > 0:

            report = report +'\n'\
                     + trade.get_stockname().get_name() +': buy ' + str(int(trade.get_operatestock())) + ' stocks'+'\n'\
                     + trade.get_stockname().get_name() + '\'s cash_acc = ' + str(trade.get_stockcash()) + trade.get_currency()
        else:
            report = report +'\n'\
                     + trade.get_stockname().get_name() +': sell ' + str(int(-trade.get_operatestock())) + ' stocks'+'\n'\
                     + trade.get_stockname().get_name() + '\'s cash_acc = ' + str(trade.get_stockcash()) + trade.get_currency()
    else:
        report = trade.get_stockname().get_name()+ ': no need to transaction'


    return report



data = xlrd.open_workbook('just_bb/kelly_formula.xlsx')

s1 = data.sheets()[0]

# nr = s1.nrows
#
value1 = s1.cell_value(6,6)

print (type(value1))


def get_csv_num(columns,index):
    df = pd.read_csv('just_bb/kelly_formula.csv', header=None,nrows=12)
    string_list = re.findall(r'-?\d+\.?\d*e?-?\d*?', df[columns][index])
    return float(''.join(string_list))
#提取单元格中的数字部分

def get_xlsx_num(row,col):
    data = xlrd.open_workbook('just_bb/kelly_formula.xlsx')
    s1 = data.sheets()[0]
    return s1.cell_value(row,col)


s1 = Stock(get_xlsx_num(6,1))
s2 = Stock(get_xlsx_num(7,1))
s3 = Stock(get_xlsx_num(8,1))
s1.set_price(get_xlsx_num(6,4))
s1.set_currency('HKD')
s1.set_eachhand(get_xlsx_num(6,2))
s2.set_price(get_xlsx_num(7,4))
s2.set_currency('HKD')
s2.set_eachhand(get_xlsx_num(7,2))
s3.set_price(get_xlsx_num(8,4))
s3.set_currency('HKD')
s3.set_eachhand(get_xlsx_num(8,2))

# s1.get_currency()


# print type(s1.get_price())
HK_account = Account()
#
HK_account.addstock(s1)
HK_account.addstock(s2)
HK_account.addstock(s3)

# HK_account.setstock_num(s1,0)
# HK_account.setstock_cash(s1,100)
T1 = Trade(HK_account,s1)
T2 = Trade(HK_account,s2)
T3 = Trade(HK_account,s3)
# T1.kelly_operate(100,10)

T1.change_money(get_xlsx_num(6,7))
T2.change_money(get_xlsx_num(7,7))
T3.change_money(get_xlsx_num(8,7))
#
T1.change_stock(get_xlsx_num(6,3))
T2.change_stock(get_xlsx_num(7,3))
T3.change_stock(get_xlsx_num(8,3))
# T1.kelly_operate(1)

T1.kelly_operate(get_xlsx_num(6,5))
T2.kelly_operate(get_xlsx_num(7,5))
T3.kelly_operate(get_xlsx_num(8,5))
# T1.operate_stock(5)
# print T1.get_stocknum()
# print T1.get_stockcash()
# print T1.get_operatestock()
print (tradeReport(T1))
print (tradeReport(T2))
print (tradeReport(T3))


for s in HK_account.getstocks():

    print (s.get_name()+':\n'\
                       +'own_stock = '+str(HK_account.getown_stock_num(s))+'\n'\
                       +'cash_acc = '+str(HK_account.getown_stock_cash(s)) + s.get_currency())

