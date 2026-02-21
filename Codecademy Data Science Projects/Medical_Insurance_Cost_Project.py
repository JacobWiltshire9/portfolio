# Jacob Wiltshire
# 02/20/2026

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Using append, add Priscilla and her insurance costs
names.append('Priscilla')
insurance_costs.append(8320.0)

# Using zip, combine the two list
medical_records = list(zip(insurance_costs, names))

# Print out medical records
print(f"{medical_records}\n")

# Find out how many medical
num_medical_records = len(medical_records)

# Print out the amount ofd medical records
print(f"There are {num_medical_records} medical records.\n")

# Put the first medical record in a variable
first_medical_record = medical_records[0]

# Print the first medical record
print(f"Here is the first medical record: {first_medical_record}\n")

# Sort the list so the people with the lowest cost are first
medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}\n")

# Store the three cheapest costs in a variable
cheapest_three = medical_records[:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}\n")

# Store the three most expensive costs in a variable
priciest_three = medical_records[-3:]
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}\n")

# Store the amount of times paul comes up in names
occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.\n")

# AI Review -  Your code adds a new person Priscilla with her cost and sets up the medical_records pairing via zip, completing Tasks 1 and 2.
# The script prints and stores data as required (medical_records, num_medical_records, first_medical_record).
# Variables have meaningful names and the flow follows the task order, making the logic easy to follow.
# Some typos and inconsistent comments reduce readability (e.g., 'put the first' and 'cheapeast'). Improve spelling and add brief comments for key steps.
# Code runs through the tasks in a straightforward way; using list.sort() on tuples works to sort by cost since cost is first in each pair.
# Consider representing records as named tuples or dataclasses for readability and to avoid relying on index order when accessing fields. Also ensure the program handles potential edge cases (e.g., non-numeric costs) in future tasks.