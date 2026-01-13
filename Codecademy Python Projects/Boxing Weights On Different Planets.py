# Boxing Weights On Different Planets
print("I have information for the following planets:\n")

# Planets in order excludng Earth
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
# User enters how much they weigh
weight = input("Enter your weight: ")

# Weight is converted to float so it can be calculated
weight = float(weight)

# User inputs which planet they would prefer to fight on and have their weight converted
planet = input("Select the number of the planet you woud like to fight on: ")



# If statements to calculate his weight on the chosen planet and declare what planet will be printed

if planet == "1":
  weight = weight * .91
  planet = "Venus"
elif planet == "2":
  weight = weight * .38
  planet = "Mars"
elif planet == "3":
  weight = weight * 2.34
  planet = "Jupiter"
elif planet == "4":
  weight = weight * 1.06
  planet = "Saturn"
elif planet == "5":
  weight = weight * .92
  planet = "Uranus"
elif planet == "6":
  weight = weight * 1.19
  planet = "Neptune"

# This round weight to two decimal points
weight = round(weight,1)

# The statement will convert the int planet and the float weight to strings and print the given information
print("Your weight on " + str(planet) + " is: " + str(weight))

# AI Review: The code correctly calculates the weight on different planets based on user input and prints the result.
# It uses clear variable names and includes comments for better understanding.
# The use of if-elif statements is appropriate for this scenario. Overall, the code is well-structured and functional.
