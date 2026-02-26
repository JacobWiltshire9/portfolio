# Jacob Wiltshire
# 02/26/2026

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Change all hashtags to dollar signs
updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)

# Create variable to track number of records
num_records = 0

# Iterate through string to count number of records
for i in updated_medical_data:
  if i == '$':
    num_records += 1

# Print number of records
print(f"\nThere are {num_records} medical records in the data.\n")

# Split the data into a list seperating by ; and print it to the console
medical_data_split = updated_medical_data.split(';')
print(f"{medical_data_split}\n")

# Define an empyt list
medical_records = []

# Iterate through medical data split and split by commas and append to the new list
for i in medical_data_split:
  medical_records.append(i.split(','))
print(f"{medical_records}\n")

# Create another list to clean up data
medical_records_clean = []

# Iterate through medical records
for record in medical_records:
  records_clean = []
  for i in record:
    records_clean.append(i.strip())
  # Append the clean records to our clean medical record list
  medical_records_clean.append(records_clean)

# Print the clean records to the console
print(f"{medical_records_clean}\n")

# Print the name of the 10 people in the records and change all characters to uppercase
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(f"{record[0]}")

# Create four empty list to store name, age, bmi, and insurance cost in
names = []
ages = []
bmis = []
insurance_costs = []

# Iterate through medical record clean and append to their corresponding list
for i in medical_records_clean:
  names.append(i[0])
  ages.append(i[1])
  bmis.append(i[2])
  insurance_costs.append(i[3])

# Print out list to make sure all items were put into the correct list
print(f"\nNames: {names}\n")
print(f"\nAges: {ages}\n")
print(f"\nBMIs: {bmis}\n")
print(f"\nInsurance Costs: {insurance_costs}\n")

# Calculate the total BMI
total_bmi = 0
for i in bmis:
  total_bmi += float(i)

# Calculate the average BMI
average_bmi = total_bmi / len(bmis)

# Print the average bmi to the console
print(f"Average BMI: {average_bmi:.2f}\n")

# Calculate the average insurance cost
insurance_costs_clean = [cost.replace('$', '') for cost in insurance_costs]
total_insurance_costs = 0
for cost in insurance_costs_clean:
  total_insurance_costs += float(cost)
average_insurance_cost = total_insurance_costs / len(insurance_costs_clean)

# Print the average insurance cost to the console
print(f"Average Insurance Cost: ${average_insurance_cost:.2f}\n")

# Output a string to print out everyones information
for i in medical_records_clean:
  print(f"{i[0]} is {i[1]} years old with a BMI of {i[2]} and an insurance cost of {i[3]}0\n")

  # AI Review - Your code attempts to fulfill the medical data cleaning workflow by replacing hashtags, counting records, splitting into records, cleaning whitespace, and organizing into lists for analysis. It prints the data at several stages, aligning with the task goals.
  # Code shows clear progression through cleaning steps, but there are minor typos and spacing issues that reduce readability.
  # The script runs through many passes; counting with count() and list comprehensions can reduce runtime and improve readability.