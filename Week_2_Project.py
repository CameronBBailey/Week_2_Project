#Still need to read over for more ways to break the code but the basic shell should be functioning  

class parking_gragage():
    
    


    def __init__(self, parkingspaces, Price, tickets_sold = 0, currentTicket = dict()):
        self.parkingspaces = list(range(parkingspaces))
        self.tickets_sold = tickets_sold
        self.currentTicket = currentTicket
        self.Price = Price
    def takeTicket(self):
        self.placeholder = 0
        if self.parkingspaces == []:
            print(f'There are no spots currently avalible please try again at a different time')
            
        else:
            self.placeholder = self.parkingspaces.pop(0)
            self.currentTicket[self.placeholder] = False
            self.tickets_sold += 1
            print(f'Thank you and enjoy your stay! Your Ticket number is {self.placeholder}')

    def payForParking(self):
        self.ticketholder = input(f'Please enter your ticketnumber :') 
        #Validticketnumber check here
        self.monies = input(f'Please insert bills into the slot or swipe your credit card now with the correct amount :')
        if self.monies.isdigit() != True:
            print(f'Please try again and enter a valid amount of money')
        else:
            if (self.Price -int(self.monies)) != 0 :
                print(f'Please try again and enter exact change') #Find a way to store the value and allow payment in parts? Also allow for overpayment and change to be given
            else:
                print(f'Your ticket is paid and you are all set to leave, please be gone within the next 15 minutes')
                self.currentTicket[self.ticketholder] = True

    def leaveGarage(self): 
        self.ticketholder2 = int(input(f'Please enter your ticketnumber :')) 
        #Valid ticket # check here
        if self.currentTicket[self.ticketholder2] == True:
            print(f'Thank you and have a nice day')
            del self.currentTicket[self.ticketholder2]
            self.parkingspaces.append(self.ticketholder2)
            self.parkingspaces.sort()
        else:
            print(f'Please pay first before you leave!!!')
            self.payForParking()








G1 = parking_gragage(2,20)

G1.takeTicket()
G1.takeTicket()
G1.takeTicket()
print(G1.currentTicket)
 #Should keep looping until exactly 20$ is put in
G1.leaveGarage()