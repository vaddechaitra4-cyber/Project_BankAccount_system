#simple Bank account syatem
#this project demonstrates python oops concepts:
#features:
#deposit money
#withdraw money 
#check account balance

#BankAccount class create chesthunam
#this class handle deposit,withdraw and balance checking

class BankAccount:
#constructor - account create ayina appudu intial balance set chesthundhi
    def __init__(self,initial_amount=0):
        self.balance=initial_amount

#deposit function - account lo ki money add cheyadaniki

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"succesfully deposited ${amount}")
            print(f"current balence:${self.balance}")
        else:
            print("deposit amount must be positive!")

#withdraw function - account nunchi money withdraw cheyadaniki

    def withdraw(self,amount):
#withdrawal amount zero or negative unte invalid
        if amount<=0:
            print("withdrawal amount must be positive!")
#balance kanna ekkuva ekkuva withdraw cheyadaniki try chesthe error 
        elif amount>self.balance:
            print("insufficient balance!")
            print(f"available balance: ${self.balance}")
        else: 
            self.balance-=amount
            print(f" succesfully withdrawn $ {amount}")
            print(f"current balance:{self.balance}")
#account balance display cheyadaniki function
    def display_balance(self):
# Account balance display cheyadaniki function
        print("\n_____Account details______")
        print(f"current balance:${self.balance}")
        print("-----------------------\n")

print("welcome to simple bank system \n")
#user nundi initial amount input tisukuntam 
initial=float(input("enter a initial amount start account($):"))
#Bank account class object create chestham
account=BankAccount(initial)

#menu repeat avvadam kosam infinite loop use chestham 

while True:
    print("\n1. __ deposit___")
    print("\n2.__withdraw____")
    print("\n3.___check balance___")
    print("\n4.___exit___")
    choice=input("enter a your choice (1 to 4):")
    if choice=="1":
        amt=float(input("enter a deposit amount:"))
        account.deposit(amt)
    elif choice=="2":
        amt=float(input("enter withdrawal amount:"))
        account.withdraw(amt)
    elif choice=="3":
        account.display_balance()
    elif choice=="4":
        print("thank you for using our bank. bye! dear customer 🥰👋:$")
        break
    else:
        print("invalid choice! please enter 1,2,3 or 4.")