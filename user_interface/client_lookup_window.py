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
    """
    Window which allows the user to search up clients.
    """
    def __init__(self):
        """
        Initialize class attrbutes to argument values.
        Invoke the super __init__, and connect button signals to slots methods.
        """
        super().__init__()

        #tuple of dictionaries.
        data_tuple = load_data()
        #clien_listing dictionary.
        self.__client_listing = data_tuple[0]
        #accounts dictionary.
        self.__accounts = data_tuple [1]

        #connect signals to slots.
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
    

    @Slot()
    def __on_lookup_client(self):
        """
        When the user looks up the client number fill the table with client data.
        """
        #parse client_number to integer, if it fails display error window.
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
        #where i represents each BankAccount (could change 'i' to 'account').
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

                #When client record is displayed, invoke toggle_filter to indicate
                #that it is not being filtered.
                self.__toggle_filter(False)
            else:
                continue
        
        self.account_table.resizeColumnsToContents()


    @Slot()
    def __on_text_changed(self):
        """
        Removes all rows from table. Sets the table row count to zero.
        """
        self.account_table.setRowCount(0)


    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """
        Receive the values of the cell clicked on the table.

        Args:
            row (int): Row of the clicked table cell.
            column (int): Column of the clicked table cell.
        """
        column = 0
        #receive account number.
        account_number = int(self.account_table.item(row, column).text())
        
        
        if account_number in self.__accounts:
            #obtain the bank account.
            bank_account = self.__accounts[account_number]
            #intance of AccountDetailsWindows.
            accountWindow = AccountDetailsWindow(bank_account)
            #connect the signal object of AccountDetailWindow to update_data.
            accountWindow.balance_updated.connect(self.__update_data)
            #open window as dialog box.
            accountWindow.exec_()
        elif account_number is None:
            QMessageBox.information(self, "account_number",
                                    "Please select a valid record.",
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.",
                                    QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def __update_data(self, account: BankAccount):
        """
        Updates account based on the transaction amount made in AccountDetailsWindow.
        AccountDetailsWindow sends a signal to this slot method.

        Args:
            account (BankAccount): The bank account being affected. 
        """
        #iterate through the table rows.
        for row in range(self.account_table.rowCount()):
            #if account_number is equal to the account number on the table cell.
            if account.account_number == int(self.account_table.item(row, 0).text()):
                #change text of the table balance cell, to the new balance. 
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")
                
                #update the account in the accounts dictionary.
                self.__accounts[account.account_number] = account

                #update CSV file.
                update_data(account)

    def __on_filter_clicked(self):
        """
        filters data on the table using user entered text form the filter_combo_box and filter_edit.
        ! update later !
        """
        #filter out rows form the filter combobox selection.
        if self.filter_button.text() == "Apply Filter":
            #filter combobox index values are the same as the table columns index. When a selection is
            #choosen in the filter combobox it's filtering by that column in the table.
            filter_combo_box_index = self.filter_combo_box.currentIndex()
            filter_edit_text = self.filter_edit.text()

            #iterate through account table.
            for row in range(self.account_table.rowCount()):
                #check each table cells by row iteration, and using the filter combobox
                #index as the column.
                table_cell = self.account_table.item(row, filter_combo_box_index)
                #grab the text of the current table cell to compare to.
                table_cell_text = table_cell.text()
                
                #if the text in the filter_edit_text widget is NOT within the table cell,
                #then hide it, else display it.
                if filter_edit_text not in table_cell_text:
                    self.account_table.setRowHidden(row, True)
                else:
                    self.account_table.setRowHidden(row, False)
                
                #data is being filtered!
                self.__toggle_filter(True)
        else:
            #data is not being filtered!
            self.__toggle_filter(False)

    def __toggle_filter(self, filter_on: bool):
        """
        docstings.
        """
        #Enable the filter button.
        self.filter_button.setEnabled(True)

        #table data is being filtered!
        if filter_on:
            self.filter_button.setText("Reset.")
            self.filter_combo_box.setDisabled(True)
            self.filter_edit.setDisabled(True)
            self.filter_label.setText("Data is Currently Filtered.")
        #table data is not being filtered!
        elif filter_on == False:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setDisabled(False)
            self.filter_edit.setDisabled(False)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            #iterate through the rows of account_table.
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered.") 