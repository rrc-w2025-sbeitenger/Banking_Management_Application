"""Description: This module defines the AccountDetailsWindow class."""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    #signal object representing the updated BankAccount.
    balance_updated = Signal(BankAccount)

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

            #connection between signals and slots.
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            AccountDetailsWindow.reject()
    
    @Slot()
    def __on_apply_transaction(self):
        """
        Will perform a transaction using the transaction amount entered.
        This is a slot method, for the signals of the withdraw and depoit buttons.
        """
        #parse transaction amount to float.
        try:
            transaction_amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(self, "Invalid Data",
                                    "Amount must be numeric.",
                                    QMessageBox.Ok, QMessageBox.Ok)
        
        try:
            #check if button widget was clicked.
            if self.sender() == self.deposit_button:
                transaction_string = "Deposit"
                self.__account.deposit(transaction_amount)
                self.balance_updated.emit(self.__account)
            
            #check if button widget was clicked.
            if self.sender() == self.withdraw_button:
                transaction_string = "Withdraw"
                self.__account.withdraw(transaction_amount)
                self.balance_updated.emit(self.__account)
            
            #set text to balance amount.
            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            #set transaction amount it empty string.
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(self, transaction_string,
                                    f"{e}",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.transaction_amount_edit.setFocus()
    
    @Slot()
    def __on_exit(self):
        """
        close window when users clicks on exit button.
        """
        self.close()