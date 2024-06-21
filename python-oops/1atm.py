class Atm:
    #static/class variable are declared outside constructor
    # static/class variable has same value for every object
    __counter = 1

    def __init__(self) -> None:
        # instance variable are declared inside constructor
        # instance variable has different value for different object
        self.__pin = ""
        self.__balance = 0

        #static variable are used by using Class name not self
        self.sno = Atm.__counter
        Atm.__counter+=1
        self.__menu()
    
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not allowed")
        
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin 
            print("Pin Changed")
        else:
            print('Not allowed')
    
    def __menu(self):
        user_input =input("""
                        Hello, how would you like to proceed?
                          1. Enter 1 to create pin
                          2. Enter 2 to deposit
                          3. Enter 3 to withdraw
                          4. Enter 4 to check balance
                          5. Enter 5 to exit
                          """)
        
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposite()
        elif user_input=='3':
            self.withdrawl()
        elif user_input=='4':
            self.check_balance()
        else:
            print('bye')
    
    def create_pin(self):
        self.__pin = input('Enter your pin')
        print("Pin set successfully")
    
    def deposite(self):
        temp = input('Enter your pin')
        if temp == self.__pin:
            amount = int(input('Enter the amount'))
            self.__balance = self.__balance+amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")
    
    def withdrawl(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount<=self.__balance:
                self.__balance= self.__balance - amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Incorrect Pin!")
    
    def check_balance(self) -> None:
        temp = input('Enter your pin')
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
#2.31