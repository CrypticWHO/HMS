"""..................................Hospital Management System............................................."""





"""......START...........................Administrator's Code..............................................."""
# Constants
valid_roles = ["Admin", "Doctor", "Nurse", "Patient"]
contact_length = 10

def validate_login(user_id):
    try:
        with open("Users.txt", "r") as file:
            for line in file:
                # Skip the header line
                if line.startswith("UserID"):
                    continue
                # Split each line into fields (UserID, Name, Role, Contact)
                fields = line.strip().split(",")
                if user_id.strip() == fields[0].strip():  # Check exact match with UserID
                    return True
        print("User ID not found.")  # If no match is found
        return False
    except FileNotFoundError:
        print("Error: The file 'Users.txt' does not exist.")
        return False


def validate_atient_login(patient_id):
    try:
        with open("Patients.txt", "r") as file:
            for line in file:
                # Skip the header line
                if line.startswith("UserID"):
                    continue
                # Split each line into fields (UserID, Name, Role, Contact)
                fields = line.strip().split(",")
                if user_id.strip() == fields[0].strip():  # Check exact match with UserID
                    return True
        print("User ID not found.")  # If no match is found
        return False
    except FileNotFoundError:
        print("Error: The file 'Users.txt' does not exist.")
        return False



def validate_user_id(user_id):
    """Validating if user ID is numeric"""
    if not user_id.isdigit():
        print("Error: User ID must be numeric")
        return False
    else:
        return True

def validate_user_contact(contact):
    """Validating if contact number has 10 digits"""
    if len(contact) != contact_length or not contact.isdigit():
        print(f"Error: Contact number must be of 10 digits")
        return False
    else:
        return True

def validate_user_role(role):
    """Validating if role exists in valid roles"""
    if role not in valid_roles:
        print(f"Error: Invalid role!. Valid roles ar {valid_roles}\n")
        return False
    else:
        return True

def read_file(file_name, heading=True):
    """Reads data from file and returns heading and data"""
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        filtered_lines = [line.strip() for line in lines]

        if heading:  # if file has heading
            heading = filtered_lines[0]
            data = [line.split(",") for line in
                    filtered_lines[1:]]  # spliting data by commas after heading from 2nd line
            return heading, data

        else:  # if file has no heading
            data = [line.split(",") for line in filtered_lines]  # spliting data by commas when there is no heading
            return data

    except FileNotFoundError:
        print(f"Error: The file {file_name} is not available")
        return None, None
    except Exception as e:
        print(f"An unexpected error has been occurred: {e}")
        return None, None

def write_file(file_name, data, heading=True):
    """Writes data in file by joining through (,)"""
    with open(file_name, 'w') as file:
        if heading:
            file.write(f"{heading}\n")

        for line in data:
            file.write(",".join(line) + "\n")

def append_file(file_name, data):
    """Appends data in File from end by joining through (,)"""
    with open(file_name, 'a') as file:
        for line in data:
            file.write(",".join(line) + "\n")

def Search_User():
    """Special Feature: I have added a Search function to find and display user by Name or ID"""

    CHOICE = int(input("Choose the following: \n1.Search in Users (Hospital Staff) \n2. Search in Patients\n"))

    if CHOICE == 1:  # Performs search in Users.txt file (Hospital Staff)
        search_type = int(input("1. Search by UserID\n2. Search by UserName\n"))

        if search_type == 1:
            user_id = input("Enter a userID to search\n")
            heading, data = read_file("Users.txt")
            found = False
            for line in data:
                if line[0] == user_id:
                    found = True
                    print(
                        f"User found! \nuserID: {line[0]} \nuserName: {line[1]} \nuserName: {line[2]} \nuserContact: {line[3]}\n")
                    break
            if not found:
                print(f"No user found with userID: {user_id}")

        elif search_type == 2:
            user_name = input("Enter a userName to search\n").lower()
            heading, data = read_file("Users.txt")
            found = False
            for line in data:
                if line[1].lower() == user_name:
                    found = True
                    print(
                        f"User found! \nuserID: {line[0]} \nuserName: {line[1]} \nUserRole: {line[2]} \nUserContact: {line[3]}\n")
                break
            if not found:
                print(f"No user found with userName: {user_name}")

        else:
            print("Invalid search type. Please enter 1 or 2.")

    elif CHOICE == 2:  # Performs search in Patients.txt file
        search_type = int(input("1. Search by PatientID\n2. Search by Patient Name\n"))
        if search_type == 1:  # Search by ID
            patient_id = input("Enter a PatientID to search\n")
            heading, data = read_file("Patients.txt")
            found = False
            for line in data:
                if line[0] == patient_id:
                    found = True
                    print(
                        f"""Patient found! \nPatientID: {line[0]} \nName: {line[1]} \nAge: {line[2]}\nGender: {line[3]}\nContact: {line[4]}\nAddress: {line[5]} \nCondition: {line[6]}\nDoctor Assigned: {line[7]}\nInsurance Status: {line[8]}\n Discharge Status: {line[9]}\n""")
                    break
            if not found:
                print(f"No patient found with patientID: {patient_id}")

        elif search_type == 2:  # Search by Name
            patient_name = input("Enter a Patient Name to search\n").lower()
            heading, data = read_file("Patients.txt")
            found = False
            for line in data:
                if line[1].lower() == patient_name:
                    found = True
                    print(
                        f"""Patient found! \nPatientID: {line[0]} \nName: {line[1]} \nAge: {line[2]}\nGender: {line[3]}\nContact: {line[4]}\nAddress: {line[5]} \nCondition: {line[6]}\nDoctor Assigned: {line[7]}\nInsurance Status: {line[8]}\n Discharge Status: {line[9]}\n""")
                    break
            if not found:
                print(f"No patient found with Name: {patient_name}")

        else:
            print("Invalid search type. Please enter 1 or 2.")
    else:
        print("Invalid search type. Please enter 1 or 2.")

def Create_User():
    """Creates a new user after validating the given information"""
    User_ID = input("Enter User ID: ").strip()
    if not validate_user_id(User_ID):
        return  # if ID is not numeric then stop the function

    User_Name = input("Enter User Name: ").strip()
    if not User_Name:
        print(f"Error : User Name cannot be empty!")
        return  # if username not entered and skipped then stop the function

    User_Role = input("Enter User Role: ").strip()
    if not validate_user_role(User_Role):
        return  # if role is not valid then stop the function

    User_Contact = input("Enter User Contact: ").strip()
    if not validate_user_contact(User_Contact):
        return  # if contact length is not 10 digits then stop the function

    # If all validations pass then create the user.
    new_user_data = [[User_ID, User_Name, User_Role, User_Contact]]
    append_file("Users.txt", new_user_data)
    print(f"""User Created Successfully""")

def Update_User():
    """Updating the user after validating the new information about existing user"""
    current_User_id = input("Please enter a userID to update")
    if not validate_user_id(current_User_id):
        return  # if userID is not numeric then stop the function

    new_User_ID = input("Enter a new userID")
    if not validate_user_id(new_User_ID):
        return  # if userID is not numeric then stop the function

    new_User_Name = input("Enter a new User Name")
    if not new_User_Name:
        return  # if username is empty then stop the function

    new_User_Role = input("Enter a new User Role")
    if not validate_user_role(new_User_Role):
        return  # if user role is not valid then stop the function

    new_User_Contact = input("Enter a new User Contact")
    if not validate_user_contact(new_User_Contact):
        return  # if contact length is not 10 digits then stop the function

    # if all validations pass then update the user
    heading, data = read_file("Users.txt")
    found = False

    for i in range(len(data)):
        user = data[i]
        if user[0] == current_User_id:
            found = True
            data[i] = [new_User_ID, new_User_Name, new_User_Role, new_User_Contact]
            break

    if found:
        # writing data back into file
        write_file("Users.txt", data, heading)
        print("User has been updated in file Successfully!")
    else:
        print("User not found")

def Delete_User():
    """Deleting the user after validating the existance of given user"""

    user_id = input(f"Enter a user to delete")
    if not validate_user_id(user_id):
        return  # if user id is not numeric then stop the function

    heading, users_list = read_file("Users.txt")

    found = False
    for i in range(len(users_list)):
        if user_id == users_list[i][0]:  # Comparing user_id to find location of user data
            found = True
            del users_list[i]  # Removing user data from list
            break

    if found:
        write_file("Users.txt", users_list, heading)
        print(f"User {user_id} has been deleted Successfully")

    else:
        print(f"User not found!")

def Add_Bed():
    """This function adds a bed to Hospital's available resources"""
    Update_Bed_Status("Resources.txt", "add")

def Remove_Bed():
    """This function removes a bed from Hospital's available resources"""
    Update_Bed_Status("Resources.txt", "remove")

def Update_Bed():
    """This function updates a bed to Hospital's available resources"""
    Update_Bed_Status("Resources.txt", "update")

def Update_Bed_Status(file_name, action):
    """This Function handles wll operations related to bed status: add, remove or update"""
    try:
        heading, data = read_file(file_name)

        if heading is None:
            return  # Exit function if file has no heading
        total_beds = int(data[0][0])
        occupied_beds = int(data[0][1])
        available_beds = int(data[0][2])

        if action == "add":
            total_beds += 1
            available_beds += 1

        elif action == "remove":
            if total_beds > occupied_beds:
                total_beds -= 1
                available_beds -= 1
            else:
                print("Cannot remove a bed as all beds are occupied currently")

        elif action == "update":
            print("Please choose an option")
            Choice = int(input(f"""1. Mark Bed as Occupied\n2. Mark Bed as Available"""))
            if Choice == 1:
                occupied_beds += 1
                available_beds -= 1
            elif Choice == 2:
                occupied_beds -= 1
                available_beds += 1
            else:
                print("Invalid choice")
                return

        # updating data
        data = [[str(total_beds), str(occupied_beds), str(available_beds)]]

        write_file("Resources.txt", data, heading)  # writing beds data back into file
        print(f"Bed has been {action}ed Successfully!")

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

def View_Policies():
    """This function views Policies from Policies File"""
    heading, data = read_file("Policies.txt")
    print("Following are the current Policies:")
    print(heading)
    for line in data:
        print(",".join(line))

def Set_Policies():
    """This function Sets Policies in Policies File"""
    heading, data = read_file("Policies.txt")
    print("Kindly view the existing policies")
    View_Policies()

    print("Enter your choice: ")
    choice = int(input(f"""1. Add a new policy \n2. overwrite existing policies """))
    if choice == 1:
        policy_title = input("Enter Policy Title")
        policy_details = input("Enter policy details")
        policy = [[policy_title, policy_details]]
        append_file("Policies.txt", policy)
        print("A new policy has been added Successfully!")

    elif choice == 2:
        policies = []
        num = int(input("Enter number of policies you will be adding"))
        for i in range(num):
            policy_title = input(f"Enter Policy Title for policy no. {i + 1}: ")
            policy_details = input(f"Enter policy details for policy no. {i + 1}:")
            policies.append([policy_title, policy_details])
        write_file("Policies.txt", policies, heading)
        print("Policies has been updated successfully")

def Manage_User_Accounts():
    """This function provides menu for handling creating, updating and deleting users in Users File"""
    print(f""" "User Account Options" \n Enter your choice to proceed""")
    choice = int(input(f"""1. Create User\n
                       2. Update User\n
                       3. Delete User\n"""))
    if choice == 1:
        Create_User()
    elif choice == 2:
        Update_User()
    elif choice == 3:
        Delete_User()

def get_user_counts():
    """This function counts no. of doctors and nurses (staff) in hospital"""
    total_doctors = 0
    total_nurses = 0
    heading, data = read_file("Users.txt")

    for i in range(len(data)):
        role = data[i][2].strip()
        if role == 'Doctor':  # assuming role [2] in file where heading = UserID,Name,Role,Contact
            total_doctors += 1
        elif role == 'Nurse':
            total_nurses += 1
    return total_doctors, total_nurses

def View_Statistics():
    """This function views  Overall Hospital Statistics from Resources File"""

    total_patients = 0
    heading, data = read_file("Patients.txt")
    for line in data:
        total_patients += 1

    total_doctors, total_nurses = get_user_counts()  # read and store total_doctors and total_nurses from file

    heading, data2 = read_file("Resources.txt")
    available_beds = int(data2[0][2])  # Assuming the data format: total, occupied, available beds

    print(
        f"""1. total patients = {total_patients}\n2. total doctors = {total_doctors}\n3. total nurses = {total_nurses}\n4. available beds = {available_beds}""")

def Generate_Report():
    """This function computes and generates a report of hospital resources into Report File"""
    total_patients = 0
    heading, data = read_file("Patients.txt")
    for line in data:
        total_patients += 1

    total_doctors, total_nurses = get_user_counts()  # getting total doctors and nurses

    heading, data2 = read_file("Resources.txt")
    total_beds = int(data2[0][0])
    occupied_beds = int(data2[0][1])
    available_beds = int(data2[0][2])

    write_file("Report.txt", data)
    report_data = [(
                       f"""Hospital Report\nTotal patients: {total_patients}\nTotal Doctors: {total_doctors}\nTotal Nurses: {total_nurses}\n
    Total Beds: {total_beds}\nOccupied Beds: {occupied_beds}\nAvailable Beds: {available_beds}\n""")]

    write_file("Report.txt", [report_data])
    print("Report has been generated Successfully!")

def Manage_Hospital_Resources():
    """This function provides menu for handling adding, removing and updating bed in Resources File"""
    print("Choose your option")
    num = int(input("1. Add Beds\n2. Remove Beds\n3. Update Bed Status\n"))

    try:
        if num == 1:
            Add_Bed()
        elif num == 2:
            Remove_Bed()
        elif num == 3:
            Update_Bed()
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid input! please enter a number")

def Set_And_View_Operational_Policies():
    """This function provides menu for handling Setting and viewing current Hospital Policies from Policies File"""

    print("Choose from the options")
    choice = int(input(f"""1. View Policies\n2. Set Policies\n"""))
    if choice == 1:
        View_Policies()
    elif choice == 2:
        Set_Policies()
    else:
        print("Invalid Choice")

# Administrator's Menu
def Display_Administrator_Menu():
    """This function provides menu for handling tasks of Administrator's Role"""

    print("Administrator's Menu")
    while True:
        print("Enter your Choice to proceed:")
        print(
            f"""1. Manage User Accounts\n2. View Hospital Statistics"\n3. Generate Report\n4. Manage Hospital Resources\n5. Set and View Operational Policies\n6. Search FUnction\n7. Exit\n""")
        try:
            option = int(input())
            if option == 1:
                Manage_User_Accounts()

            elif option == 2:
                View_Statistics()

            elif option == 3:
                Generate_Report()

            elif option == 4:
                Manage_Hospital_Resources()

            elif option == 5:
                Set_And_View_Operational_Policies()
            elif option == 6:
                Search_User()
            elif option == 7:  # exit
                break
        except ValueError:
            print("Invalid input! Please enter a number")

"""......END...........................Administrator's Code................................................."""

"""......START...........................Doctotor's Code...................................................."""
user_records_file = "Users.txt"
patient_records_file = "Patients.txt"
schedule_appointment_file = "Appointments.txt"
medical_history_file = "Medical_Records.txt"
#.....................................................use this login..................................
# Login function
def doctor_login():
    print("#" * 40)
    print(f"{'#-----🥼 Doctor Login 🥼-----#':^40}")
    print("#" * 40)

    while True:
        doctor_id = input("Enter your Doctor ID ▶ : ").strip().upper()

        if validate_doctor_id(doctor_id):
            print(f"Welcome, Doctor ID: {doctor_id}")
            doctor_menu(doctor_id)
            break
        else:
            print("  " * 40)
            print("-" * 55)
            print(f"{'*****⛔️Invalid Doctor ID. Please try again. ⛔️***** ':^40}")
            print("-" * 55)

            retry = input("To re-enter Doctor ID press ▶ 'Y'. To exit press ▶ 'N': ").strip().upper()
            if retry == 'N':
                print(f"{'-----👋Goodbye! 👋-----'} ^40")
                exit()
            elif retry == 'Y':
                doctor_login()

# Doctor's Menu
def doctor_menu(doctor_id):
    while True:
        print("  " * 40)
        print("#" * 40)
        print(f"{'-----📃MENU 📃-----':^40}")
        print("1. ⭕️View Patient List")
        print("2. ⭕️Update Patient Record")
        print("3. ⭕️Schedule Follow-up Appointment")
        print("4. ⭕️View Medical History")
        print("5. ⭕️Issue Discharge Approval")
        print("6. ⭕️Exit")
        print("#" * 40)

        choice = input("\n ⭕️Choose an option from 1-6 ▶ : ").strip()

        if choice == "1":
            view_patient_list(doctor_id)
        elif choice == "2":
            update_patient_record()
        elif choice == "3":
            schedule_follow_up(doctor_id)
        elif choice == "4":
            view_medical_history()
        elif choice == "5":
            issue_discharge_approval()
        elif choice == "6":
            print("  " * 40)
            print("-" * 40)
            print(f"{'-----👋Goodbye! 👋-----':^40}")
            print("-" * 40)
            print("  " * 40)
            break
        else:
            print("*" * 45)
            print(f"{'-----⛔️Invalid choice. Please choose a valid option.⛔️-----':^40}")
            print("*" * 45)

# Validate Doctor ID
def validate_doctor_id(doctor_id):
    try:
        with open(user_records_file, "r") as file:
            for line in file:
                if doctor_id in line:
                    return True
    except FileNotFoundError:
        print("*" * 40)
        print(f"{'-----⛔️User records file not found.⛔️-----':^40}")
        print("*" * 40)
    return False

# View Patient List
def view_patient_list(doctor_id):
    try:
        with open(patient_records_file, "r") as file:
            print("#" * 40)
            print(f"{'-----✅Patients assigned to you:✅-----':^40}")
            print("#" * 40)
            found = False
            for line in file:
                if doctor_id in line:
                    patient_data = line.strip().split(",")
                    print(f"Patient ID: {patient_data[0]} - Name: {patient_data[1]} - Age: {patient_data[2]} - Gender: {patient_data[3]}")
                    found = True
            if not found:
                print("⛔️No patients assigned to this doctor.⛔️")


    except FileNotFoundError:
        print("-" * 40)
        print(f"{'-----⛔️Patient records file not found.⛔️-----':^40}")
        print("-" * 40)
        return False

    go_back_or_exit(doctor_id)  # After viewing the list, ask if they want to go back or exit
    return True

# Update Patient Record
def update_patient_record():
    try:
        patient_id = input("Enter Patient ID: ").strip().upper()
        print("Enter new details for the patient:")
        diagnosis = input("Diagnosis: ").strip()
        prescription = input("Prescription: ").strip()
        treatment_plan = input("Treatment Plan: ").strip()

        if not diagnosis or not prescription or not treatment_plan:
            print("All fields must be filled.")
            return False

        updated = False

        # Reading the file
        with open(medical_history_file, "r") as file:
            lines = file.readlines()

        # Writing updated information back to the file
        with open(medical_history_file, "w") as file:
            for line in lines:
                fields = line.strip().split(",")
                if fields[0] == patient_id:
                    fields[2] = diagnosis
                    fields[3] = prescription
                    fields[4] = treatment_plan
                    updated = True
                file.write(",".join(fields) + "\n")

        if updated:
            print("-" * 40)
            print(f"{'-----✅ Patient record updated successfully. ✅-----':^40}")
            print("-" * 40)
        else:
            print("-" * 40)
            print(f"{'-----⛔️ Patient ID not found. ⛔️-----':^40}")
            print("-" * 40)

    except FileNotFoundError:
        print("-" * 40)
        print(f"{'-----⛔️ Medical history file not found. ⛔️-----':^40}")
        print("-" * 40)
        return False

    return updated

# Schedule Follow-up Appointment
def schedule_follow_up(doctor_id):
    try:
        patient_id = input("Enter Patient ID: ").strip()
        date = input("Appointment Date (YYYY-MM-DD): ").strip()
        time = input("Appointment Time (HH:MM): ").strip()

        # Make sure to correctly write the entire details to the file
        with open(schedule_appointment_file, "a") as file:
            file.write(f"{patient_id},{doctor_id},{date},{time}\n")

        print("-" * 40)
        print(f"{'-----✅ Appointment scheduled successfully. ✅-----':^40}")
        print("-" * 40)

    except FileNotFoundError:
        print("-" * 40)
        print(f"{'-----⛔️ Appointment file not found. ⛔️-----':^40}")
        print("-" * 40)
        return False

    go_back_or_exit(doctor_id)
    return True

# View Medical History
def view_medical_history():
    try:
        patient_id_input = input("Enter Patient ID: ").strip().upper()
        found = False

        with open(medical_history_file, "r") as file:
            print("#" * 50)
            print(f"-----◀️Medical history for patient ID {patient_id_input}:▶️-----")
            print("#" * 50)
            for line in file:
                patient_data = line.strip().split(",")
                if patient_data[0] == patient_id_input:
                    print(f"Patient ID: {patient_data[0]},- Date: {patient_data[1]}  ,- Diagnosis: {patient_data[2]},- Prescription: {patient_data[3]},- TreatmentPlan: {patient_data[4]} ,- Followups: {patient_data[5]}")
                    found = True
                    break
        if not found:
            print(f"{'----- ⛔️No medical history found for this patient.⛔️-----':^40}")
    except FileNotFoundError:
        print("-" * 40)
        print(f"{'-----⛔️Medical history file not found.⛔️-----':^40}")
        print("-" * 40)
        return False

    return found

# Issue Discharge Approval
def issue_discharge_approval():
    try:
        patient_id = input("Enter Patient ID : ").strip().upper()
        discharge_status = input("Do you want to discharge this patient? (Yes/No): ").strip().upper()

        if discharge_status == "YES":
            updated = False
            lines = []

            with open(patient_records_file, "r") as file:
                for line in file:
                    if patient_id in line:
                        parts = line.strip().split(",")
                        if parts[-1] == "No":
                            line = line.replace(parts[-1], "Yes")
                            updated = True
                        lines.append(line + "\n")
                    else:
                        lines.append(line)

            with open(patient_records_file, "w") as file:
                file.writelines(lines)

            if updated:
                print("=" * 40)
                print(f"{'-----✅ Patient discharged successfully.✅ -----':^40}")
                print("=" * 40)
            else:
                print("-" * 40)
                print(f"{'-----⛔️ Patient discharge status is already Yes or Patient ID not found.⛔️ -----':^40}")
                print("-" * 40)

        if discharge_status == "NO":
            print("-" * 40)
            print(f"{'-----❌ Patient discharge canceled.❌ -----':^40}")
            print("-" * 40)
            doctor_menu()

    except FileNotFoundError:
        print("-" * 40)
        print(f"{'-----⛔️ Patient records file not found.⛔️ -----':^40}")
        print("-" * 40)
        return False

    return True

# Exit or Continue
def go_back_or_exit(doctor_id):
    choice = input("Would you like to go back to the main menu or exit? (Enter 'M' for main menu or 'E' to exit): ").upper().strip()
    if choice == 'M':
        doctor_menu(doctor_id)
    elif choice == 'E':
        print(f"{'-----👋Goodbye! 👋-----'} ^40")
        exit()
    else:
        print(" " * 40)
        print("-" * 40)
        print("-----⛔Invalid input. Please enter 'M' to go back to the main menu or 'E' to exit.⛔-----")
        print("-" * 40)
        go_back_or_exit(doctor_id)

"""......END...........................Doctotor's Code......................................................"""



"""......START...........................Nurse's Code...................................................."""

def get_current_time():
    """Generate the current date and time in the format YYYY-MM-DD,HH:MM:SS."""
    # Manually get current date and time using the local time in a format
    import time
    current_time = time.localtime()
    return f"{current_time.tm_year}-{current_time.tm_mon:02d}-{current_time.tm_mday},{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

def validate_patient_id(patient_id):
    """Validate if the patient ID exists in Patients.txt."""
    try:
        with open('Patients.txt', 'r') as file:
            for line in file:
                if line.startswith(patient_id):
                    return True
        return False
    except FileNotFoundError:
        print("Error: Patients.txt file not found.")
        return False


def prompt_for_valid_patient_id():
    """Prompt the user to enter a valid Patient ID until a correct one is provided."""
    while True:
        patient_id = input("Enter Patient ID: ")
        if validate_patient_id(patient_id):
            return patient_id
        print("Invalid Patient ID. Please try again.")


def update_patient_observation(patient_id, new_observation, heartrate, blood_pressure):
    """Update the patient's observation and vitals in the observation records."""
    patient_id = prompt_for_valid_patient_id()  # Ensure valid patient ID is entered
    try:
        with open('Observations.txt', 'r') as file:
            lines = file.readlines()

        with open('Observations.txt', 'w') as file:
            updated = False
            current_time = get_current_time()

            for line in lines:
                if line.startswith(patient_id):
                    line = f"{patient_id},{new_observation},Heartrate:{heartrate},BP:{blood_pressure},{current_time}\n"  # Update line with new data
                    updated = True
                file.write(line)

            if not updated:
                file.write(
                    f"{patient_id},{new_observation},Heartrate:{heartrate},BP:{blood_pressure},{current_time}\n")  # Add new record if patient not found
        print("Patient observation and vitals updated successfully.")
    except FileNotFoundError:
        print("Error: Observation records file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def log_medication(patient_id, medication_details):
    """Log medication administered to a patient with a timestamp."""
    patient_id = prompt_for_valid_patient_id()  # Ensure valid patient ID is entered
    try:
        current_time = get_current_time()
        with open('Medication_Logs.txt', 'a') as file:
            file.write(f"{patient_id},{medication_details},{current_time}\n")  # Append medication log
        print("Medication logged successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_medical_record(patient_id):
    """Update a patient's medical record with diagnosis, prescription, treatment plan, and follow-up date."""
    patient_id = prompt_for_valid_patient_id()  # Ensure valid patient ID is entered
    try:
        # Get current time for date in medical record
        current_time = get_current_time()

        # Prompt for diagnosis, prescription, and treatment plan
        diagnosis = input("Enter diagnosis: ")
        prescription = input("Enter prescription: ")
        treatment_plan = input("Enter treatment plan: ")

        # Ask for follow-up date and validate if it is in the future
        while True:
            follow_up_date = input("Enter follow-up date (YYYY-MM-DD): ")
            if validate_future_date(follow_up_date):
                break
            else:
                print("Error: Follow-up date must be in the future. Please enter a valid date.")

        # Append the medical record to the file
        with open('Medical_Records.txt', 'a') as file:
            file.write(f"{patient_id},{current_time},{diagnosis},{prescription},{treatment_plan},{follow_up_date}\n")

        print("Medical record updated successfully.")
    except FileNotFoundError:
        print("Error: Medical_Records.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def validate_future_date(date_str):
    """Validate if the date is in the future."""
    try:
        # Manually check if the entered date is in the future
        year, month, day = map(int, date_str.split('-'))
        today = input("Enter today's date (YYYY-MM-DD): ").split('-')
        today_year, today_month, today_day = map(int, today)

        if year > today_year:
            return True
        elif year == today_year:
            if month > today_month:
                return True
            elif month == today_month:
                if day > today_day:
                    return True
        return False
    except ValueError:
        return False


def retrieve_patient_info(patient_id):
    """Retrieve and display a patient's information, vitals, and observations."""
    patient_id = prompt_for_valid_patient_id()  # Ensure valid patient ID is entered
    try:
        # Read patient details from Patients.txt
        patient_details = None
        with open('Patients.txt', 'r') as file:
            for line in file:
                if line.startswith(patient_id):
                    patient_details = line.strip().split(',')
                    break

        if not patient_details:
            return "Patient not found."

        # Format patient details
        patient_headings = [
            "PatientID", "Name", "Age", "Gender", "Contact", "Address", "Condition", "DoctorID", "Insurance",
            "Discharge"
        ]
        patient_info = "\n".join(
            f"{heading}: {value}" for heading, value in zip(patient_headings, patient_details)
        )

        # Read observations and vitals from Observations.txt
        observations = []
        with open('Observations.txt', 'r') as file:
            for line in file:
                if line.startswith(patient_id):
                    observation_details = line.strip().split(',')
                    observations.append(
                        f"Observation: {observation_details[1]}\nHeartrate: {observation_details[2]}\nBP: {observation_details[3]}\nDate: {observation_details[4]}"
                    )

        if observations:
            observation_info = "\n\nObservations:\n" + "\n\n".join(observations)
        else:
            observation_info = "\n\nNo observations found."

        # Combine and return patient and observation details
        return patient_info + observation_info

    except FileNotFoundError as e:
        return f"Error: {e.filename} file not found."
    except Exception as e:
        return f"An error occurred: {e}"


def Nurse_menu():
    while True:
        print("\nNurse Menu:")
        print("1. Update Patient Observation and Vitals")
        print("2. Log Medication")
        print("3. Update Medical Record")
        print("4. Retrieve Patient Info")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            patient_id = prompt_for_valid_patient_id()
            new_observation = input("Enter new observation: ")
            heartrate = input("Enter heartrate (in bpm): ")
            blood_pressure = input("Enter blood pressure (x/x): ")
            update_patient_observation(patient_id, new_observation, heartrate, blood_pressure)

        elif choice == '2':
            patient_id = prompt_for_valid_patient_id()
            medication_details = input("Enter medication details: ")
            log_medication(patient_id, medication_details)

        elif choice == '3':
            patient_id = prompt_for_valid_patient_id()
            update_medical_record(patient_id)

        elif choice == '4':
            patient_id = prompt_for_valid_patient_id()
            info = retrieve_patient_info(patient_id)
            print(info)

        elif choice == '5':
            print("Exiting the Nurse Menu.")
            break
        else:
            print("Invalid option. Please try again.")

"""......END...........................Nurse's Code......................................................"""



"""......START...........................Receptionist's Code...................................................."""
# Function to display the main menu
def display_menu():
    print("\n Welcome to Receptionist Management System")
    print("1. Register a new patient")
    print("2. Update Patient Information")
    print("3. Schedule an appointment")
    print("4. View hospital services, doctors, and departments")
    print("5. Check-in a patient")
    print("6. Check-out a patient")
    print("7. Record services used")
    print("8. Generate and view billing")
    print("9. Send Appointment Reminders")
    print("10. Exit")

# Function to register a new patient
def register_patient():
    patient_id = input("Enter patient ID (unique): ").strip()
    name = input("Enter patient's name: ").strip()

    while True:
        age = input("Enter patient's age: ").strip()
        if age.isdigit():
            break
        else:
            print("Invalid input. Please enter a valid age (numeric).")

    while True:
        gender = input("Enter patient's gender (M/F): ").strip().upper()
        if gender in ["M", "F"]:
            break
        else:
            print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

    while True:
        contact = input("Enter patient's contact number: ").strip()
        if contact.isdigit():
            break
        else:
            print("Invalid input. Contact number must be numeric.")

    address = input("Enter patient address: ").strip()

    condition = input("Enter patient condition: ").strip()

    doctor_id = input("Enter patient Assigned Doctor ID: ").strip()

    with open("Patients.txt", "a") as file:
        file.write(f"{patient_id},{name},{age},{gender},{contact},{address},{condition},{doctor_id}\n")

    print(f"Patient {name} registered successfully.")

# Function to update patient information
def update_patient_info():
    print("\nUpdate Patient Information")
    patient_id = input("Enter Patient ID to update: ").strip()

    try:
        with open("Patients.txt", "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No patients found. Please register a patient first.")
        return

    updated = False
    for i, record in enumerate(records):
        data = record.strip().split(",")
        if data[0] == patient_id:
            print("Leave the field blank to keep the current value.")
            new_name = input("Enter new name: ").strip() or data[1]

            while True:
                new_contact = input("Enter new contact number: ").strip() or data[4]
                if new_contact.isdigit():
                    break
                else:
                    print("Invalid input. Contact number must be numeric.")

            new_address = input("Enter new home address: ").strip() or data[5]
            new_condition = input("Enter new medical condition: ").strip() or data[6]
            new_doctor_id = input("Enter new doctor ID: ").strip() or data[7]

            records[i] = f"{data[0]},{new_name},{data[2]},{data[3]},{new_contact},{new_address},{new_condition},{new_doctor_id}\n"
            updated = True
            break

    if updated:
        with open("Patients.txt", "w") as file:
            file.writelines(records)
        print("Patient information updated successfully.")
    else:
        print("Patient ID not found.")

# Function to schedule an appointment
def schedule_appointment():
    patient_id = input("Enter patient ID: ").strip()
    doctor_id = input("Enter doctor ID: ").strip()

    while True:
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
        if len(appointment_date) == 10 and appointment_date.count("-") == 2:
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        appointment_time = input("Enter appointment time (HH:MM): ").strip()
        if len(appointment_time) == 5 and appointment_time.count(":") == 1:
            break
        else:
            print("Invalid time format. Please use HH:MM.")

    with open("Appointments.txt", "a") as file:
        file.write(f"{patient_id},{doctor_id},{appointment_date},{appointment_time}\n")

    print(f"Appointment scheduled for patient ID {patient_id} with doctor ID {doctor_id}.")

#Function to view hospital Information
def view_hospital_info():
    print("\n-- Hospital Information --")

    # hospital services
    services = ["General Consultation", "Pediatrics", "Cardiology", "Orthopedics", "Dermatology"]

    #Doctors
    doctors = [
        {"ID": "D001", "Name": "Dr. Susan Clark", "Specialty": "Cardiology","Contact":"2345678901"},
        {"ID": "D002", "Name": "Dr. John Smith", "Specialty": "Pediatrics","Contact":"1122334455"},
        {"ID": "D003", "Name": "Dr. Robert Darris", "Specialty": "Orthopedics","Contact":"1222334555"},
        {"ID": "D004", "Name": "Dr. Linda Johnson", "Specialty": "Dermatology","Contact":"1123334445"},
    ]

    #Departments
    departments = ["Emergency", "Outpatient", "Inpatient", "Radiology", "Pharmacy"]

    # Display hospital services
    print("\nAvailable Hospital Services:")
    for service in services:
        print(f"- {service}")

    # Display doctors
    print("\nDoctors:")
    for doctor in doctors:
        print(f"- ID: {doctor['ID']}, Name: {doctor['Name']}, Specialty: {doctor['Specialty']}, Contact: {doctor['Contact']}")

    # Display departments
    print("\nHospital Departments:")
    for department in departments:
        print(f"- {department}")

    print("\n-- End of Hospital Information")

# Function to check in a patient
def check_in_patient():
    patient_id = input("Enter patient ID: ").strip()
    check_in_time = input("Enter check-in time (YYYY-MM-DD HH:MM): ").strip()

    with open("check_in.txt", "a") as file:
        file.write(f"{patient_id},{check_in_time}\n")

    print(f"Patient {patient_id} checked in at {check_in_time}.")

# Function to check out a patient
def check_out_patient():
    patient_id = input("Enter patient ID: ").strip()
    check_out_time = input("Enter check-out time (YYYY-MM-DD HH:MM): ").strip()

    with open("check_out.txt", "a") as file:
        file.write(f"{patient_id},{check_out_time}\n")

    print(f"Patient {patient_id} checked out at {check_out_time}.")

# Function to record services used by a patient
def record_services():
    patient_id = input("Enter patient ID: ").strip()
    service_name = input("Enter service name: ").strip()

    while True:
        service_cost = input("Enter service cost: ").strip()
        if service_cost.replace(".", "", 1).isdigit():
            service_cost = float(service_cost)
            break
        else:
            print("Invalid input. Please enter a valid numeric value for service cost.")

    with open("services_used.txt", "a") as file:
        file.write(f"{patient_id},{service_name},{service_cost}\n")

    print(f"Service {service_name} recorded for patient {patient_id}.")

#Function to generate bill
def generate_billing():
    billing = {}

    try:
        with open("services_used.txt", "r") as file:
            for line_num, line in enumerate(file, start=1):
                parts = line.strip().split(",")

                # Validate line format
                if len(parts) != 3:
                    continue

                patient_id, service_name, service_cost = parts

                try:
                    service_cost = float(service_cost)  # Convert cost to float
                except ValueError:
                    continue

                # Add to billing dictionary
                if patient_id in billing:
                    billing[patient_id] += service_cost
                else:
                    billing[patient_id] = service_cost

        # Get the patient ID to display the total amount
        patient_id = input("Enter Patient ID to view the total amount: ").strip()

        if patient_id in billing:
            total_amount = billing[patient_id]
            print(f"Patient ID: {patient_id}, Your Total Bill is {total_amount:.2f} RM")

            with open("Billing.txt", "a") as file:
                file.write(f"{patient_id},{total_amount:.2f}\n")
        else:
            print(f"No billing information found for the Patient ID {patient_id}.")
    except FileNotFoundError:
        print("No services recorded yet.")

# Function to send appointment reminders
# Function to manually calculate tomorrow's date
def get_tomorrows_date():
    today = input("Enter today's date in YYYY-MM-DD format: ").strip()
    year, month, day = map(int, today.split('-'))

    # Calculate tomorrow's date
    day += 1

    # Handle  amount of day in a month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            day = 1
            month += 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day = 1
            month += 1
    elif month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and day > 29:  # Leap year check
            day = 1
            month += 1
        elif day > 28:
            day = 1
            month += 1

    if month > 12:
        month = 1
        year += 1

    # Return tomorrow's date in the same format YYYY-MM-DD
    return f"{year:04d}-{month:02d}-{day:02d}"

# Function to send appointment reminders with contact notification
def send_appointment_reminders():
    tomorrow_date = get_tomorrows_date()  # Get tomorrow's date

    try:
        with open("Appointments.txt", "r") as file:
            appointments = file.readlines()
    except FileNotFoundError:
        print("No appointments found.")
        return

    reminder_found = False
    for appointment in appointments:
        data = appointment.strip().split(",")
        appointment_date = data[2]  # Appointment date is the 3rd value in the record

        if appointment_date == tomorrow_date:  # Check if the appointment is for tomorrow
            patient_id = data[0]  # Patient ID is the 1st value
            doctor_id = data[1]  # Doctor ID is the 2nd value

            # Get the patient's contact number from the Patients.txt file
            try:
                with open("Patients.txt", "r") as patient_file:
                    patients = patient_file.readlines()
            except FileNotFoundError:
                print("No patient data found.")
                return

            patient_contact = None
            for patient in patients:
                patient_data = patient.strip().split(",")
                if patient_data[0] == patient_id:  # Match the Patient ID
                    patient_contact = patient_data[4]  # Contact is the 5th value in the record
                    break

            if patient_contact:
                # Send reminder (here, we print it as a simple reminder notification)
                print(
                    f"Reminder: Patient ID {patient_id} has an appointment tomorrow ({appointment_date}) with Doctor ID {doctor_id}.")
                print(f"Reminder sent to Patient ID {patient_id} at Contact: {patient_contact}")
                reminder_found = True
            else:
                print(f"Could not find contact information for Patient ID {patient_id}.")

    if not reminder_found:
        print(f"No appointments found for tomorrow ({tomorrow_date}).")
    else:
        print("Reminder process complete.")

# Main program loop
def Receptionist_Menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            register_patient()
        elif choice == '2':
            update_patient_info()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_hospital_info()
        elif choice == '5':
            check_in_patient()
        elif choice == '6':
            check_out_patient()
        elif choice == '7':
            record_services()
        elif choice == '8':
            generate_billing()
        elif choice == '9':
            send_appointment_reminders()
        elif choice == '10':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

"""......END...........................Receptionist's Code......................................................"""


"""......START...........................Patient's Code......................................................"""
def patient_menu():
    initialize_files()
    while True:
        print("\n--- Patient Menu ---")
        print("1. View Personal Information")
        print("2. Book an Appointment")
        print("3. View Appointments")
        print("4. Update Personal Information")
        print("5. Give Feedback")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again")
            continue

        if choice == 1:
            view_personal_info()
        elif choice == 2:
            book_appointment()
        elif choice == 3:
            view_appointments()
        elif choice == 4:
            update_personal_information()
        elif choice == 5:
            give_feedback()
        elif choice == 6:
            print("Exiting Patient Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def validate_date(date_text):
    try:
        year, month, day = map(int, date_text.split("-"))
        assert 1 <= month <= 12
        assert 1 <= day <= 31
        return True
    except (ValueError, AssertionError):
        return False

def validate_time(time_text):
    try:
        hour, minute = map(int, time_text.split(":"))
        assert 0 <= hour < 24
        assert 0 <= minute < 60
        return True
    except (ValueError, AssertionError):
        return False

def is_future_appointment(date, time):
    try:
        from time import strptime, mktime, localtime
        appointment_time = mktime(strptime(f"{date} {time}", "%Y-%m-%d %H:%M"))
        return appointment_time > mktime(localtime())
    except ValueError:
        return False

def view_personal_info():
    try:
        with open("patients.txt", "r") as file:
            patient_id = input("Enter your Patient ID: ")
            found = False
            for line in file:
                if line.startswith(patient_id):
                    print("\n--- Personal Information ---")
                    print(line.strip())
                    found = True
                    break
            if not found:
                print("Patient ID not found.")
    except FileNotFoundError:
        print("Patient records file not found.")

def get_doctors_list(file_path):
    doctors = {}
    try:
        with open(file_path) as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4 and data[2].strip().lower() == "doctor":
                    doctors[data[1].strip()] = data[0].strip()  # Name as key, ID as value
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return doctors

def book_appointment():
    users_file = "Users.txt"
    appointments_file = "appointments.txt"

    doctors = get_doctors_list(users_file)
    if not doctors:
        print("No doctors available to book an appointment.")
        return

    try:
        with open(appointments_file, "a") as file:
            patient_id = input("Enter your Patient ID: ")

            doctor = input("Enter the doctor's name: ")
            while doctor not in doctors:
                print("Invalid doctor name. Available doctors:")
                for name in doctors.keys():
                    print(f"- {name}")
                doctor = input("Enter the doctor's name: ")

            date = input("Enter the appointment date (YYYY-MM-DD): ")
            while not validate_date(date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                date = input("Enter the appointment date (YYYY-MM-DD): ")

            time = input("Enter the appointment time (HH:MM): ")
            while not validate_time(time):
                print("Invalid time format. Please use HH:MM.")
                time = input("Enter the appointment time (HH:MM): ")

            while not is_future_appointment(date, time):
                print("The appointment date and time must be in the future.")
                date = input("Enter the appointment date (YYYY-MM-DD): ")
                while not validate_date(date):
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    date = input("Enter the appointment date (YYYY-MM-DD): ")

                time = input("Enter the appointment time (HH:MM): ")
                while not validate_time(time):
                    print("Invalid time format. Please use HH:MM.")
                    time = input("Enter the appointment time (HH:MM): ")

            file.write(f"{patient_id},{doctor},{date},{time}\n")
            print("Appointment booked successfully.")

    except Exception as e:
        print(f"Error booking appointment: {e}")

def view_appointments():
    try:
        with open("appointments.txt", "r") as file:
            patient_id = input("Enter your Patient ID: ")
            print("\n--- Your Appointments ---")
            found = False
            for line in file:
                if line.startswith(patient_id):
                    print(line.strip())
                    found = True
            if not found:
                print("No appointments found for the given Patient ID.")
    except FileNotFoundError:
        print("Appointments file not found.")

def update_personal_information():
    try:
        patient_id = input("Enter your Patient ID: ")
        found = False
        lines = []
        with open("patients.txt", "r") as file:
            for line in file:
                if line.startswith(patient_id):
                    found = True
                    current_info = line.strip().split(",")
                    print("Current Information:")
                    print(f"Name: {current_info[1]}\nContact: {current_info[4]}\nAddress: {current_info[5]}")

                    # Prompt for each field to update or keep the same
                    name = input(f"Name (current: {current_info[1]}): Keep same? (y/n): ")
                    if name.lower() == "n":
                        current_info[1] = input("Enter new Name: ")

                    contact = input(f"Contact (current: {current_info[4]}): Keep same? (y/n): ")
                    if contact.lower() == "n":
                        current_info[4] = input("Enter new Contact: ")

                    address = input(f"Address (current: {current_info[5]}): Keep same? (y/n): ")
                    if address.lower() == "n":
                        current_info[5] = input("Enter new Address: ")

                    # Rebuild the updated line
                    lines.append(",".join(current_info) + "\n")
                else:
                    lines.append(line)

        if not found:
            print("Patient ID not found.")
        else:
            with open("patients.txt", "w") as file:
                file.writelines(lines)
                print("Information updated successfully.")
    except FileNotFoundError:
        print("Patient records file not found.")

def give_feedback():
    try:
        with open("feedback.txt", "a") as file:
            patient_id = input("Enter your Patient ID: ")
            feedback = input("Enter your feedback: ")
            file.write(f"{patient_id},{feedback}\n")
            print("Feedback submitted successfully.")
    except Exception as e:
        print(f"Error submitting feedback: {e}")

def initialize_files():
    required_files = ["patients.txt", "appointments.txt", "feedback.txt"]
    for file in required_files:
        try:
            with open(file, "r") as f:
                pass
        except FileNotFoundError:
            with open(file, "w") as f:
                pass

"""......END.............................Patient's Code......................................................"""

# Main Menu
if __name__ == "__main__":
    while True:
        try:
            choice = int(input(f"""Welcome to Hospital Management System, Choose your Role to Login \n 
            1. Administrator\n
            2. Doctor\n
            3. Nurse\n
            4. Receptionist\n
            5. Patient\n"""))



            if choice == 1:
                user_id = input("Please give your User id to Login") #A001
                found = validate_login(user_id)
                if found == True:
                    Display_Administrator_Menu()
                else:
                    print("Invalid User id")
            elif choice == 2:
                doctor_login()

            elif choice == 3:
                user_id = input("Please give your User id to Login")  # A001
                found = validate_login(user_id)
                if found == True:
                    Nurse_menu()
                else:
                    print("Invalid User id")


            elif choice == 4:
                user_id = input("Please give your User id to Login")  # A001
                found = validate_login(user_id)
                if found:
                    Receptionist_Menu()
                else:
                    print("Invalid User id")

            elif choice == 5:

                user_id = input("Please give your User id to Login")  #P001, #P002, #P003, #P004, #P005
                found = validate_atient_login(user_id)
                if found:
                    patient_menu()
                else:
                    print("Invalid User id")

            else:
                print("Invalid choice! Please try again")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number")