#

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    docstrings
    """
    def __init__(self, overdraft_limit:float, overdraft_rate: float):
        """
        docstrings
        """

        self.overdraft_limit = overdraft_limit
        self.overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for each client.

        Returns:
            service_charge(str): Calculated service charge for clients bank account.

        """
        if self.balance >= self.__overdraft_limit:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        
        if self.balance < self.__overdraft_limit:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE + 
                             (self.__overdraft_limit - self.balance)
                             * self.__overdraft_rate)
            
        return service_charge

