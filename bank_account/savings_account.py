"""
Description: A class to savings account
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"

#imports
from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    InvestmentAccount class: Represents clients savings account.
    """

    def __init__(self, account_number:int, client_number:int,
                balance:float, date_created:date, minimum_balance:float):
        """
        Initializes class attrbutes to argument values.

        Args:

        
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.SERVICE_CHARGE_PREMIUM = 2.00

        try:
            if float(minimum_balance):
                self.__minimum_balance = minimum_balance
        except Exception:
            minimum_balance = 50
            self.__minimum_balance = minimum_balance

    def __str__(self):
        """
        informal string rep
        """
        account_info = super().__str__()
        minimun_balance_info = (f"Account Number: {self._BankAccount__account_number}" +
                                f" Balance: {self._BankAccount__balance}" +
                                f" Minimum Balance: {self.__minimum_balance} Account Type: Savings")
        
        return account_info + minimun_balance_info

    def get_service_charges(self):
        """
        service charges for savings account.
        """
        if self.__balance >= self.__minimum_balance:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        
        if self.__balance < self.__minimum_balance:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE 
                             * self.SERVICE_CHARGE_PREMIUM)
        
        return service_charge