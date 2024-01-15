import json
import os
import random
from faker import Faker


fake_data = Faker()
def generate_patient(num_files, output_directory):
    for i in range(num_files):
        patient_data = {
            "resourceType": "Patient",
            "id": f"patient_{i + 1}",
            "name": {
                "firstName": fake_data.first_name(),
                "secondName": fake_data.last_name()
            },
            "gender": random.choice(["male", "female", "other"]),
            "birthDate": fake_data.date_of_birth().strftime("%Y-%m-%d"),
            "address": {
                "city": fake_data.city(),
                "state": fake_data.state(),
                "country": fake_data.country()
            }
        }

        save_data_to_file(patient_data, output_directory, f"patient_{i + 1}")


def generate_practitioner(num_files, output_directory):
    for i in range(num_files):
        practitioner_data = {
            "resourceType": "Practitioner",
            "id": f"practitioner_{i + 1}",
            "name": {
                "firstName": fake_data.first_name(),
                "SecondName": fake_data.last_name()
            },
            "address": {
                "city": fake_data.city(),
                "state": fake_data.state(),
                "country": fake_data.country()
            },
            "qualification": {
                "title": fake_data.job(),
                "period": {
                    "start": fake_data.date_this_decade().strftime("%Y-%m-%d"),
                    "end": fake_data.date_this_decade().strftime("%Y-%m-%d")
                }
            }
        }

        save_data_to_file(practitioner_data, output_directory, f"practitioner_{i + 1}")


def generate_appointment(num_files, output_directory):
    patients = [f"patient_{i + 1}" for i in range(num_files)]
    practitioners = [f"practitioner_{i + 1}" for i in range(num_files)]

    for i in range(num_files):
        appointment_data = {
            "resourceType": "Appointment",
            "id": f"appointment_{i + 1}",
            "status": random.choice(["booked", "confirmed", "done"]),
            "class": random.choice(["ambulatory", "acute"]),
            "description": fake_data.sentence(),
            "start": fake_data.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
            "end": fake_data.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
            "created": fake_data.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
            "subject": {
                "reference": f"Patient/{random.choice(patients)}",
                "display": fake_data.name()
            },
            "participant": [{
                "reference": f"Practitioner/{random.choice(practitioners)}",
                "display": fake_data.name()
            }]
        }

        save_data_to_file(appointment_data, output_directory, f"appointment_{i + 1}")


def save_data_to_file(data, output_directory, filename):
    file_path = os.path.join(output_directory, f"{filename}.json")
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        print(f"File saved: {file_path}")
