class Phone:

    def __inti__(self,price,brand,camera):
        print('Print inside phone Constructor')
        self.price = price 
        self.__brand = brand 
        self.camera = camera 
    

    def buy(self):
        print("Buying a phone")
    
    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone):
    
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera) # super should be the firs inside any function
        self.os = os 
        self.ram = ram 
        print("Inside smartphone constructor")

s = SmartPhone(2000,"Samsung",13,"Android",2)
s.buy() 