"""This module defines the TestChequingAccount class.

Usage:
    to run all tests type this command:

    $ python -m unittest tests/test_chequing_account.py
"""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    """
    Unit test class for chequings account.
    """

    def setUp(self):
        self.chequing_account = ChequingAccount(1172010, 98765, 80000.85, date(2025, 9, 30), -200, 0.08)
    
    def test_init_valid_inputs_attributes_set(self):
        #superclass private attributes.
            #already tested in previous assignment.

        #superclass protected attributes.
        self.assertEqual(date(2025,9,30), self.chequing_account._date_created)

        #subclass private attributes.
        self.assertEqual((-200), self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.08, self.chequing_account._ChequingAccount__overdraft_rate)
    
    def test_init_invalid_overdraft_limit_value(self):
        test_account = ChequingAccount(1172010, 98765, 80000.85, date(2025, 9, 30), "str", 0.08)
        actual = test_account._ChequingAccount__overdraft_limit
        excepted = -100
        self.assertEqual(actual, excepted)
    
    def test_init_invalid_overdraft_rate_value(self):
        test_account = ChequingAccount(1172010, 98765, 80000.85, date(2025, 9, 30), -200, "str")
        actual = test_account._ChequingAccount__overdraft_rate
        expected = 0.05
        self.assertEqual(actual, expected)

    #COME BACK TO THIS TEST
    def test_init_invalid_date_created_value(self):
        test_account = ChequingAccount(1172010, 98765, 80000.85, 2025, -200, 0.08)
        actual = test_account._date_created
        excepted = date.today()
        self.assertEqual(actual, excepted)

    def test_get_services_charges_balance_greater_than_overdraft_limit(self):
        #using setup
        actual = self.chequing_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, round(expected, 2))

    def test_get_services_charges_balance_less_than_overdraft_limit(self):
        test_account = ChequingAccount(1172010, 98765, -300, 2025, -200, 0.08)
        actual = test_account.get_service_charges()
        expected = 8.5
        self.assertEqual(actual, round(expected, 2))

    def test_get_services_charges_balance_equal_to_overdraft_limit(self):
        test_account = ChequingAccount(1172010, 98765, -200, 2025, -200, 0.08)
        actual = test_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, round(expected, 2))

    def test_str_valid_format_returned(self):
        actual = str(self.chequing_account)
        expected = (f"Account Number: 1172010 Balance: $80,000.85\n"+
                    f"Overdraft Limit: $-200.00 Overdraft Rate: 8.00% Account Type: Chequing")
        self.assertEqual(actual, expected)