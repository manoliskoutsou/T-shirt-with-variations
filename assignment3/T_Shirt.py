import abc

class Strategy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def payment(self):
        pass
 
'''T-shirt with different prices for color, size and fabric'''
class TShirt:
    
    color_price = 30
    size_price = 20
    fabric_price = 50
    

    def __init__(self):
        self.color = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET"]
        self.size = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
        self.fabric = ["WOOL", "COTTON", "POLYESTER", "RAYON", "LINEN", "CASHMERE", "SILK"]
         
    @staticmethod  
    def setPrice():
        total_price = TShirt.color_price + TShirt.size_price + TShirt.fabric_price
        return total_price
    
'''Final price with cash'''   
class Cash(Strategy):
    def payment(self):
        price = TShirt.setPrice()
        return price
    
'''Final price with credit card and discound''' 
class CreditCard(Strategy):
    def payment(self):
        price = TShirt.setPrice()
        return price - (price * 0.20)
    
''' Final price with money transfer and extra cost'''   
class Transfer(Strategy):
    def payment(self):
        price = TShirt.setPrice()
        return price + 5
    
'''Execute strategy''' 
class Payment:
    def __init__(self, strategy):
        self.strategy = strategy
        
    def executeStrategy(self):
        return self.strategy.payment()
    

'''All t-shirt with Cash method'''
def allTshirtWithCash():
    tshirt = TShirt()
    payment = Payment(Cash())
    for c in tshirt.color:
        for s in tshirt.size:
            for f in tshirt.fabric:
                print(f"A t-shirt with color : {c}, size : {s}, fabric : {f} and price : {payment.executeStrategy()}$")
                

'''All t-shirt with Credit Cards method'''
def allTshirtWithCreditCards():
    tshirt = TShirt()
    payment = Payment(CreditCard())
    for c in tshirt.color:
        for s in tshirt.size:
            for f in tshirt.fabric:
                print(f"A t-shirt with color : {c}, size : {s}, fabric : {f} and price : {payment.executeStrategy()}$")
                
'''All t-shirt with Transfer method'''
def allTshirtWithTransfer():
    tshirt = TShirt()
    payment = Payment(Transfer())
    for c in tshirt.color:
        for s in tshirt.size:
            for f in tshirt.fabric:
                print(f"A t-shirt with color : {c}, size : {s}, fabric : {f} and price : {payment.executeStrategy()}$") 

'''menu : all variation of t-shirt with different payment''' 
def menu():
    print("Methods of payment : \n1 Payment method : Cash \n2 Payment method : Credit Cards \n3 Payment method : Transfer \n4 Exit ")
    
    while True:
        try:
            choice = int(input("Please pick a choice : "))
            if choice == 1 :
                allTshirtWithCash()
                menu()
            elif choice == 2 :
                allTshirtWithCreditCards()
                menu()
            elif choice ==  3 :
                allTshirtWithTransfer()
                menu()
            elif choice == 4 :
                exit()
            else:
                print("Invalid Selection! Please Try Again!")
                menu()
        except ValueError:
            print("No valid integer! Please try again")
            menu()
            
menu()
            
            

    
    
    

    