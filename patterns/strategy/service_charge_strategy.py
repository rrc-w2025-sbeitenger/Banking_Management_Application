#

#imports
from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    docstring
    """
    #//! EDIT DOC STRINGS
    
    #constant.
    BASE_SERVICE_CHARGE: float = 0.50

    def calculate_service_charges(account:BankAccount) -> float:
        """
        docstring
        """
        pass

