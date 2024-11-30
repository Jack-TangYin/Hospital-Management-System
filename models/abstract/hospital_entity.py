"""
This module defines the HospitalEntity abstract base class, 
which provides a blueprint for entities in the hospital system.
"""

from abc import ABC, abstractmethod

class HospitalEntity(ABC):
    """
    Abstract base class for all hospital entities.
    Ensures that each subclass implements the `display_details` method.
    """
    @abstractmethod
    def display_details(self):
        """
        Abstract method to display details about the entity.
        Must be implemented by subclasses.
        """
        pass
