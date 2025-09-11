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
        
        if isinstance(balance, float):
            self.__balance = balance
        else:
            raise ValueError("Balance must be numeric.")
        
        if float(balance) > 0:
            self.__balance = balance
        else:
            balance = 0
            self.__balance = balance
        
