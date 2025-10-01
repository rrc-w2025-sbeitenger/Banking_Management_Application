"""
Description: A class to chequing
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"

#imports
from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Represents clients chequings account.
    """

    def __init__(self, account_number: int, client_number: int,
                  balance: float, date_created: date,
                  overdraft_limit: float, overdraft_rate: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            account_number (int): Integer value representing the account number.
            client_number (int): Integer value representing the client number.
            balance (float): Float value representing the client's bank account balance.
            date_created(date): The date of account creation.
            overdraft_limit (float): Overdraft Limit of how much money can be taken out.
            overdraft_rate (float): The pertectage rate of the overdraft.
        
        """

        #invoke the dunder init method of the superclass with all 
        #superclass attributes.
        super().__init__(account_number, client_number, balance, date_created)

        #The maximum amount a balance can be overdrawn (below 0.00)
        #before overdraft fees are applied.
        try:
            if float(overdraft_limit):
                self.__overdraft_limit = overdraft_limit
        except:
            #if overdraft_limit cannot be parsed to a float set a
            #default of -100.
            overdraft_limit = -100
            self.__overdraft_limit = overdraft_limit

        try:
            if float(overdraft_rate):
                self.__overdraft_rate = overdraft_rate
        except:
            overdraft_rate = 0.05
            self.__overdraft_rate = overdraft_rate
    

    def __str__(self) -> str:
        """
        Formal string repsention of client accounts overdraft.

        Returns:
            (str): Account number with balance, and all overdraft information.

        """
        account_and_balance = super().__str__()
        overdraft_limit_and_rate = (f"Overdraft Limit: ${self.__overdraft_limit:.2f}" +
                                    f" Overdraft Rate: {self.__overdraft_rate * 100:.2f}" +
                                    "% Account Type: Chequing")

        return (account_and_balance + overdraft_limit_and_rate)

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for each client.

        Returns:
            service_charge(str): Calculated service charge for clients bank account.

        """
        if self._BankAccount__balance >= self.__overdraft_limit:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        
        if self._BankAccount__balance < self.__overdraft_limit:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE + 
                             (self.__overdraft_limit - self._BankAccount__balance)
                             * self.__overdraft_rate)
            
        return service_charge
