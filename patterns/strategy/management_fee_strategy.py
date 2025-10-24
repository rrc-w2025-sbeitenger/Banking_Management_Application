"""This module defines the ManagmentFeeStrategy class."""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Class to represent the ManagementFeeStrategy for bank account.
    """
    #constant
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes class attrbutes to argument values.

        Args:
            date_created(date): Date the bank account was created.
            management_fee(float): management fee for the bank account.

        """
        #define each arugment value to the corresponding attribute.
        self.__date_created = date_created
        self.__management_fee = management_fee
    
    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        service charges for the investments bank accounts.

        Args:
            account(BankAcount): the client bank account of BankAccount class.

        Returns:
            service_charge (float): Service charge for clients bank account.

        """
        #if creation date is greater than 10 years.
        if self.__date_created < self.TEN_YEARS_AGO:
            service_charge = account.BASE_SERVICE_CHARGE
        else:
            service_charge = account.BASE_SERVICE_CHARGE + self.__management_fee
        
        return service_charge
