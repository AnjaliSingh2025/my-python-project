# display available stocks
# Request a bike for rent(100 rs->1 qty)
# Exit
class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than 0")
        elif q>self.stock:
            print("Enter the Values (less the stock)")
        else:
            print("Total prices",q*100)
            print("Total Bikes",q)
while True:
    obj=bikeShop(100)
    uc=int(input('''
1.Display Stocks
2.Rent a bike
3.Exit
''')) 
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the qunatity:---"))
        obj.rentForBike(n)
    else:
        break