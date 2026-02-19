# Jacob Wiltshire
# 02/19/2026

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(f"{name}'s Estimated Insurance Cost: ${estimated_cost:.2f}\n")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Create names list
names = ['Maria', 'Rohan', 'Valentina']

# Create a list of the actual amount of insurance paid
insurance_costs = [4150.00, 5320.00, 35210.00]

# Combine the two list using zip
insurance_data = list(zip(names, insurance_costs))
print(f"Here is the actual insurance cost data: {insurance_data}\n")

# Create an empty list
estimated_insurance_data = []
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))
print(f"Here is the estimated insurance cost data: {estimated_insurance_data}")

# AI Review - Your code estimates insurance costs for three individuals and stores actual vs estimated costs using lists and zip, fulfilling the project’s core goals.
# The function is correctly computing estimates and returning the value, demonstrating the intended estimation logic.
# Variable and function names are descriptive and easy to follow.
# Print statements clearly show outputs; however, some long lines could benefit from formatting for readability
# Code uses simple lists and zip effectively to pair data, which is efficient for this task.
# The code could avoid printing inside the estimator for cleaner separation of concerns and rely on return values for display.