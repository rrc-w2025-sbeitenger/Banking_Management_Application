__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        if isinstance(account, BankAccount):
            self.__account = copy.copy(account)
            
            #set labels.
            self.account_number_label.setText(str(self.__account.account_number))
            self.balance_label.setText((f"${self.__account.balance:,.2f}"))

            #connection between slots and signals.
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            AccountDetailsWindow.reject()
    

    def __on_apply_transaction(self):
        """
        docstrings
        """
        pass
    

    def __on_exit(self):
        """
        docstrings
        """
        pass