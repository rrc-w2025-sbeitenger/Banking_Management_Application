"""This module defines the TestInvestmentAccount class.

Usage:
    to run all tests type this command:

    $ python -m unittest tests/test_investment_account.py
"""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    """
    Unittesting InvestmentAccount Class
    """

    def test_init_valid_input_values_are_set(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2025, 9, 30), 3)

        #superclass private attributes.
            #already tested in previous assignment.

        #superclass protected attributes.
        self.assertEqual(date(2025,9,30), investment_account._date_created)

        #subclass private attributes.
        self.assertEqual(3, investment_account._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_type(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2025, 9, 30), "str")
        actual = investment_account._InvestmentAccount__management_fee
        expected = 2.55
        self.assertEqual(actual, expected)
    
    def test_get_service_charges_creation_date_more_than_10_years(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2000, 9, 30), 3)
        actual = investment_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charges_creation_date_10_years(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2015, 10, 1), 3)
        actual = investment_account.get_service_charges()
        expected = 0.50
        self.assertEqual(actual, expected)

    def test_get_service_charges_creation_date_within_10_years(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2020, 10, 1), 3)
        actual = investment_account.get_service_charges()
        expected = 3.5
        self.assertEqual(actual, expected)
    
    def test_str_valid_format_with_wavied_fee_payment(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2000, 9, 30), 3)
        actual = str(investment_account)
        expected = ("Account Number: 1172010 Balance: $80,000.85\n" +
                    "Date Created: 2000-09-30 Management Fee: wavied Account Type: Investment")
        self.assertEqual(actual, expected)
    
    def test_str_valid_format_with_wavied_fee_payment(self):
        investment_account = InvestmentAccount(1172010, 98765, 80000.85, date(2020, 10, 1), 3)
        actual = str(investment_account)
        expected = ("Account Number: 1172010 Balance: $80,000.85\n" +
                    "Date Created: 2020-10-01 Management Fee: $3.00 Account Type: Investment")
        self.assertEqual(actual, expected)