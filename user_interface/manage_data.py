__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sven Beitenger"

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime, date
import logging

from client.client import Client
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************






def load_data()->tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        try:
            #for each row in reader, pull out the corresponding data.
            #//! Indexing such as int(reader[0]) only works in a csv.reader.
            for row in reader:
                client_number = int(row['client_number'])
                first_name = str(row['first_name'])
                last_name = str(row['last_name'])
                email_address = str(row['email_address'])
                #create client object that will be added to client_listing dictionary
                #with key and value.
                client = Client(client_number, first_name, last_name, email_address)
                client_listing[client_number] = client
        except Exception as e:
            logging.error(f"Unable to create client: {e}") 


    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)  

        for row in reader:
            try:
                account_number = int(row['account_number'])
            
                client_number = int(row['client_number'])
            
                balance = float(row['balance'])

                date_str = str(row['date_created'])
                date_created = datetime.strptime(date_str, "%Y-%m-%d").date()
            
                account_type = str(row['account_type'])

                overdraft_limit_str = str(row['overdraft_limit'])
                if overdraft_limit_str == 'Null':
                    overdraft_limit = 0
                else:
                    overdraft_limit = float(overdraft_limit_str)

                overdraft_rate_str = str(row['overdraft_rate'])
                if overdraft_rate_str == 'Null':
                    overdraft_rate = 0
                else:
                    overdraft_rate = float(overdraft_rate_str)

                minimum_balance_str = str(row['minimum_balance'])
                if minimum_balance_str == 'Null':
                    minimum_balance = 0
                else:
                    minimum_balance = float(minimum_balance_str)

                management_fee_str = str(row['management_fee'])
                if management_fee_str == 'Null':
                    management_fee = 0
                else:
                    management_fee = float(management_fee_str)

                #evluate the account_type for each record.
                if account_type == "ChequingAccount":
                    #//! if check (move overdraft_rate and limit to here).
                    bank_account = ChequingAccount(account_number, client_number,
                                    balance, date_created,
                                    overdraft_limit, overdraft_rate)
                elif account_type == "SavingsAccount":
                    #//! if check (move minimum_balance to here).
                    bank_account = SavingsAccount(account_number, client_number,
                                    balance, date_created, 
                                    minimum_balance)
                elif account_type == "InvestmentAccount":
                    #//! if check (move managment_fee to here).
                    bank_account = InvestmentAccount(account_number, client_number,
                                        balance, date_created,
                                        management_fee)
                else:
                    raise ValueError("Not a valid account type.")
                
                #if BankAccount exits in client_listing add it to the accounts dictionary
                if client_number in client_listing:
                    accounts[account_number] = bank_account
                else:
                    logging.error(f"Bank Account: {account_number}" +
                                    f" contains invalid Client Number: {client_number}")
            except Exception as e:
                logging.error(f"Unable to create bank account: {e}")

    # RETURN STATEMENT -> returning client_listing and accounts dicts in a tuple.
    return (client_listing, accounts)
    

def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")