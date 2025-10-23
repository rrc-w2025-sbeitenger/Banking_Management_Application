"""This module defines the superclass Observer class."""

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

#imports
from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer superclass will be used to define the interface for all
    concrete observers that need to be notified of changes in the subject.
    """

@abstractmethod
def update(message:str):
    """
    Abstract update method. Implemented in subclasses.
    """
    pass