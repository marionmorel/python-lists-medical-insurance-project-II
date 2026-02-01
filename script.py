names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

# Task 1
names.append("Priscilla")
insurance_costs.append(8320.0)

# Task 2
medical_records = list(zip(insurance_costs, names))

# Task 3
print(medical_records)

# Task 4
num_medical_records = len(medical_records)

# Task 5
print("There are " + str(num_medical_records) + " medical records.")

# Task 6
first_medical_record = medical_records[0]

# Task 7
print("Here is the first medical record: " + str(first_medical_record))

# Task 8
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))