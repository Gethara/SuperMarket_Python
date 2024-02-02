from datetime import date
from datetime import time

class Bill:
    def __init__(self,productList,unitPrice,quantity):
        self.date = str(date.today())
        self.productLis = productList
        self.unitPrice = unitPrice
        self.quantity = quantity

    def printBillHead(self):
        print("+--------------------------------------------+")
        print("|                FOODCITY                    |")
        print("+--------------------------------------------+")
        print("| Date :  {:35s}|".format(self.date))

    def printBillFooter(self):
        print("|        Thank You.Come Again                |")
        print("+--------------------------------------------+")

    def getTotal(self):
        l = len(self.productLis)
        subToLis = []
##        ["apple","mango","banana"]
##        [12,10,40]
##        [40,30,15]
        for value in range(l):
            subTot = self.quantity[value] * self.unitPrice[value]
            subToLis.append(subTot)
        print("Total price is Rs."+str(sum(subToLis)))

    def printBill(self,paid):
        l = len(self.productLis)
        subToLis = []
        self.printBillHead()
        print("+----------------+--------------+------------+")
        print("| Name           |Quantity      |Price       |")
        print("+----------------+--------------+------------+")
        for value in range(l):
            subTot = self.quantity[value] * self.unitPrice[value]
            subToLis.append(subTot)
            print("|{:16s}|{:14s}|{:12s}|".format(self.productLis[value],"  "+str(self.quantity[value]),"  "+str(subTot)))
            print("+--------------------------------------------+")
        print("|Total : Rs{:34s}|".format(str(sum(subToLis))))
        print("+--------------------------------------------+")
        print("|Balance : Rs{:32s}|".format(str(paid-sum(subToLis))))
        print("+--------------------------------------------+")
        self.printBillFooter()

