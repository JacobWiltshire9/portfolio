# List for all hairstyles, how much they cost, and how much of each haircut was done last week
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create variable for total price of all haircuts
total_price = 0

# Find the sum of the haircuts prices
for p in prices:
  total_price += p

# Create variable to find the average price
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price:.2f}\n")

# Zip hairstyles and new prices together
new_prices = [price - 5 for price in prices]
print("New Haircut Prices: ")
for h, p in zip(hairstyles, new_prices):
  print(f"{h}: ${p}")
print()
# Figure out how much revenue was brought last week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Print the total revenue
print(f"Total revenue: ${total_revenue:.2f}\n")

# Find the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: $ {average_daily_revenue:.2f}\n")

# Advertise all haircuts that are under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# For loop to print off each haircut that is under $30
for h in range(len(cuts_under_30)):
  print(f"Haircuts under $30: {cuts_under_30[h]}")

# AI Review - Your code implements all required tasks from the project: computes average price, applies a $5 reduction, 
# calculates total and average revenue, and lists cuts under $30. 
# It runs without syntax errors and aligns with Carly's Clippers goals.
# The code clearly follows the tasks outline and outputs the expected results for each metric 
# (average price, new_prices, total revenue, average daily revenue, cuts under 30).
# Variable names are descriptive (total_price, average_price, total_revenue, average_daily_revenue).
# The code efficiently computes sums and averages using a single pass where appropriate. 
# The loop for revenue uses range(len(hairstyles)) which is fine for this dataset.