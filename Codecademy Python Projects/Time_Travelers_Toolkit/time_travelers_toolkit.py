# Import all that are needed
from datetime import datetime as dt
from decimal import Decimal
import random
from custom_module import generate_time_travel_message

# Print the current time
print(f"The current date and time is: {dt.now(): %B %d %Y}\n")

# Set current year and desired time trvael year
current_year = dt.now().year
time_travel_year = random.randint(current_year, 5977)

# Initialize the base cost
base_cost = Decimal('500.00')

# Find the year difference, use abs to return a positive number
year_difference = abs(current_year - time_travel_year)

# Calculate the total cost of the trip, adding 11% to each year
total_cost = Decimal(year_difference) * Decimal('.11') + (base_cost)

# Create a list of travel destinations
destinations = ['Paris, France', 'Rome, Italy', 'Tokyo, Japan', 'New York City, USA', 'Dubai, UAE', 'London, UK', 'Bali, Indonesia', 'Machu Picchu, Peru', 'Okinawa, Japan', 'Puerto Penasco, Mexico', 'Maui, Hawaii']

# Pick a random destination from the list of destinations
final_destination = random.choice(destinations)

# Use the function imported from custom_module to print out the final message
print(generate_time_travel_message(time_travel_year, final_destination, total_cost))

# AI Reveiew: Your code implements a basic time travel message generator by using a custom module and randomness to choose year and destination.
# It aligns with the project goal of generating a formatted message about time travel and ensures a numeric cost is included.
# The script captures current date/time conceptually and prints a formatted message, satisfying the idea of producing a time-travel experience summary.
# Code uses descriptive function name generate_time_travel_message and clear variable names, aiding readability.
# Some formatting and spacing inconsistencies exist (e.g., missing spaces after operators, trailing spaces). Consider consistent indentation and PEP8-style formatting.
# The code efficiently uses Decimal for cost and random for variety; imports are direct and straightforward.
# Time Travelers Toolkit project goal is met effectively with this implementation.
# The function generates a formatted message about time travel, including year, destination, and cost.