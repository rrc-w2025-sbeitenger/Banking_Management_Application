"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""


import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """
    UnitTesting Client class.
    """

    def setUp(self):
        self.client = Client(12345, "Max", "Beit", "maxbeit@pixell-river.com")

    def test_init_valid_client_attributes_are_set(self):
        client = Client(12345, "Max", "Beit", "maxbeit@pixell-river.com")

        self.assertEqual(12345, client._Client__client_number)
        self.assertEqual("Max", client._Client__first_name)
        self.assertEqual("Beit", client._Client__last_name)
        self.assertEqual("maxbeit@pixell-river.com", client._Client__email_address)

    def test_init_non_integer_client_valueerror_raised(self):
        with self.assertRaises(ValueError):
            Client("string", "Max", "Beit", "maxbeit@pixell-river.com")
    
    def test_init_blank_first_name_valueerror_raised(self):
        with self.assertRaises(ValueError):
            Client("string", " ", "Beit", "maxbeit@pixell-river.com")

    def test_init_blank_last_name_valueerror_raised(self):
        with self.assertRaises(ValueError):
            Client("string", "Max", " ", "maxbeit@pixell-river.com")

    def test_init_invalid_email_address_valueerror_raised(self):
        with self.assertRaises(ValueError):
            Client("string", "Max", "Beit", "maxbeit@real-river.com")

    
    def test_client_number_accessor_is_valid_client_number_returned(self):
        #arrange (already done in setup)
        #act
        actual = self.client.client_number
        expected = 12345

        #assert
        self.assertEqual(actual, expected)

    def  test_first_name_accessor_is_valid_first_name_returned(self):
        #act
        actual = self.client.first_name
        expected = "Max"

        #assert
        self.assertEqual(actual, expected)
    
    def test_last_name_accessor_is_valid_last_name_returned(self):
        #act
        actual = self.client.last_name
        expected = "Beit"

        #assert
        self.assertEqual(actual, expected)

    def test_email_address_accessor_is_valid_email_address_returned(self):
        #act
        actual = self.client.email_address
        expected = "maxbeit@pixell-river.com"

        #assert
        self.assertEqual(actual, expected)
    
    def test_dunder_str_method_valid_informal_format_returned(self):
        #ASK IF THIS is correct
        #arrange
        #client = Client(12345, "Max", "Beit", "maxbeit@pixell-river.com")

        #act
        actual = str(self.client)
        expected = "Beit, Max [12345] - maxbeit@pixell-river.com\n"
        
        #assert
        self.assertEqual(actual, expected)