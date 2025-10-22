#

#imports
from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    docstring
    """

    #constant.
    base_service_charge = BankAccount.BASE_SERVICE_CHARGE

    def calculate_service_charges(account:BankAccount) -> float:
        """
        docstring
        """
        pass

