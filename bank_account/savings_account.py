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
            account_number (int): Integer value representing the account number.
            client_number (int): Integer value representing the client number.
            balance (float): Float value representing the client's bank account balance.
            date_created (date): The date of creation.
            minimum_balance (float): Minimum balance in savings account.
        
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
        informal string reresentation of savings bank account.

        Returns:
            (str): account information, alongside account minimum
            balance information.

        """
        account_info = super().__str__()
        
        minimun_balance_info = (f"Minimum Balance:" + 
                                f" ${self.__minimum_balance:,.2f} Account Type: Savings")
        
        return account_info + minimun_balance_info

    def get_service_charges(self):
        """
        service charges for savings account.

        Returns:
            service_charge (str): Savings bank account fee for
            using our service.

        """
        if self.balance >= self.__minimum_balance:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        
        if self.balance < self.__minimum_balance:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE 
                             * self.SERVICE_CHARGE_PREMIUM)
        
        return service_charge