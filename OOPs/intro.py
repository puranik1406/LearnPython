class Number:
    def __init__(self,value1,value2): #Constructor
        self.value1=value1
        self.value2=value2

    def info(self):
        print(f"The values passed are {self.value1} and {self.value2}")

    def greet(fx):#Decorator
        def sayhello(*args,**kwargs):
            print("Welcome to calculator, I am here to calculate for ya!")
            fx(*args,**kwargs)
        return sayhello
    @greet
    def calculate(self):
        print("The sum of these values is",self.value1+self.value2)
        print("The difference of these values is",self.value1-self.value2)
        print("The product of these values is",self.value1*self.value2)
        print("The division of these values are",self.value1/self.value2)

    @property #Property/Method/Getter
    def ten_value(self):
      return 10* (self.value1)
    
    @ten_value.setter #Setter
    def ten_value(self, new_value):
      self.value1 = new_value/10

class Exponent(Number):#SubClass(Inheritance)
    def power(self):
        print(f"{self.value1} power {self.value2} is equal to {self.value1 ** self.value2}")
    
    @staticmethod
    def any(a,b): #StaticMethod
        print(a**b)


a=Number(12,15)
a.info()
a.calculate()
a.ten_value=69
a.calculate()

num=Exponent(2,7)
num.power()
num.any(3,4)