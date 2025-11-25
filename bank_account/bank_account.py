"""
Description: A class to manage BankAccount objects.
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"
__credits__ = ""

#imports.
from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

#abstact BankAccount class.
class BankAccount(Subject, ABC):
    """
    BankAccount class: Represents clients bank account.
    """
    #constants
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.0

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date):
        """
        Initializes a Bank Account object based on the arguments,
        if they are valid. 

        Args:
            account_number (int): Integer value representing the account number.
            client_number (int): Integer value representing the client number.
            balance (float): Float value representing the client's bank account balance.
            date_created (date): The date of creation.

        """
        #invoke the superclass init, so that _observer = [] is initialized.
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.\n")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.\n")
        
        try:
            if float(balance):
                self.__balance = balance
        except ValueError:
            balance = 0
            self.__balance = balance
        
        if not isinstance(date_created, date):
            self._date_created = date.today()
        else:
            self._date_created = date_created

    @property
    def account_number(self) -> int:
        """
        Accessor for account_number attribute.

        Returns:
            (int): The client's account number.

        """
        return self.__account_number
        
    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute.

        Returns:
            (int): The client's number.

        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for balance attribute.

        Returns:
            (int): The client's account balance.

        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Updates client's account balance. Calls notify() method to alert the
        bank account if the balance is lower than the low balance limit or
        transaction amount is over the threshold.

        Args:
            amount (float): The transaction amount being entered.

        """
        try:
            if float(amount):
                self.__balance += amount
        except ValueError:
            pass
        
        #if balance is less than low balance level.
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning {self.__balance:,.2f}:" +
                         f" on account {self.__account_number}.")
        
        #if transaction amount is greater than threshold.
        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction {amount:,.2f}: on account {self.__account_number}.")
         
    def deposit(self, amount:float) -> None:
        """
        Deposits the client's amount into their account balance.

        Args:
            amount (float): The transaction amount being entered. 

        """
        #Check if amount is intance of int or float then check if amount is 
        #negative, else we update the balacne with amount.
        #If the amount is neither float or int then raise ValueError.
        if isinstance(amount, (float, int)):
            if amount < 0:
                raise ValueError(f"Deposit amount: -${abs(amount):,.2f}" 
                                 + f" must be positive.\n")
            else:
                self.update_balance(amount)
        else:
            raise ValueError(f"Deposit amount: {amount} must be numeric.\n")

    def withdraw(self, amount:float) -> None:
        """
        Withdraw the client's amount from their account balance.

        Args:
            amount (float): The transaction amount being entered. 

        """
        #If amount is instance of float or int, then if amount exceeds
        #balance raise ValueError, elif amount is negative then
        #raise ValueError, else update balance.
        #If amount is not an instance of float or int then raise ValueError.
        if isinstance(amount, (float, int)):
            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: ${amount:,.2f}"
                                + f" must not exceed the account balance:"
                                + f" ${self.__balance:,.2f}\n")
            elif amount < 0:
                raise ValueError(f"Withdraw amount: -${abs(amount):,.2f}"
                                + f" must be positive.\n")
            else:
                self.update_balance(-amount)
        else:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.\n")
        
    def __str__(self) -> str:
        """
        Returns the informal string representaion of the client's bank
        information (object).

        Returns:
            (str): The informal string representation of client's bank information.

        """
        return (f"Account Number: {self.__account_number}" 
                + f" Balance: ${self.__balance:,.2f}\n")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Abstract method.
        Implemented in subclasses.
        """
        pass
    
    def attach(self, observer: Observer) -> None:
        """
        Append new observer to the subjects list of observers.

        Args:
            observer (Observer): Chooses the correct update interface from Observer.

        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Remove existing observer from the subjects list of observers.

        Args:
            observer (Observer): Chooses the correct update interface from Observer.
        
        """
        self._observers.remove(observer)
    
    def notify(self, message:str) -> None:
        """
        Alerts all registered observers of a state change, by
        iterating through the _observers list.

        Args:
            message (str): Alert notification message.

        """
        for i in self._observers:
            i.update(message)