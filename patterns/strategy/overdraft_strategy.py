"""Description: This module defines the OverdraftStrategy class."""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Class to represent the overdraft for bank account.
    """

    def __init__(self, overdraft_limit:float, overdraft_rate: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            overdraft_limit (float): Overdraft Limit of the amount that can be taken out.
            overdraft_rate (float): The pertectage rate of the overdraft.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for each client.

        Args:
            account (BankAcount): The client bank account of BankAccount class.
            
        Returns:
            service_charge (float): Service charge for clients bank account.

        """
        if account.balance >= self.__overdraft_limit:
            service_charge = account.BASE_SERVICE_CHARGE
        
        if account.balance < self.__overdraft_limit:
            service_charge = (account.BASE_SERVICE_CHARGE + 
                             (self.__overdraft_limit - account.balance)
                             * self.__overdraft_rate)
            
        return service_charge

