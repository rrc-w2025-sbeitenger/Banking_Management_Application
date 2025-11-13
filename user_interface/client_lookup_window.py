__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    
    def __init__(self):
        super().__init__()

        #tuple of dictionaries.
        data_tuple = load_data()
        #clien_listing dictionary.
        self.__client_listing = data_tuple[0]
        #accounts dictionary.
        self.__accounts = data_tuple [1]

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
    

    @Slot()
    def __on_lookup_client(self):
        """
        docstrings
        """
        #parse client_number to integer, if it fails display QMessageBox.
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.information(self, "Input Error",
                                    "The client number must must be a numeric value.",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.reset_display()
            return
        
        #if client_number is in client_listing then set the client_info_label to client's name.
        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found",
                                    f"Client number: {client_number} not found.",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.reset_display()
            return
        else:
            client_object = self.__client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {client_object.first_name} {client_object.last_name}")
        
        #iterate though the accounts dict for matching client_number.
        #where i represents each BankAccount.
        for i in self.__accounts.values():
            if client_number == i.client_number:
                #add empty row under any other rows.
                current_row = self.account_table.rowCount()
                self.account_table.insertRow(current_row)
                
                #widgets for each account_table column.
                account_number_widget = QTableWidgetItem(str(i.account_number))
                balance_widget = QTableWidgetItem(f"${(i.balance):,.2f}")
                date_created_widget = QTableWidgetItem(str(i._date_created))
                account_type_widget = QTableWidgetItem(i.__class__.__name__)

                #center each widget
                account_number_widget.setTextAlignment(Qt.AlignCenter)
                balance_widget.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)
                date_created_widget.setTextAlignment(Qt.AlignCenter)
                account_type_widget.setTextAlignment(Qt.AlignCenter)

                #add each widget item to the table.
                self.account_table.setItem(current_row, 0, account_number_widget)
                self.account_table.setItem(current_row, 1, balance_widget)
                self.account_table.setItem(current_row, 2, date_created_widget)
                self.account_table.setItem(current_row, 3, account_type_widget)
            else:
                continue
        
        self.account_table.resizeColumnsToContents()


    @Slot()
    def __on_text_changed(self):
        """
        docstrings
        """
        self.account_table.setRowCount(0)


    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """
        docstrings
        """
        column = 0
        #obtain account number.
        account_number = int(self.account_table.item(row, column).text())
        
        if account_number in self.__accounts:
            bank_account = self.__accounts[account_number]
            AccountDetailsWindow(bank_account).exec_()
        elif account_number is None:
            QMessageBox.information(self, "account_number",
                                    f"Please select a valid record.",
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, "No Bank Account",
                                    f"Bank Account selected does not exist.",
                                    QMessageBox.Ok, QMessageBox.Ok)


