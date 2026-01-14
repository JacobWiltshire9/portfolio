# Set a list for the toppings for the pizza
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Set a list for the price of each slice
prices = [2, 6, 1, 3, 2, 7, 2]

# Count how many times '2' appears in the prices list
num_two_dollar_slices = prices.count(2)
print("There are", num_two_dollar_slices, "two dollar slices.\n")

# Find length of the toppings list and store it
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!\n")

# Make two dimensional list to combine pizza and pricing
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# Sort pizza and price in ascending order of price
pizza_and_prices.sort()

# Store first element in pizza and prices to variable 'cheapeast pizza
cheapest_pizza = pizza_and_prices[0]

#Store last element in pizza and prices to variable 'priciest pizza'
priciest_pizza = pizza_and_prices[-1]

# Remove anchovies since it was bought
pizza_and_prices.remove([7, "anchovies"])

# Add peppers to the list since anchovies is no longer available
pizza_and_prices.insert(4, [2.5, "peppers"])
print("This is our updated pizza and prices:", pizza_and_prices, "\n")

# Add list '3 cheapest' for the customers that came in to buy them
three_cheapest = pizza_and_prices[:-4]
print("The three cheapest pizzas are:", three_cheapest)

# AI Review: Compliment: The code creates the required toppings and prices lists and computes counts and lengths as per tasks.
# Suggestions: 1) Ensure you’re addressing all tasks in order (e.g., task 6 requires a fresh 2D list built from scratch with exact price-topping pairs).
# 2) Consider keeping task outputs in separate print statements to clearly show each result.
# Optional compliment: The overall flow follows the project steps and prints intermediate results.
# Suggestion: Add explicit comments for each task to improve traceability, e.g., “# Task 3: count $2 slices”.
# The code uses simple, readable variable names and straightforward list operations.
# The code uses built-in list methods effectively (sort, count, remove, insert).
# Suggestions: 1) When sorting 2D lists by the first element, explicitly key by first item for clarity (pizza_and_prices.sort(key=lambda x: x[0])). 2)
# Avoid mixing in-place modifications with prints; assign results to clearly named variables before printing to facilitate debugging.