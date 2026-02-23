# Jacob Wiltshire
# 02/23/2026

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Initialize total cost variable
total_cost = 0

# Add up all insurance cost
for i in actual_insurance_costs:
  total_cost += i

# Find the average cost
average_cost = total_cost / len(actual_insurance_costs)

# Print the average costs
print(f"Average Insurance Cost: ${average_cost:.2f}\n")

# Iterate through the list and find whether their insurance is above, below, or equal to the average cost
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  insurance_difference = abs(average_cost - insurance_cost)
  print(f"The insurance cost for {name} is ${insurance_cost:.2f}.")
  if insurance_cost > average_cost:
    print(f"The insurance cost for {name} is ${insurance_difference:.2f} above average.\n")
  elif insurance_cost < average_cost:
    print(f"The insurance cost for {name} is ${insurance_difference:.2f} below average.\n")
  else:
    print(f"The insurance cost for {name} is ${insurance_difference:.2f} equal to the average.\n")

# Create a new list that rounds up the estimated insurance cost
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

# Print out the updated estimated insurance costs
print(f"Here are the updated estimated insurance costs: {updated_estimated_costs}")

# AI Review - Your code implements the core tasks: computing the average actual cost, printing per-person costs, comparing to average, and updating estimated costs by a 10% increase. It runs without syntax errors and completes the majority of the project tasks.
# The project goals are clearly reflected in the outputs and the final updated costs align with the task description. Minor edge-case handling (e.g., division by zero if lists were empty) could be added for robustness.
# Variable names are meaningful (names, estimated_insurance_costs, actual_insurance_costs, total_cost, average_cost).
# Code formatting is mostly consistent; minor improvements could enhance readability (consistent indentation, consistent comments for each step).
# Commentary explains steps but could reiterate intent for future readers. Add a brief summary at the top outlining the pipeline.
# The loop to accumulate total_cost is straightforward and efficient for small lists.
# Consider computing average_cost with a single-pass approach or using built-ins (sum, len) as you did; your approach is already concise. For larger datasets, ensure lists are the same length before indexing to avoid IndexError.
# Optional enhancement: guard against empty lists to avoid division by zero and add minimal error handling for unexpected data types.