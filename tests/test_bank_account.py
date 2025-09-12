"""
Description: Unit tests for the BankAccount class.
Author: Sven Beitenger
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """
    """

    def setUp(self):
        self.bank_account = BankAccount(1172007, 12345, 70000.85)

    def test_init_valid_bank_account_attributes_are_set(self):
        bank_account = BankAccount(1172007, 12345, 70000.85)
        
        self.assertEqual(1172007, bank_account._BankAccount__account_number)
        self.assertEqual(12345,bank_account._BankAccount__client_number)
        self.assertEqual(70000.85, bank_account._BankAccount__balance)

    def test_init_non_numeric_balance_attribute_set_balance_to_zero(self):
        #arrange
        test_bank_account = BankAccount(1172007, 12345, "str")

        #act
        actual = test_bank_account.balance
        excepted = 0

        #assert
        self.assertEqual(actual, excepted)

    def test_init_non_numeric_account_number_valueerror_raised(self):
        with self.assertRaises(ValueError):
            BankAccount("str", 12345, 70000.85)

    def test_init_non_numeric_client_number_valueerror_raised(self):
        with self.assertRaises(ValueError):
            BankAccount(1172007, "str", 70000.85)
    
    def test_account_number_accessor_is_valid_returned(self):
        #act
        actual = self.bank_account.account_number
        expected = 1172007

        #assert
        self.assertEqual(actual, expected)

    def test_client_number_accessor_is_valid_returned(self):
        #act
        actual = self.bank_account.client_number
        expected = 12345

        #assert
        self.assertEqual(actual, expected)
    
    def test_balance_accessor_is_valid_returned(self):
        #act
        actual = self.bank_account.balance
        expected = 70000.85

        #assert
        self.assertEqual(actual, expected)

    def test_update_balance_is_valid_new_amount_in_balance_returned(self):
        #arrange
        self.bank_account.update_balance(500)

        #act
        actual = self.bank_account.balance
        expected = 70500.85

        #assert
        self.assertEqual(actual, expected)

    def test_update_balance_is_valid_with_negative_number_updated_balance_returned(self):
        #arrange
        self.bank_account.update_balance(-500)

        #act
        actual = self.bank_account.balance
        expected = 69500.85

        #assert
        self.assertEqual(actual, expected)

    def test_update_balance_invalid_non_numeric_balance_unchanged_returned(self):
        #arrange
        self.bank_account.update_balance("str")

        #act
        actual = self.bank_account.balance
        expected = 70000.85

        #assert
        self.assertEqual(actual, expected)
    
    def test_deposit_with_valid_BankAccount_object_balance_updated_updated_balance_returned(self):
        #testing BankAccount object's balance
        #arrange
        bank_account = BankAccount(1172007, 12345, 70000.85)
        bank_account.deposit(500)

        #act
        actual = bank_account._BankAccount__balance
        expected = 70500.85

        #assert
        self.assertEqual(actual, expected)
    
    def test_deposit_invalid_negative_number_valueerror_rasied(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-500)
    
    def test_withdraw_with_valid_BankAccount_object_balance_updated_updated_balance_returned(self):
        #testing BankAccount object's balance
        #arrange
        bank_account = BankAccount(1172007, 12345, 70000.85)
        bank_account.withdraw(500)

        #act
        actual = bank_account._BankAccount__balance
        expected = 69500.85

        #assert
        self.assertEqual(actual, expected)

    def test_withdraw_invalid_negative_amount_valueerror_returned(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-500)

    def test_withdraw_invalid_amount_exceeded_passed_balance_valueerror_returned(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(80000)

    def test_dunder_str_method_valid_informal_format_returned(self):
        #act
        actual = str(self.bank_account)
        expected = f"Account Number: 1172007 Balance: $70,000.85\n"
        
        #assert
        self.assertEqual(actual, expected)
