"""This module defines the TestSavingsAccount class.

Usage:
    to run all tests type this command:

    $ python -m unittest tests/test_savings_account.py
"""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    """
    Unittesting InvestmentAccount Class
    """

    def test_init_valid_inputs_are_set(self):
        savings_account = SavingsAccount(1172010, 98765, 50000.85, date(2025, 9, 30), 1000)

        #superclass private attributes.
            #already tested in previous assignment.

        #superclass protected attributes.
        self.assertEqual(date(2025,9,30), savings_account._date_created)

        #subclass private attributes.
        self.assertEqual(1000, savings_account._SavingsAccount__minimum_balance)

    def test_init_invalid_inputs_miniumn_balance(self):
        savings_account = SavingsAccount(1172010, 98765, 50000.85, date(2025, 9, 30), "str")
        actual = savings_account._SavingsAccount__minimum_balance
        expected = 50
        self.assertEqual(actual, expected)

    def test_get_service_charges_valid_input_balance_greater_than_minimum(self):
        savings_account = SavingsAccount(1172010, 98765, 50000.85, date(2025, 9, 30), 1000)
        actual = savings_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, expected)
    
    def test_get_service_charges_valid_inputs_balance_equal_to_minimum(self):
        savings_account = SavingsAccount(1172010, 98765, 1000, date(2025, 9, 30), 1000)
        actual = savings_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, expected)
    
    def test_get_service_charges_valid_inputs_balance_less_than_minimum(self):
        savings_account = SavingsAccount(1172010, 98765, 500, date(2025, 9, 30), 1000)
        actual = savings_account.get_service_charges()
        expected = 1.00
        self.assertEqual(round(actual, 2), expected)
    
    def test_str_valid_format_returned(self):
        savings_account = SavingsAccount(1172010, 98765, 50000.85, date(2025, 9, 30), 1000)
        actual = str(savings_account)
        expected = ("Account Number: 1172010 Balance: $50,000.85\n"+
                    "Minimum Balance: $1,000.00 Account Type: Savings")
        self.assertEqual(actual, expected)