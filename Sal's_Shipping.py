#Setting cost to a variable
cost = 0

# Setting the weight any number
weight = input("Enter the weight of the package: ")
weight = float(weight)

# Ground Shipping
if weight <= 2:
  cost = (weight * 1.50) + 20.00
  cost = "%.2f" % cost
  print("Your total cost for Ground Shipping is: $", cost)
elif weight >= 2 and weight <= 6:
  cost = (weight * 3.00) + 20
  cost = "%.2f" % cost
  print("Your total cost for Ground Shipping is: $", cost)
elif weight >=6 and weight <= 10:
  cost = (weight * 4.00) + 20
  cost = "%.2f" % cost
  print("Your total cost for Ground Shipping is: $", cost)
else:
  cost = (weight * 4.75) + 20
  cost = "%.2f" % cost
  print("Your total cost for Ground Shipping is: $", cost)
  
# Ground Shipping Premium
ground_shipping = 125.00
print ("Your total shipping cost for Ground Shipping Premium is: $", ground_shipping)

# Resetting weight variable to a float and cost variable to 0 for drone shipping calculation
weight = float(weight)
cost = 0

# Drone Shipping
if weight <= 2:
  cost = (weight * 4.50)
  cost = "%.2f" % cost
  print("Your total cost for Drone Shipping is: $", cost)
elif weight >= 2 and weight <= 6:
  cost = (weight * 9.00)
  cost = "%.2f" % cost
  print("Your total cost for Drone Shipping is: $", cost)
elif weight >=6 and weight <= 10:
  cost = (weight * 12.00)
  cost = "%.2f" % cost
  print("Your total cost for Drone Shipping is: $", cost)
else:
  cost = (weight * 14.25)
  cost = "%.2f" % cost
  print("Your total cost for Drone Shipping is: $", cost)
  
# AI Review - The code effectively calculates shipping costs based on weight for three different shipping methods: ground shipping, ground shipping premium, and drone shipping.
# It uses conditional statements to determine the correct pricing tier based on weight and outputs the total cost formatted to two decimal places.
# The code is functional and meets the requirements of the task. However, there are areas for improvement:
# 1. Code Duplication: The weight input and conversion to float is repeated for drone shipping. This could be optimized by storing the weight once and reusing it.
# 2. Readability: The variable name 'weight' is reused to store the total cost, which can be confusing. Using a different variable name for the cost would enhance clarity.
# 3. Consistency: The code uses both 'weight' and 'ground_shipping' inconsistently. Standardizing variable names would improve code quality.