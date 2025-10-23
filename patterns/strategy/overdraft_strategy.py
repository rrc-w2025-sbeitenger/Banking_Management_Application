#

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    docstrings
    """
    #//! EDIT DOC STRINGS
    
    def __init__(self, overdraft_limit:float, overdraft_rate: float):
        """
        docstrings
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for each client.

        Returns:
            service_charge(float): Calculated service charge for clients bank account.

        """
        if account.balance >= self.__overdraft_limit:
            service_charge = account.BASE_SERVICE_CHARGE
        
        if account.balance < self.__overdraft_limit:
            service_charge = (account.BASE_SERVICE_CHARGE + 
                             (self.__overdraft_limit - account.balance)
                             * self.__overdraft_rate)
            
        return service_charge

