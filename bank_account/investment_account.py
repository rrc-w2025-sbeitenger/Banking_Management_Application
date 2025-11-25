"""
Description: A class to investment account
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"

#imports
from datetime import date, timedelta, datetime
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Represents clients Investment account.
    """

    #CONSTANTS
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

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

        #private managment_fee attribute.
        try:
            if  float(management_fee):
                self.__management_fee = management_fee
        except Exception:
            management_fee = 2.55
            self.__management_fee = management_fee

        #private ManagementFeeStrategy instance.
        self.__strategy = ManagementFeeStrategy(date_created, self.__management_fee)
        
    def __str__(self) -> str:
        """
        informal string reresentation of investment bank account.

        Returns:
            (str): Account information, alongside account management
            information.

        """
        #invoke superclass str
        account_and_balance = super().__str__()
        
        #if creation date is less than 10 years.
        #Sign is swapped since these are dates.
        if self._date_created >= self.TEN_YEARS_AGO:
            fee = f"${self.__management_fee:.2f}"
        #if creation date is greater than 10 years
        elif self._date_created < self.TEN_YEARS_AGO:
            fee = "wavied"
        
        account_management_info = (f"Date Created: {self._date_created}" +
                                  f" Management Fee: {fee} Account Type: Investment")
        
        return account_and_balance + account_management_info
    
    def get_service_charges(self) -> float:
        """
        Calling calculate_service_charges on strategy object, which is an instance of
        ManagementFeeStrategy, to calculate the service charges for the investments bank accounts.

        Returns:
            service_charge (float): Service charge for clients bank account.

        """
        #calling calculate_service_charges with self, since self is an instance of the class,
        #and this class inherits from BankAccount.
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge