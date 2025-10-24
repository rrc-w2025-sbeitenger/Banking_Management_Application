"""This module defines the MinimumBalanceStrategy class."""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Class to represent the MinimumBalanceStrategy for bank account.
    """
    #constant
    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(self, minimum_balance: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            minimum_balance(float): the minimum balance of the bank account.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        service charges for savings account.

        Args:
            account(BankAcount): the client bank account of BankAccount class.

        Returns:
            service_charge (float): Service charge for clients bank account.

        """
        if account.balance >= self.__minimum_balance:
            service_charge = account.BASE_SERVICE_CHARGE
        
        if account.balance < self.__minimum_balance:
            service_charge = (account.BASE_SERVICE_CHARGE 
                             * self.SERVICE_CHARGE_PREMIUM)
        
        return service_charge
