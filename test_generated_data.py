from data_generator import *
import json
import os
import pytest


@pytest.fixture
def output_directory(tmpdir):
    return str(tmpdir)


def test_generate_patient(output_directory):
    num_files = 3

    generate_patient(num_files, output_directory)

    assert len(os.listdir(output_directory)) == num_files

    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            assert data["resourceType"] == "Patient"
            assert "id" in data
            assert "name" in data
            assert "gender" in data
            assert "birthDate" in data
            assert "address" in data


def test_generate_practitioner(output_directory):
    num_files = 2

    generate_practitioner(num_files, output_directory)

    assert len(os.listdir(output_directory)) == num_files

    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            assert data["resourceType"] == "Practitioner"
            assert "id" in data
            assert "name" in data
            assert "address" in data
            assert "qualification" in data


def test_generate_appointment(output_directory):
    num_files = 6

    generate_appointment(num_files, output_directory)

    assert len(os.listdir(output_directory)) == num_files

    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            assert data["resourceType"] == "Appointment"
            assert "id" in data
            assert "status" in data
            assert "class" in data
            assert "description" in data
            assert "start" in data
            assert "end" in data
            assert "created" in data
            assert "subject" in data
            assert "participant" in data