"""
This module defines the Patient class, which inherits from the Person class 
and adds patient-specific details like patient ID and ailment.
"""

from models.person import Person

class Patient(Person):
    """
    Represents a patient with unique attributes like patient ID and ailment.

    Attributes:
        name (str): The name of the patient.
        age (int): The age of the patient.
        gender (str): The gender of the patient.
        patient_id (str): A unique identifier for the patient.
        ailment (str): The ailment the patient is suffering from.
    """

    def __init__(self, name, age, gender, patient_id, ailment):
        """
        Initializes a Patient object with additional details specific to patients.

        Args:
            name (str): The name of the patient.
            age (int): The age of the patient.
            gender (str): The gender of the patient.
            patient_id (str): A unique identifier for the patient.
            ailment (str): The ailment the patient is suffering from.
        """
        super().__init__(name, age, gender)
        self.__patient_id = patient_id
        self.ailment = ailment

    def get_patient_id(self):
        """
        Provides controlled access to the private patient ID.
        
        Returns:
            str: The patient's ID.
        """
        return self.__patient_id

    def display_details(self):
        """
        Extends the display_details method to include patient-specific details.

        Returns:
            str: A string with the patient's name, age, gender, ID, and ailment.
        """
        details = super().display_details()
        return f"{details}, Patient ID: {self.__patient_id}, Ailment: {self.ailment}"

        