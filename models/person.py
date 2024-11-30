"""
This module defines the Person class, representing a generic person in the hospital system.
"""

from models.abstract.hospital_entity import HospitalEntity

class Person(HospitalEntity):
    """
    Represents a generic person with basic details like name, age, and gender.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person.
    """

    def __init__(self, name, age, gender):
        """
        Initializes a Person object with basic details.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        """
        Returns a string representation of the person's details.
        
        Returns:
            str: A string with the person's name, age, and gender.
        """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
