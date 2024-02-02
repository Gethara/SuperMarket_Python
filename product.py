class Product:
    def __init__(self,productName):
        self.productName=productName
        

    def autoUpdateQuantity(self,boughtQuantity):
        productList=[]
        productQuantity=[]
        with open("product.txt","r") as file:
            for line in file:
                product,quantity=line.strip().split(" ")
                productList.append(product)
                productQuantity.append(int(quantity))
            if (self.productName in productList) or productList.index(self.productName)!=0 :
                productQuantity[productList.index(self.productName)]=productQuantity[productList.index(self.productName)]-boughtQuantity
            else:
                print("{self.productName out of the stock")

        with open("product.txt","w") as file:
             for i in range(len(productList)-1):
                 file.write(productList[i]+ " "+ str(productQuantity[i])+ "\n")
             else:
                 file.write(productList[-1]+" "+ str(productQuantity[-1])+"\n")

    def manuallyUpdateQuantity(self,boughtQuantity,unitPrice):
        productList=[]
        productQuantity=[]
        with open("product.txt","r") as file:
            for line in file:
                product,quantity=line.strip().split(" ")
                productList.append(product)
                productQuantity.append(int(quantity))
        if (self.productName in productList):
                if productQuantity[productList.index(self.productName)]-boughtQuantity>=0 :
                     productQuantity[productList.index(self.productName)]=productQuantity[productList.index(self.productName)]-boughtQuantity
                else:
                    print(f"remaining Quantity is less than bought quantity. remaining quantiy = {productQuantity[productList.index(self.productName)]}")
        
##        with open("price.txt","w") as file:
##            for i in range(len(product)-1):
##                 file.write(productList[i]+ " "+ str(productQuantity[i])+ "\n")
##            else:
##                 file.write(productList[-1]+" "+ str(productQuantity[-1])+"\n")

        with open("product.txt","w") as file:
            for i in range(len(product)-1):
                file.write(productList[i]+ " "+ str(productQuantity[i])+ "\n")
            else:
                file.write(productList[-1]+" "+ str(productQuantity[-1])+"\n")

##Apple=Product("Apple",35)
##Apple.autoUpdateQuantity(5)

     
