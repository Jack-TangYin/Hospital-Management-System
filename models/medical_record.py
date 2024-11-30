"""
This module defines the MedicalRecord class, which stores a patient's diagnosis 
and treatment history.
"""

class MedicalRecord:
    """
    Represents a medical record with details about the diagnosis and treatment.

    Attributes:
        record_id (str): A unique identifier for the medical record.
        patient (Patient): The patient associated with the record.
        diagnosis (str): The diagnosis for the patient.
        treatment (str): The prescribed treatment for the patient.
    """

    def __init__(self, record_id, patient, diagnosis, treatment):
        """
        Initializes a MedicalRecord object with relevant details.

        Args:
            record_id (str): A unique identifier for the medical record.
            patient (Patient): The patient associated with the record.
            diagnosis (str): The diagnosis for the patient.
            treatment (str): The prescribed treatment for the patient.
        """
        self.__record_id = record_id
        self.patient = patient
        self.diagnosis = diagnosis
        self.treatment = treatment

    def display_details(self):
        """
        Returns a string representation of the medical record's details.

        Returns:
            str: A string with the medical record's details.
        """
        return (f"Record ID: {self.__record_id}, Patient: {self.patient.name}, "
                f"Diagnosis: {self.diagnosis}, Treatment: {self.treatment}")
