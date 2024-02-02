from CustomerSide import *
print("### --------- WELCOME TO THE PANADURA FOODCITY---------###")
while True:
    print("+----Enter Number to access the system----+")
    print("SYSTEM \n 1) Type 1 : Enter to shop management \n 2) Type 2 : Enter to Customer side")

    number = int(input("Enter Number : "))
    while True:    
        if number == 1:
            userName = input("Enter user name : ")
            password = input("Enter Password : ")
            if userName == "foodcity" and password == "12345":
                print("+-----Welcome to Shop management-----+")
                print("Task for Salesman: \n 1) Type 1: Create a bill \n 2) Type 2: Add new product to shop \n 3) Type 3: Update Product")
                response = int(input("Enter Number : "))
                while True:
                    if response == 1:
                        print("Create Bill")
                    elif responce == 2:
                        print("Add item")
                    elif responce == 3:
                        print("update item")
                    else:
                       print("invalid response")
                       response = int(input("Enter Number : "))
            else:
                pass
                
        elif number == 2:
            print("=-=-==-=-=-=-=-=-=-=-= Welcome to the =-=-=-=-=-=-=-=-=-=-=-=")
            Customer()
        else:
            print("invalid response")
            number = int(input("Enter Number : "))
