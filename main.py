"""
Main module to simulate the Hospital Management System.
Includes functionalities for managing patients, doctors, appointments, and medical records.
"""

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from models.medical_record import MedicalRecord

def add_patient():
    """
    Function to dynamically add a new patient by collecting user input.
    
    Returns:
        Patient: A new Patient object with the provided details.
    """
    print("\n=== Add New Patient ===")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender (Male/Female/Other): ")
    patient_id = input("Enter patient ID: ")
    ailment = input("Enter patient's ailment: ")

    new_patient = Patient(name, age, gender, patient_id, ailment)
    print(f"\nPatient {name} has been successfully added.")
    return new_patient

def add_doctor():
    """
    Function to dynamically add a new doctor by collecting user input.
    
    Returns:
        Doctor: A new Doctor object with the provided details.
    """
    print("\n=== Add New Doctor ===")
    name = input("Enter doctor name: ")
    age = int(input("Enter doctor age: "))
    gender = input("Enter doctor gender (Male/Female/Other): ")
    specialization = input("Enter doctor's specialization: ")
    doctor_id = input("Enter doctor ID: ")

    new_doctor = Doctor(name, age, gender, specialization, doctor_id)
    print(f"\nDoctor {name} has been successfully added.")
    return new_doctor

def add_appointment(doctors, patients, appointments):
    """
    Function to dynamically add a new appointment by collecting user input.
    
    Args:
        doctors (list): List of available Doctor objects.
        patients (list): List of available Patient objects.
    
    Returns:
        Appointment: A new Appointment object with the provided details.
    """
    print("\n=== Schedule New Appointment ===")
    if not doctors:
        print("No doctors available. Please add a doctor first.")
        return None
    if not patients:
        print("No patients available. Please add a patient first.")
        return None

    print("\nSelect a Doctor:")
    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. {doctor.display_details()}")
    doctor_choice = int(input("Enter the doctor number: ")) - 1

    print("\nSelect a Patient:")
    for i, patient in enumerate(patients, start=1):
        print(f"{i}. {patient.display_details()}")
    patient_choice = int(input("Enter the patient number: ")) - 1

    date = input("Enter the appointment date (YYYY-MM-DD): ")
    time = input("Enter the appointment time (e.g., 10:00 AM): ")

    new_appointment = Appointment(f"A{len(appointments)+1:04d}", doctors[doctor_choice], patients[patient_choice], date, time)
    print("\nAppointment successfully scheduled.")
    return new_appointment

def add_medical_record(patients, medical_records):
    """
    Function to dynamically add a new medical record by collecting user input.
    
    Args:
        patients (list): List of available Patient objects.
    
    Returns:
        MedicalRecord: A new MedicalRecord object with the provided details.
    """
    print("\n=== Add Medical Record ===")
    if not patients:
        print("No patients available. Please add a patient first.")
        return None

    print("\nSelect a Patient:")
    for i, patient in enumerate(patients, start=1):
        print(f"{i}. {patient.display_details()}")
    patient_choice = int(input("Enter the patient number: ")) - 1

    diagnosis = input("Enter the diagnosis: ")
    treatment = input("Enter the treatment: ")

    new_record = MedicalRecord(f"R{len(medical_records)+1:04d}", patients[patient_choice], diagnosis, treatment)
    print("\nMedical record successfully added.")
    return new_record

def main():
    """
    Main function to run the simulation of the hospital system.
    """
    doctors = []
    patients = []
    appointments = []
    medical_records = []

    # Add sample data
    doctors.append(Doctor("Dr. Smith", 50, "Male", "General Physician", "D2001"))
    doctors.append(Doctor("Dr. Emily", 40, "Female", "Orthopedic", "D2002"))

    patients.append(Patient("Alice", 30, "Female", "P1001", "Flu"))
    patients.append(Patient("Bob", 45, "Male", "P1002", "Back Pain"))

    while True:
        print("\n=== Hospital Management Menu ===")
        print("1. View Patients")
        print("2. Add New Patient")
        print("3. View Doctors")
        print("4. Add New Doctor")
        print("5. View Appointments")
        print("6. Schedule New Appointment")
        print("7. View Medical Records")
        print("8. Add New Medical Record")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            print("\n=== Patients ===")
            if not patients:
                print("No patients available.")
            else:
                for i, patient in enumerate(patients, start=1):
                    print(f"{i}. {patient.display_details()}")

        elif choice == "2":
            new_patient = add_patient()
            patients.append(new_patient)

        elif choice == "3":
            print("\n=== Doctors ===")
            if not doctors:
                print("No doctors available.")
            else:
                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.display_details()}")

        elif choice == "4":
            new_doctor = add_doctor()
            doctors.append(new_doctor)

        elif choice == "5":
            print("\n=== Appointments ===")
            if not appointments:
                print("No appointments available.")
            else:
                for i, appointment in enumerate(appointments, start=1):
                    print(f"{i}. {appointment.display_details()}")

        elif choice == "6":
            new_appointment = add_appointment(doctors, patients, appointments)
            if new_appointment:
                appointments.append(new_appointment)

        elif choice == "7":
            print("\n=== Medical Records ===")
            if not medical_records:
                print("No medical records available.")
            else:
                for i, record in enumerate(medical_records, start=1):
                    print(f"{i}. {record.display_details()}")

        elif choice == "8":
            new_record = add_medical_record(patients, medical_records)
            if new_record:
                medical_records.append(new_record)

        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
