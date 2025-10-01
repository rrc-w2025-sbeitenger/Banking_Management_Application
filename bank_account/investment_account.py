"""
Description: A class to chequing
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"

#imports
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Represents clients Investment account.
    """

    def __init__(self, account_number, client_number, balance, date_created, managment_fee: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            ():

        """

        #invoke superclass
        super().__init__(account_number, client_number, balance, date_created)

        #constants (SHOULD CHECK IF REQUIRED TO BE OUTISDE OR INSIDE INIT)
        TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        try:
            if  float(managment_fee):
                self.__managment_fee = managment_fee
        except Exception:
            managment_fee = 2.55
            self.__managment_fee = managment_fee
        
    def __str__(self) -> str:
        """
        informal string reresentation.
        """

        account_and_balance = super().__str__()
        
        if self._BankAccount__date_created <= self.TEN_YEARS_AGO:
            fee = self.managment_fee
        elif self._BankAccount__date_created > self.TEN_YEARS_AGO:
            fee = "wavied"
        
        account_managment_info = (f"Date Created: {self._date_created} Management Fee: ${fee:.2f} Account Type: Investment")
        
        return account_and_balance + account_managment_info
    
    def get_service_charges(self) -> float:
        """
        service charge
        """
        if self._date_created > self.TEM_YEARS_AGO:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__managment_fee
        
        return service_charge