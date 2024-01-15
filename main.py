from data_generator import *


def generate_data_menu():
    output_directory = "output"

    while True:
        print("\nSelect a resource to generate:")
        print("1. Patient")
        print("2. Practitioner")
        print("3. Appointment")
        print("4. Exit")

        choice = input("Enter the number from 1 to 4: ")

        if choice == '4':
            print("Exiting the data generator. Goodbye!")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a valid number.")
            continue

        try:
            num_files = int(input("What number of data files would you like to generate? "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        generate_resource(choice, num_files, output_directory)


def generate_resource(choice, num_files, output_directory):
    if choice == '1':
        generate_patient(num_files, output_directory)
    elif choice == '2':
        generate_practitioner(num_files, output_directory)
    elif choice == '3':
        generate_appointment(num_files, output_directory)


if __name__ == "__main__":
    generate_data_menu()
