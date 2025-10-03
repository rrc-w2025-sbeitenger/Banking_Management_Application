"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(1172010, 98765, -300, date(2025,9,30), -200, 0.08)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
print(chequing_account.get_service_charges())


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing_account.deposit(1300)
except ValueError as e:
    print(e)

print(chequing_account)
print(chequing_account.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(6436534, 84364, 2000.67, date(2010,10,2), 500)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
print(savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    savings_account.withdraw(1800)
except ValueError as e:
    print(e)

print(savings_account)
print(savings_account.get_service_charges())

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account_1 = InvestmentAccount(5429519, 46346, 5200.90, date(2020,10,1), 4)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account_1)
print(investment_account_1.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account_2 = InvestmentAccount(600000, 37584, 6000.90, date(2010,10,1), 4)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account_2)
print(investment_account_2.get_service_charges())


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(8.5)
except ValueError as e:
    print(e)

try:
    savings_account.withdraw(0.5)
except ValueError as e:
    print(e)

try:
    investment_account_1.withdraw(4.5)
except ValueError as e:
    print(e)

try:
    investment_account_2.withdraw(0.5)
except ValueError as e:
    print(e)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(f"{chequing_account}\n")
print(f"{savings_account}\n")
print(f"{investment_account_1}\n")
print(f"{investment_account_1}")
