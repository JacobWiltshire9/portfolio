# Jacob Wiltshire
# 02/19/2026

# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.\n")
  else:
    print("Smoking is not an issue for you.\n")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(f"{name}'s Estimated Insurance Cost: ${estimated_cost:.2f}.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

# Estimate my insurance cost
jacob_insurance_cost = estimate_insurance_cost('Jacob', 22, 1, 0, 0)

# AI Review - Your code estimates insurance cost for individuals and provides smoker-related advice, aligning with the task goals and the provided formula.
# The program prints and returns the cost, and calls analyze_smoker to give guidance, which matches Task 5 to integrate analysis with the estimate.
# Function names and variable names are clear and descriptive; the code is easy to follow.
# The code computes cost with a direct formula and calls analyze_smoker, which is efficient for this task.