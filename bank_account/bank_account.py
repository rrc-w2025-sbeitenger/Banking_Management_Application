"""
Description:
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"
__credits__ = ""

class BankAccount:
    """
    Description:
    """

    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Description:

        args:
            account_number: an integer value representing the account number.
            client_number: an integer value representing the client number.
            balance: float value representing the client's bank account balance.
        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        try:
            if float(balance):
                self.__balance = balance
        except ValueError:
            balance = 0
            self.__balance = balance

    @property
    def account_number(self) -> int:
        """
        """
        return self.__account_number
        
    @property
    def client_number(self) -> int:
        """
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        """
        return self.__balance
    
    def update_balance(self, amount: float):
        """
        Description:
        """
        try:
            if float(amount):
                self.__balance += amount
                return
        except ValueError:
            pass
        
    def deposit(self, amount:float):
        """
        Description:
        """
        if isinstance(amount, (float, int)):
            if amount < 0:
                raise ValueError(f"Deposit amount: -${abs(amount):,.2f} must be positive.\n")
            else:
                self.update_balance(amount)
        else:
            raise ValueError(f"Deposit amount: {amount} must be numeric.\n")

    def withdraw(self, amount:float):
        """
        Description:
        """
        if isinstance(amount, (float, int)):
            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: ${amount:,.2f}"
                                + f" must not exceed the account balance: ${self.__balance:,.2f}\n")
            elif amount < 0:
                raise ValueError(f"Withdraw amount: -${abs(amount):,.2f} must be positive.\n")
            else:
                self.update_balance(-amount)
        else:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.\n")
        
    def __str__(self):
        """
        Description:
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"