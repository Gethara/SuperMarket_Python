from place_order import Items
from  customer_details import detail_form
class Customer():
    def __init__(self):
        print("*"*20+" CUSTOMER SIDE "+"*"*20+"\n")
        print("\n\
                 MENU\n\
              1.Place an order\n\
              2.detail form\n\
              3.available products\n\
              4.Back\n\
              \n")
        
        task=input("please Enter the task number :")
        if task=="1":
            self.task1()
        elif task=="2":
            self.task2()
        elif task=="3":
            self.task3()
        elif task=="4":
            pass
        else:
            print("Invalid Number!!! Try again!!")
         


    def task1(self):
        p=Items()
        p.sep_list()
        while True:
            print("\n\
                    MENU\n\
                  1.place a new order\n\
                  2.add new items to the ordered list\n\
                  3.remove items from the ordered list\n\
                  4.update items in the ordered list\n\
                  5.print my ordered list\n\
                  6.confirm order\n\
                  7.back\n\
                  \n")
            status=input("Please Enter a number: ")
            
            if status=="1":
                p=Items()
                p.sep_list()
            elif status=="2":
                p.add_items()
            elif status=="3":
                p.remove_items()
            elif status=="4":
                p.update_items()
            elif status=="5":
                p.print_list()
            elif status=="6":
                p.confirm_order()
                break
            elif status=="7":
                break
            else:
                print("!!!!Invalid number. Try again!!!!")

        
    def task2(self):
        customer=detail_form()
        customer.Heading()
        customer.print_form()
        customer.add_details()
        while True:
            print("\n\
            ***********  Customer Detail Form ***********\n\
                    MENU\n\
                  1.new form\n\
                  2.Back\n\
                  \n")
            status=input("Please Enter a number :")
            
            if status=="1":
               customer=detail_form()
               customer.print_form()
               customer.add_details()
            elif status=="2":
                break
            else:
                print("Invalid Number!!")
            
    def task3(self):
        while True:
            print("\n\
                    MENU\n\
                  1.Continue\n\
                  2.Exit\n\
                  \n")
            status=input("Please Enter Number:")
            if status=="1":
                p=Items()
                item=input("Type Item here: ")
                if p.available_product(item.title()):
                    print(f"---------------------{item} is Available-------------")
                else:
                    print(f"---------------------{item} is not Available---------------")
            elif status=="2":
                break
    
