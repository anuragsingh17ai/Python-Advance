class Fraction:
    def __init__(self,n,d) -> None:
        self.num = n
        self.den = d
    
    def __str__(self) -> str:
        return f'{self.num}/{self.den}'
    
    def __add__(self,other) -> str:
        temp_num = self.num*other.den + other.num*self.den 
        temp_den = self.den * other.den 
        return f'{temp_num}/{temp_den}'
    
    def __sub__(self,other) -> str:
        temp_num = self.num * other.den - other.num * self.den 
        temp_den = self.den * other.den 
        return f'{temp_num}/{temp_den}'
    
    def __mul__(self,other) -> str:
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return f'{temp_num}/{temp_den}'
    
    def __truediv__(self,other) -> str:
        temp_num = self.num * other.den 
        temp_den = self.den * other.num
    
    #1.23