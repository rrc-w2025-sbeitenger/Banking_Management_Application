#

#imports
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    docstrings
    """
    #constant
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        docstrings
        """
        #define each arugment value to the corresponding attribute.
        self.__date_created = date_created
        self.__management_fee = management_fee
    
    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        service charges for the investments bank accounts.

        Returns:
            service_charge (float): Cost of service charge.

        """
        #if creation date is greater than 10 years.
        if self.__date_created < self.TEN_YEARS_AGO:
            service_charge = account.BASE_SERVICE_CHARGE
        else:
            service_charge = account.BASE_SERVICE_CHARGE + self.__management_fee
        
        return service_charge
