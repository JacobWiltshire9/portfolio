# Jacob Wiltshire
# 03/02/2026

# Create empty dictionary for medical costs
medical_costs = {}

# Add some costs to the dictionary
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

# Using one line of code add more costs to the dictionary
medical_costs.update({'Connie':8886.0, 'Isaac':16444.0, 'Valentina':6420.0})

# Print medical_costs to see the output
print("Original Dictionary:")
print(f"{medical_costs}\n")

# Update Vinay's costs
medical_costs['Vinay'] = 3325.0 

# Print the update dictionary
print("Updated Dictionary:")
print(f"{medical_costs}\n")

# Create total cost variable
total_cost = 0

# Iterate through the dictionary and add the total costs
for i in medical_costs.values():
  total_cost += i

# Calculate the average costs
average_cost = total_cost / len(medical_costs)

# Print the average costs
print(f"Average Insurance Cost: ${average_cost:.2f}\n")

# Create two lists called names and ages
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

# Zip the two lists so the pairs are names : ages
zipped_ages = list(zip(names,ages))

# Create dictionary to turn the zipped list into a dictionary
names_to_ages = {key:value for key, value in zipped_ages}
print(f"{names_to_ages}\n")

# Store Marina's age into a variable
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}\n")

# Create dictionary to hold medical records
medical_records = {}
medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

# Add everyone elses information to the dictionary
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

# Print the medical records
print(f"{medical_records}\n")

# Print Connie's insurance cost
print(f"Connie's insurance costs is {medical_records['Connie']['Insurance_cost']} dollars.\n")

# Vinay moved away and we no longer need his record
medical_records.pop("Vinay")

#Use a for loop to iterate through the dictionary to print each person medical record
for person, record in medical_records.items():
  print(f"{person} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}\n")

  # AI Review - Your code implements the core tasks: creates and updates a medical_costs dictionary, builds a medical_records database, and prints/updates data as required. It demonstrates dictionary use and basic iteration correctly.
  # Variables and steps are easy to follow; the code is straightforward and uses descriptive keys. Minor spacing could improve readability.
  # Some comments explain what each block does, which helps readability. Ensure consistent indentation and avoid mixing tabs/spaces.
  # Simple dictionary usage and a single update are efficient for this dataset. Printing whole dictionaries is fine for small datasets.
  # Average calculation correctly uses length of dictionary and sums values; this scales with dictionary size. Consider computing total_cost with sum() for readability.