# Jacob Wiltshire
# 02/18/2026

# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = (250 * age) - (128 * sex) + (370 * bmi) + 425 * num_of_children + (24000 * smoker) - 12500
  return f"The estimated insurance cost for {name} is ${estimated_cost:.2f}."

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost('Maria', 28, 0, 26.2, 3, 0)
print(maria_insurance_cost)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost('Omar', 35, 1, 22.2, 0, 1)
print(omar_insurance_cost)

# Estimate Jacob's insurance cost
jacob_insurance_cost = calculate_insurance_cost('Jacob', 22, 1, 21.2, 0, 0)
print(jacob_insurance_cost)

# AI Review - Your code implements calculate_insurance_cost with the required parameters and prints personalized insurance estimates for Maria, Omar, and Jacob, aligning with the project goals and avoiding syntax errors.
# Good use of a single function to encapsulate the cost calculation and returning a formatted string. The code is straightforward and easy to follow.
# Names for variables and function parameters are clear and descriptive. Consider keeping consistent string formatting in the return to ensure uniform output.
# Function call usage is correct and prints personalized results for each person. The code runs without obvious errors.
# The function returns a ready-to-print message. If you later need just the numeric value, you could add an option to return both the message and the cost.