class Car:

    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0


    def set_speed(self, speed):
        self.__speed = 0 if speed < 0 else speed

    
    def get_speed(self):
        return self.__speed


car1 = Car(2020, "Lamborghini", "Hurracan", 310)
car1.set_speed(240)
# print(car1._Car__speed)
# print(car1.get_speed())





class Account:

    def __init__(self, balance):
        self.__balance = balance

    
    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    
    def get_balance(self):
         return self.__balance


himraj_account = Account(2000)
himraj_account.deposit(500)
# print(himraj_account.get_balance())
himraj_account.withdraw(1000)
print(himraj_account.get_balance())

        
