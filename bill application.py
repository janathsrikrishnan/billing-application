#simple billing application for small store


############### WARNING ####################
##this program is not dynamic type once#####    
##generate the bill we cannot change the####
##values                                ####
############################################
import datetime, time

#want to complete
#1 want to implement command line for best text based user interface
#2 after implemented storage type change to persistent
#3 want to implement new memory allocation for every month and ask the user want to keep the old records or not
#4 Important : generatebill doesnot print in allined want fix this first 
#5 want to complete buyerslist in bill which print the buyers name and the purchased products
#not implemented analysis, graph, log entry, persistent storage

#item will manage items in the list and it also a main part of application

#############################################
################# REFERENCE #################
### 1. for access price in self.itemsbook ###
###    just 'price'                       ###
### 2. for access name in self.buyerbook  ###
###    just 'name'                        ###
### 3. for date just 'date'               ###
### 4. for time just 'time'               ###
### 5. total: 'Total'                     ###
### 6. stock or quantity : 'stock'        ###
#############################################




class item:
    def __init__(self):
        self.itembook = {}

#print the item in items with thier price
    def printitems(self):
        user = input("Enter the item to see: ")
        if user == 'all' or user == 'a':
            print("START".center(40, '-'))
            print("""Name\t\t\t\tPrice\t\t\tStock""")
            for i in self.itembook:
                print(i.ljust(20), str(self.itembook[i]['price']).center(24),str(self.itembook[i]['stock']).rjust(14))
            print("END".center(40, '-'))

        else:
            print("START".center(40, '-'))
            print(user, ":",'  Price :',self.itembook[user]['price'], '  stock:', self.itembook[user]['stock'])
            print("END".center(40, '-'))
#insert the item in the list with their price and total stock  

    def insertitem(self):

    #ask the user to enter the name of the item
    #if user enter exit it come out from the insert the item
        

        Name = input("Enter the item name you want to insert in the list: ")
        while Name != 'e':

    #ask the user to enter item price and quantity
    #store the price and quantity in another dictionary and assign to name of the item (refer line 32)

            price = self.getnumber("Enter the price of the %s :"%(Name))
            quantity = self.getnumber("Enter the stock(quantity) of the %s :"%(Name))
            self.itembook[Name] = {"price":price, "stock":quantity}

    #after inserting the item show the user updated successfully

            print("item : %s, price :%i stock: %i is successfully updated"%(Name, self.itembook[Name]['price'], self.itembook[Name]['stock']))
            Name = input("Enter the item name you want to insert in the list or 'e' to exit: ")
        self.printitems()   
        
    #getnumber allow the user to enter only number
    def getnumber(self, promt):
        price = input(promt)
        while not price.isnumeric():
            price = input(promt)
        return int(price)

    def instructions(self):
        print("Warning: if two are same but different brand ")
        print("Enter separatly with brand name if you want to show seperatly")
        print("or enter item name if the items are mixed")

class bills(item):

    #initialize with items so that bill can use items attributes
    def __init__(self):
        self.items = item()
        self.billbook = {}
        self.buyerbook = {}
        self.itembook = self.items.itembook

    def billing(self):
        name= input("Buyer Name :")                  #ask the buyer name  (user)                                  
        itemName = input("Item Name :")              #ask the items (user)
        billNo = len(self.billbook) +1                    #compute the billno (computer part)
        self.billbook[billNo] = {}                   #create billno as key in bill book and assign value dict (computer)
        self.buyerbook[billNo] = {}
        self.buyerbook[billNo]['name'] = name
        while itemName != 'e':                       #to end the process enter 'e'(computer)
            if itemName in self.items.itembook:
                quantity = self.items.getnumber("Enter the quantity :")
                if quantity <= self.items.itembook[itemName]['stock']:
                    self.billbook[billNo][itemName] = quantity
                    self.itembook[itemName]['stock'] = self.itembook[itemName]['stock'] - quantity
                    
                else:
                    print("stock avaliabe for %s :"%(itemName), self.itembook[itemName]['quantity'])
            else:
                print("There is no item %s in item list"%(itemName))
            
            itemName = input("Item Name :")
        self.generatebill(billNo)

#generatebill functions will generate the bill after the buyer add required items in cart.
# it first take the bill no
# date and time
# buyers name
# items the buyers added to the cart
#
    def generatebill(self, billNo):
        dateTime = datetime.datetime.now()
        date = str(dateTime.day) +'-'+str(dateTime.month)+'-'+str(dateTime.year)
        time = str(dateTime.hour)+':'+str(dateTime.minute)
        print('-'*60, '\n'*2)
        print('billNo :%i'.ljust(10)%(billNo), 'Time :%s'.center(10)%(time), 'Date :%s'.rjust(10)%(date))#want to fill date in formate place
        print('Name :%s'.ljust(25)%(self.buyerbook[billNo]))
        print('-'*60)
        print("""S.no\titems\t\tqty\tprice\ttotal""")
        print('-'*60)
        Sno = 1
        total = 0
        for i in self.billbook[billNo]:
            subTotal = self.billbook[billNo][i]*self.itembook[i]['price']
            print('%i'.ljust(8)%(Sno),'%s'.ljust(16)%(i),'%i'.ljust(4)%(self.billbook[billNo][i]),'%i'.ljust(6)%(self.itembook[i]['price']),'%i'.ljust(6)%(subTotal))
            total += subTotal
        print('-'*60)
        print('Total : %i'.rjust(38)%(total))
        self.billbook[billNo]['Total'] = total
        self.buyerbook[billNo]['Total item'] = len(self.billbook[billNo]) - 1
        self.buyerbook[billNo]['Total'] = total
        self.buyerbook[billNo]['date'] = date
        self.buyerbook[billNo]['time'] = time


#buyer list it  show the bills
#take input bill number start and end
#if you want to see only one bill enter start and end same number
#buyerlist just collabarate self.items.book, self.buyerbook, self.billbook
    def buyerslist(self):
        askUser = self.items.getnumber('Enter the starting range of bill :')
        endUser = self.items.getnumber('Enter the End range of bill :')
        while endUser not in self.buyerbook:
            print('please enter valid range')
            endUser = self.items.getnumber('Enter the End range of bill :')
        print('='*60, '\n'*2)
        
        for i in range(askUser, endUser+1):
            
            print('Bill no :%s     Name :%s     Date :%s     Time: %s'%(i, self.buyerbook[i]['name'], self.buyerbook[i]['date'], self.buyerbook[i]['time']))
            print('Total items :%s     Total cost :%s'%(self.buyerbook[i]['Total item'], self.buyerbook[i]['Total']))
            print('Items :')
            for j in self.billbook[i]:
                if j != 'Total':
                    print('item Name :%s     Qty :%s    price :%s      Total :%s'%(j, self.billbook[i][j], self.itembook[j]['price'], self.billbook[i][j]*self.itembook[j]['price']))
            print('\n'*2, '='*60)

#user interaction part
#it depend on user input only

def main():
    print('Thanks for selecting JSK\'s bill generator')
    print('"insert" item, "bill" for bill, "items" for view items added to list and "help" for help')
    bill = bills()
    print("-"*60, '\n'*2)
    print('Command >>>', end = '')
    user = input().lower()
    while True:
        if user == 'insert' or user == 'i':
            bill.insertitem()
        elif user == 'bill' or user == 'b':
            bill.billing()
        elif user == 'help' or user == 'h':
            help()
        elif user == 'view' or user == 'v':
            bill.printitems()
        elif user == 'buyers' or user == 'buy':
            
            bill.buyerslist()
        else:
            print("Sorry, %s command is not exits"%(user))
        print('\n'*2, '-'*60)
        print('Command >>>', end = '')
        user = input().lower()

def help():
    print("""
'INSERT' or 'I' or 'Insert or 'insert' or 'i' for inserting item in list
'BILL' or 'B' or 'Bill' or 'bill' or 'b' for putting bill
'HELP' or 'H' or 'help' or 'h' for help
'buy' to see the billbook 
Tip :
     1. For changing values in item enter the item name and enter the current values
     2. want to fill
""")
    
main()
