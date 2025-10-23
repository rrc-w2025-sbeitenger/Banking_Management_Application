#

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    docstrings
    """
    #//! EDIT DOC STRINGS
    
    #constant
    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(self, minumum_balance: float):
        """
        """
        self.__minimum_balance = minumum_balance

    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        service charges for savings account.

        Returns:
            service_charge (float): Savings bank account fee for
            using our service.

        """
        if account.balance >= self.__minimum_balance:
            service_charge = account.BASE_SERVICE_CHARGE
        
        if account.balance < self.__minimum_balance:
            service_charge = (account.BASE_SERVICE_CHARGE 
                             * self.SERVICE_CHARGE_PREMIUM)
        
        return service_charge
