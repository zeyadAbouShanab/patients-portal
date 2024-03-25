# Patients Portal

## Introduction

Patient Portal is a basic Patient management system, where the user (ie. receptionist) should do the folowing tasks:
- **List Patients:**
- **List Patients with a given name:**
- **Read a Patient with certain id:**
- **Create a Patient:**
- **Update the data of a Patient:**
- **Delete a Patient:**

## Prerequisites

- Install **Python** (recommended version >= 3.10)
- Install **Gitbash** (Optional)

## Installation Steps

Follow these steps to install the repository requirements:

1. **Clone the Repository:**

```bash
git clone https://github.com/amhkhowaja/patient-portal.git
```

2. **Navigate to the Repository:**
```bash
cd patient-portal
```

3. **Create a virtual environment**
```bash
python -m venv venv
```

4. **Activate the virtual environment**

*In linux (gitbash)*

```bash
source venv/bin/activate
```

*In windows*
```bash
source venv/Scripts/activate
```

5. **Install python packages to run the application**
```bash
python -m pip install -r requirements.txt
```

## Testing the final application

In Terminal :

First Run the flask server by running the API_CONTROLLER (`src/api_controller.py`) directly or using linux command:
```bash
python src/api_controller.py
```
Once the Flask server is running, open a new terminal and keep the server running in the first one.

Then,
```bash
cd testing-api-templates
```

Then,
```bash
bash create_patient.sh
```

If it returns the patient_id in the response then meaning that Patient has been created successfully and added to the database.

Then for listing the created patients,
```bash
bash list_patients.sh
```

Then for listing the created patients with \*name\* as parameter,
```bash
bash list_patient_by_name.sh
```

Then for getting a patient details with certain id,
```bash
bash get_certain_patient.sh
```

Then, to update the patient,
```bash
bash update_patient.sh
```

Finally, to delete the created patient,
```bash
bash delete_patient.sh
```


## You can Refer:

Flask Documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing

Flask Cheatsheet: https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf

Swagger Editor (Playground): https://editor.swagger.io/

Python OOP : https://docs.python.org/3/tutorial/classes.html


## Feedback

If you need more clarification, please ping me. I will update the readme file.
