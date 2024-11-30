"""
This module defines the Appointment class, representing an appointment 
between a doctor and a patient.
"""

class Appointment:
    """
    Represents an appointment with details of the doctor, patient, date, and time.

    Attributes:
        appointment_id (str): A unique identifier for the appointment.
        doctor (Doctor): The doctor involved in the appointment.
        patient (Patient): The patient involved in the appointment.
        date (str): The date of the appointment.
        time (str): The time of the appointment.
    """

    def __init__(self, appointment_id, doctor, patient, date, time):
        """
        Initializes an Appointment object with relevant details.

        Args:
            appointment_id (str): A unique identifier for the appointment.
            doctor (Doctor): The doctor involved in the appointment.
            patient (Patient): The patient involved in the appointment.
            date (str): The date of the appointment.
            time (str): The time of the appointment.
        """
        self.__appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def display_details(self):
        """
        Returns a string representation of the appointment's details.

        Returns:
            str: A string with the appointment's details.
        """
        return (f"Appointment ID: {self.__appointment_id}, "
                f"Doctor: {self.doctor.name}, Patient: {self.patient.name}, "
                f"Date: {self.date}, Time: {self.time}")
