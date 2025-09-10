"""
Description:
"""

__author__ = "Sven Beitegner"
__version__ = "1.0.0"
__credits__ = ""

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Client class:
    """
    
    def __init__(self, client_number: int, first_name: str,
                  last_name: str, email_address: str):
        """

        agrs:
            client_number: An integer value representing the client number.
            first_name: A string value the client's last name.
            last_name: A  string value the client's last name.
            email_address: A string value the client's email address.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name must not be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name must not be blank")
        
        email = "Joanne.Sinclair@Pixel-River.COM"

        try:
            validate_email = validate_email(email, check_deiverability = False)
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

        Returns
            str: The client's last name.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for email_address attribute.

        Returns
            str: The client's email address.
        """
        return self.__email_address
    
    def __str__(self, client_number: int, first_name: str,
                  last_name: str, email_address: str):
        """
        Returns the informal string representaion of the client information (# ask if object).

        Returns:
            str: the informal string representation of client information (# aks if object).
        """
        
        return (f"{last_name}, {first_name} [{client_number}] - {email_address}")
