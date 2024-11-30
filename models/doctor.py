"""
This module defines the Doctor class, which inherits from the Person class 
and adds doctor-specific attributes like specialization and doctor ID.
"""

from models.person import Person

class Doctor(Person):
    """
    Represents a doctor with attributes specific to their role.

    Attributes:
        name (str): The name of the doctor.
        age (int): The age of the doctor.
        gender (str): The gender of the doctor.
        specialization (str): The doctor's area of expertise.
        doctor_id (str): A unique identifier for the doctor.
    """

    def __init__(self, name, age, gender, specialization, doctor_id):
        """
        Initializes a Doctor object with additional details specific to doctors.

        Args:
            name (str): The name of the doctor.
            age (int): The age of the doctor.
            gender (str): The gender of the doctor.
            specialization (str): The doctor's area of expertise.
            doctor_id (str): A unique identifier for the doctor.
        """
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.doctor_id = doctor_id

    def prescribe_medicine(self, patient, medicine):
        """
        Simulates prescribing medicine to a patient.

        Args:
            patient (Patient): The patient receiving the prescription.
            medicine (str): The name of the prescribed medicine.
        """
        print(f"Dr. {self.name} prescribed {medicine} to {patient.name}.")

    def display_details(self):
        """
        Extends the display_details method to include doctor-specific details.

        Returns:
            str: A string with the doctor's name, age, gender, specialization, and ID.
        """
        details = super().display_details()
        return f"{details}, Specialization: {self.specialization}, Doctor ID: {self.doctor_id}"
