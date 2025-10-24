"""This module defines the Subject class."""
#This class depends on the Observer.

#imports
from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

__author__ = "Sven Beitenger"
__version__ = "1.0.0"

class Subject(ABC):
    """
    The Subject class is responsible for maintaining a list of its observers
    and notifying them of state changes or events.
    """

    def __init__(self):
        #self._observers = Observer[]
        self._observers = []

    @abstractmethod
    def attach(observer: Observer):
        """
        Abstract attach method. Implemented in concerte classes.
        """
    
    @abstractmethod
    def detach(observer: Observer):
        """
        Abstract detach method. Implemented in concerte classes.
        """

    @abstractmethod
    def notify(message: str):
        """
        Abstract notify method. Implemented in concerte classes.
        """