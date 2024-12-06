class Patient:
    def __init__(self, patient_id, name, age, gender, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.doctor_assigned = None

    def display_info(self):
        print(f"\nPatient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Doctor Assigned: {self.doctor_assigned.name if self.doctor_assigned else 'Not Assigned'}")


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def assign_doctor(self, patient_id, doctor_id):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)

        if patient and doctor:
            patient.doctor_assigned = doctor
            print(f"Patient {patient.name} assigned to Doctor {doctor.name}")
        else:
            print("Patient or Doctor not found.")

    def create_patient_record(self):
        patient_id = len(self.patients) + 1
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender: ")
        contact_number = input("Enter patient contact number: ")

        new_patient = Patient(patient_id, name, age, gender, contact_number)
        self.add_patient(new_patient)
        print(f"Patient {name} added successfully with ID {patient_id}")

    def edit_patient_record(self, patient_id):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)

        if patient:
            print("Enter new information (leave blank to keep existing):")
            name = input(f"Current Name: {patient.name}, New Name: ") or patient.name
            age = int(input(f"Current Age: {patient.age}, New Age: ") or patient.age)
            gender = input(f"Current Gender: {patient.gender}, New Gender: ") or patient.gender
            contact_number = input(f"Current Contact Number: {patient.contact_number}, New Contact Number: ") or patient.contact_number

            # Update patient information
            patient.name = name
            patient.age = age
            patient.gender = gender
            patient.contact_number = contact_number

            print(f"Patient {patient.name}'s record updated successfully.")
        else:
            print("Patient not found.")

    def generate_bill(self, patient_id):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)

        if patient:
            # Basic billing calculation (you may need a more sophisticated billing system)
            total_amount = 1000  # Example amount
            print(f"Bill for Patient {patient.name} (ID: {patient_id}): ${total_amount}")
        else:
            print("Patient not found.")

    def display_patients(self):
        print("\nPatients:")
        for patient in self.patients:
            patient.display_info()

    def display_doctors(self):
        print("\nDoctors:")
        for doctor in self.doctors:
            print(f"ID: {doctor.doctor_id}, Name: {doctor.name}, Specialization: {doctor.specialization}")


# Example usage:
hospital = Hospital("City Hospital")

patient1 = Patient(1, "Mukesh", 30, "Male", "123-456-7890")
patient2 = Patient(2, "Shivani", 25, "Female", "987-654-3210")

doctor1 = Doctor(101, "Dr. Hamza", "Cardiologist")
doctor2 = Doctor(102, "Dr. Siddiqi", "Orthopedic")

hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

hospital.assign_doctor(1, 101)
hospital.assign_doctor(2, 102)

while True:
    print("\nHospital Management System Menu:")
    print("1. Display Patients")
    print("2. Display Doctors")
    print("3. Create Patient Record")
    print("4. Edit Patient Record")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hospital.display_patients()
    elif choice == "2":
        hospital.display_doctors()
    elif choice == "3":
        hospital.create_patient_record()
    elif choice == "4":
        patient_id = int(input("Enter patient ID to edit record: "))
        hospital.edit_patient_record(patient_id)
    elif choice == "5":
        patient_id = int(input("Enter patient ID to generate bill: "))
        hospital.generate_bill(patient_id)
    elif choice == "6":
        print("Exiting Hospital Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
