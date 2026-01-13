# Setting the weight any number
weight = input("Enter the weight of the package: ")
weight = float(weight)

# Ground Shipping
if weight <= 2:
  weight = (weight * 1.50) + 20.00
  weight = "%.2f" % weight
  print("Your total cost for Ground Shipping is: $", weight)
elif weight >= 2 and weight <= 6:
  weight = (weight * 3.00) + 20
  weight = "%.2f" % weight
  print("Your total cost for Ground Shipping is: $", weight)
elif weight >=6 and weight <= 10:
  weight = (weight * 4.00) + 20
  weight = "%.2f" % weight
  print("Your total cost for Ground Shipping is: $", weight)
else:
  weight = (weight * 4.75) + 20
  weight = "%.2f" % weight
  print("Your total cost for Ground Shipping is: $", weight)
  
# Ground Shipping Premium
ground_shipping = 125.00
print ("Your total shipping cost for Ground Shipping Premium is: $", ground_shipping)

# Resetting weight variable for drone shipping calculation
weight = input("Enter the weight of the package: ")
weight = float(weight)

# Drone Shipping
if weight <= 2:
  weight = (weight * 4.50)
  weight = "%.2f" % weight
  print("Your total cost for Drone Shipping is: $", weight)
elif weight >= 2 and weight <= 6:
  weight = (weight * 9.00)
  weight = "%.2f" % weight
  print("Your total cost for Drone Shipping is: $", weight)
elif weight >=6 and weight <= 10:
  weight = (weight * 12.00)
  weight = "%.2f" % weight
  print("Your total cost for Drone Shipping is: $", weight)
else:
  weight = (weight * 14.25)
  weight = "%.2f" % weight
  print("Your total cost for Drone Shipping is: $", weight)
  
# AI Review - The code effectively calculates shipping costs based on weight for three different shipping methods: ground shipping, ground shipping premium, and drone shipping.
# It uses conditional statements to determine the correct pricing tier based on weight and outputs the total cost formatted to two decimal places.
# The code is functional and meets the requirements of the task. However, there are areas for improvement:
# 1. Code Duplication: The weight input and conversion to float is repeated for drone shipping. This could be optimized by storing the weight once and reusing it.
# 2. Readability: The variable name 'weight' is reused to store the total cost, which can be confusing. Using a different variable name for the cost would enhance clarity.
# 3. Consistency: The code uses both 'weight' and 'ground_shipping' inconsistently. Standardizing variable names would improve code quality.