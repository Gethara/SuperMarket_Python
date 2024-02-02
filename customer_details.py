from datetime import date
class detail_form():
   ###taking main details from the user
   def __init__(self):
       self.input_NIC()
       self.input_TPNum()
       self.Date=str(date.today())


   ###taking rest of the details from the user    
   def print_form(self):
       while True:
          self.first_name=input("First name **:".ljust(20))
          if self.val_data(self.first_name):
                break
          else:
                print("\n\
                     !!!Please Enter a valid NIC No.!!!!\n\
                     \n")
       self.last_name=input("Last name :".ljust(20))
       self.address_line1=input("Address line 1: ".ljust(20))
       self.address_line2=input("Address line 2: ".ljust(20))
       self.address_line3=input("Address line 3: ".ljust(20))
       self.email=input("Email Address: ".ljust(20))


   ### add details to the txt File or cancel submission
   def add_details(self):
      while True:
          print("\n\
                 To Submit the form =====> type : 1\n\
                 To cancel submission and goback ====> type: 2\n\
                 \n")
          
          status=input("please Enter a number: ")
          if status=="1":
               print("Thank you!! successfully submitted!!")
               with open("customer_details.txt","a") as file1:
                    file1.write("{:20s}{:20s}{:20s}{:20s}{:20s}{:20s}{:20s}{:20s}{:20s}\n".format(self.NIC,
                                                                                           self.TPnumber,
                                                                                           self.Date,
                                                                                           self.first_name,
                                                                                           self.last_name,
                                                                                           self.address_line1,
                                                                                           self.address_line2,
                                                                                           self.address_line3,
                                                                                           self.email))
                    
                    
               break
          elif status=="2":
             break
          else:
            print("................!!!!Invalid Number try again!!..............")

           

   ##check the validity of NIC number
   def val_NIC(self,nic):
      oldnic= len(nic)== 10 and nic[:9].isdigit() and (nic[-1]=="v" or nic[-1]=="x")
      newnic= len(nic)== 12 and nic[:].isdigit()
      if (oldnic or newnic):
         return True


   ##check the validity of TP number
   def val_TPnum(self,tnum):
      if (len(tnum)==10) and tnum.isdigit():
          return True


   ## check the validity of input data
   def val_data(self,data):
      if data!=" ":
         return True


   ##Heading of the cutomer detail form
   def Heading(self):
      print( "\n\
                ***********  Customer Detail Form ***********\n\
             ----------- compulsury infomation is with ** -------------\n\
          >>>>> help us by filling the form with true information <<<<<<\n\
             \n")


   ##take NIC as a user input 
   def input_NIC(self):
       while True:
          self.NIC=input("Enter NIC number** : ")
          if self.val_NIC(self.NIC):
             break
          else:
             print("\n\
                  !!!Please Enter a valid NIC No.!!!!")


   ##take TP number as a user input
   def input_TPNum(self):
       while True:     
          self.TPnumber=input("Enter Telephone number** : ")
          if self.val_TPnum(self.TPnumber):
             break
          else:
             print("\n\
                  !!!Please Enter a valid Tele Phone No.!!!!")


       
             
             

  
