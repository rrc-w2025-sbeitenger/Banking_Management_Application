"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client


# 2. Create a Client object with data of your choice.
try:
    client_1 = Client(123456, "John", "Marathon", "John.Marathon@pixel-river.com")
except ValueError as e:
    print(e)
    #traceback.print_exc()


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    johnChequingAccount = ChequingAccount(987654, 123456, 1000, date(2025, 10, 20), 1000, 0.08)
except Exception as e:
        print(e)

try:
    johnSavingAccount = SavingsAccount(765432, 123456, 20000.56, date(2025, 9, 20), 1000)
except Exception as e:
        print(e)
        

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
try:
    johnChequingAccount.attach(client_1)
except Exception as e:
        print(e)

try:
    johnSavingAccount.attach(client_1)
except Exception as e:
        print(e)
       

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_2 = Client(192837, "Astrid", "Iron", "Astrid.Iron@pixel-river.com")
except Exception as e:
        print(e)

try:  
    astridSavingAccount = SavingsAccount(273645, 192837, 3000.79, date(2025, 8, 10), 200)
except Exception as e:
        print(e)

try:
    astridSavingAccount.attach(client_2)
except Exception as e:
        print(e)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.


#John chequingAccount
try:
    johnChequingAccount.withdraw(960)
except Exception as e:
        print(e)

try:
    johnChequingAccount.deposit(950)
except Exception as e:
        print(e)

try:
    johnChequingAccount.withdraw(960)
except Exception as e:
        print(e)


#John Savings account
try:
    johnSavingAccount.withdraw(100)
except Exception as e:
        print(e)

try:
    johnSavingAccount.withdraw(1000)
except Exception as e:
        print(e)

try:
    johnSavingAccount.deposit(15000)
except Exception as e:
        print(e)
       

#astrid savings account
try:
    astridSavingAccount.withdraw(0.79)
except Exception as e:
        print(e)

try:
    astridSavingAccount.deposit(1000)
except Exception as e:
        print(e)

try:
    astridSavingAccount.withdraw(3960)
except Exception as e:
        print(e)
