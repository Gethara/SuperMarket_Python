from Bill import Bill
from product import Product
class Items():
    def __init__(self):
        self.items=[]
        self.amount=[]
        self.unit_price=[]
    ##take items and quantity as user inputs and add to seperate lists
    def sep_list(self):
        try:
            print("\n\
                  place your order in the format, \n\
                           item1_amount item2_amount item3_amount\n\
                           eg: apple_50 banana_10 Mango_10\n\
                           \n")
            order=input("type your order here: ").strip().split(" ")
            
           
            for item in order:
                list1=item.split("_")
                if len(list1)<2:
                     print("invalid format. please try again")
                else:
                    if self.available_product(list1[0].title()):
                        if not self.limited_amount(list1[0],int(list1[1])):
                              self.items.append(list1[0].title())
                              self.amount.append(int(list1[1]))
                        else:
                            print(f"Limited no of {list1[0]} in the stock")
                    else:
                        print(f"{list1[0]} is out of stock")
        except ValueError as Error1:
           print("Invalid amount entered")
        except IndexError as Error2:
           print("Invalid Format. Please try again!!")
    ##update the product.txt file and print the bill        
    def confirm_order(self):
        if len(self.items)>0:
          while True:
            try:
                up=self.unit_price_list(self.items)
                b=Bill(self.items,up,self.amount)
                b.getTotal()
                paid=int(input("pay here :"))
                b.printBill(paid)
            except ValueError as error1:
                print("\n\
                      Please Pay. if you want to cancell the order type '#'")
            else:
                for item in self.items:
                    p=Product(item)
                    p.autoUpdateQuantity(self.amount[self.items.index(item)])
                break
        else:
            print("sorry! Can not print the bill.Nothing has been ordered")
    ##check if the product is in the stock
    def available_product(self,item):
        
        self.productList=[]
        self.productQuantity=[]
        with open("product.txt","r") as file:
            for line in file:
                product,quantity=line.strip().split(" ")
                self.productList.append(product)
                self.productQuantity.append(int(quantity))
        if item.title() in self.productList:
             return True
        else:
            return False
      
    ##check if the stock quantity is less than the ordered amount
    def limited_amount(self,item,amount):
       if self.available_product(item.title()):
            if self.productQuantity[self.productList.index(item.title())]<amount:
                    return True
            else:
                return False
    ##add new items to the list before conferm
    def add_items(self):
        try:
            new_items=input("add new items here: ").strip().split(" ")
            
           
            for item in new_items:
                list1=item.split("_")
                a=list1[0].title()
                if a in self.items:
                    print(f"{a} is already in the order list. Please use 'update' option to edit amount")
                else:
                    if self.available_product(list1[0].title()):
                        if not self.limited_amount(list1[0],int(list1[1])):
                              self.items.append(list1[0].title())
                              self.amount.append(int(list1[1]))
                        else:
                            print(f"Limited no of {list1[0]} in the stock")
                    else:
                        print(f"{list1[0]} is out of stock")
        except ValueError as Error1:
           print("Invalid amount entered")
        except IndexError as Error2:
           print("Invalid Format. Please try again!!")
    ## remove items from the list before confirm 
    def remove_items(self):
        try:
            remove_items=input("type the items to be removed  here: ").strip().split(" ")
            
           
            for item in remove_items :
                a=item.title()
                if a in self.items:
                    self.amount.pop(self.items.index(a))
                    self.items.remove(a)
                    print(f"{a} was removed from the order list")
                else:
                    print(f" you have not ordered {a} to remove")
        except ValueError as Error1:
           print("Invalid amount entered")
        except IndexError as Error2:
           print("Invalid Format. Please try again!!")
        
    ## update items in the list before confirm
    def update_items(self):
        try:
            update_items=input("type the items to be updated here: ").strip().split(" ")
            for item in update_items:
                list1=item.split("_")
                a=list1[0].title()
                if a in self.items:
                  b=self.amount[self.items.index(a)]
                  self.amount[self.items.index(a)]= int(list1[1])
                else:
                    print(f"still {a} is not in the ordered list. Therefore it cannot be updated")
        except ValueError as Error1:
           print("Invalid amount entered")
        except IndexError as Error2:
           print("Invalid Format. Please try again!!")

    ## making the unit price list for given product list 
    def unit_price_list(self,list1):
        self.productList2=[]
        self.productPrice=[]
        with open("price.txt","r") as file:
            for line in file:
                product,price=line.strip().split(" ")
                self.productList2.append(product)
                self.productPrice.append(int(price))
        for item in list1:
            a=item.title()
            if a in self.productList2:
                self.unit_price.append(self.productPrice[self.productList2.index(a)])
        return self.unit_price
    ##print the current items in the order list    
    def print_list(self):
          print("\n\
================The Item list You Ordered================================")
          for item in self.items:
              print(item,self.amount[self.items.index(item)])
          print(" ")
