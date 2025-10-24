"""This module defines the ServiceChargeStrategy class."""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

#imports
from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Class to represent the base abstract superclass for strategy's to inherit from.
    """
    #constant.
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(account:BankAccount) -> float:
        """
        Abstract calculte_service_charges. Implemented in subclasses.
        """
        pass

