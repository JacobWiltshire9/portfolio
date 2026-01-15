train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Make a function to convert fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Test function with 100 degrees fahrenheit
f_100_in_celsius = f_to_c (100)

# Write a function to convert celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp) * (9/5) + 32
  return f_temp

# Test function with 0 degrees celsius
c0_in_fahrenheit = c_to_f(0)

# Write function to set up equation for get_force
def get_force (mass, acceleration):
  return mass * acceleration

# Test get_force and print it
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies", train_force, "Newtons of force.\n")

# Write function get_energy 
def get_energy(mass, c = 3*10**8):
  return (mass) * (c ** 2)

# Test get_energy and print it
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.\n")

# Write get_work function
def get_work(mass, acceleration, distance):
  return (mass * acceleration) * (distance)

# Test get_work and print it out
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")

# AI Review - Your code correctly implements the required temperature conversion functions f_to_c and c_to_f,
# and includes the force, energy, and work calculations as described in the tasks.
# The project fulfills the core goals by defining the conversion and
# physics-related functions and validating them with test calls.
# The code uses descriptive function names and follows a straightforward structure that makes the flow easy to follow.
# Some minor formatting tweaks could improve readability, such as consistent spacing around operators and in-line comments for sections.
# Functions are simple and efficient for the task scale; calculations are done with direct arithmetic.
# Consider a small refactor to reduce repetitive code and improve input validation in real-world usage, but it’s not necessary for this exercise.