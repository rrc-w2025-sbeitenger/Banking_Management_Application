"""
Description: A class to manage Client objects
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"

#imports
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

class Client(Observer):
    """
    Client class: Represents the clients information.
    """
    
    def __init__(self, client_number: int, first_name: str,
                  last_name: str, email_address: str):
        """
        Initializes class attrbutes to argument values.

        Args:
            client_number: An integer value representing the client number.
            first_name: A string value the client's last name.
            last_name: A  string value the client's last name.
            email_address: A string value the client's email address.

        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.\n")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name must not be blank.\n")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name must not be blank\n")
        
        email = "Joanne.Sinclair@pixel-river.com"

        try:
            validated_email = validate_email(email,
                                            check_deliverability = False)
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    #accessors
    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute.

        Returns:
            int: The client number.
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for first_name attribute.
        
        Returns:
            str: The client's first name.
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for last_name attribute.

        Returns:
            str: The client's last name.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for email_address attribute.

        Returns:
            str: The client's email address.
        """
        return self.__email_address
    
    def __str__(self):
        """
        Returns the informal string representaion of the client
        information (object).

        Returns:
            str: The informal string representation of client information.
        """
        
        return (f"{self.__last_name}, {self.__first_name}"
               + f" [{self.__client_number}] - {self.__email_address}\n")
    
    def update(self, message: str):
        """
        Send email notification to alert the client of bank account balance bellow the minmum limit, or
        transactions amounts over max thershold.

        Args:
            message(str): Alert notification for client.
        
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        fullMessage = f"Notification for {self.__client_number}: {self.__first_name} {self.__last_name}: {message}"
        simulate_send_email(self.__email_address, subject, fullMessage)
