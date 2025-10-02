"""
Description: A class to investment account
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

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, management_fee: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            account_number (int): Integer value representing the account number.
            client_number (int): Integer value representing the client number.
            balance (float): Float value representing the client's bank account
            balance.
            date_created (date): The date of creation.
            management_fee (float): Management fee that the client owns for using
            our service.

        """
        #invoke superclass
        super().__init__(account_number, client_number, balance, date_created)

        #constants (SHOULD CHECK IF REQUIRED TO BE OUTISDE OR INSIDE INIT).
        #also check if needs to have self or not.
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        try:
            if  float(management_fee):
                self.__management_fee = management_fee
        except Exception:
            management_fee = 2.55
            self.__management_fee = management_fee
        
    def __str__(self) -> str:
        """
        informal string reresentation of investment bank account.

        Returns:
            (str): account information, alongside account management
            information.

        """
        #invoke superclass str
        account_and_balance = super().__str__()
        
        #if creation date is greater than 10 years
        if self._date_created >= self.TEN_YEARS_AGO:
            fee = f"${self.__management_fee:.2f}"
        #if creation date is less than 10 years
        elif self._date_created < self.TEN_YEARS_AGO:
            fee = "wavied"
        
        account_management_info = (f"Date Created: {self._date_created}" +
                                  f" Management Fee: {fee} Account Type: Investment")
        
        return account_and_balance + account_management_info
    
    def get_service_charges(self) -> float:
        """
        service charges for the investments bank accounts.

        Returns:
            service_charge (float): Cost of service charge.

        """
        #if creation date is greater than 10 years
        if self._date_created < self.TEN_YEARS_AGO:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee
        
        return service_charge