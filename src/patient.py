"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import uuid
import datetime
from src.config import ROOM_MAX_CAPACITY, WARD_MAX_CAPACITY
from src.patient_db import PatientDB


class Patient:
    def __init__(self, name, gender, age):
        self.patient_id = str(uuid.uuid4())
        self.name = name
        self.gender = gender
        self.age = age
        self.checkin = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.checkout = None
        self.room = None
        self.ward = None

    def update_room_and_ward(self, room, ward):
        if room > ROOM_MAX_CAPACITY or ward > WARD_MAX_CAPACITY:
            raise ValueError("Room or ward capacity exceeded")
        self.room = room
        self.ward = ward

    def commit_to_database(self):
        patient_data = {
            "patient_id": self.patient_id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "checkin": self.checkin,
            "checkout": self.checkout,
            "room": self.room,
            "ward": self.ward,
        }
        patient_db = PatientDB()
        patient_db.insert_patient(patient_data)
