# Jacob Wiltshire
# 02/18/2026

# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
print(f"This person's insurance cost is {insurance_cost:.2f} dollars.\n")

# Age Factor
age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost:.2f} dollars.\n")

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost:.2f} dollars.\n")

# Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost:.2f} dollars.\n")

# Smoker Factor
smoker = 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change of being a smoker vs a non-smoker would be ${change_in_insurance_cost:.2f}\n")

# Children Factor
num_of_children = 0
smoker = 0
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change of having 0 kids instead of 3 would be ${change_in_insurance_cost:.2f}\n")

# AI Review - Your code implements the Insurance cost formula and demonstrates how changes to age, BMI, sex, smoker, and children affect the estimated cost, aligning with the project tasks.
# Code is readable and straightforward, with clear variable names and linear progression through tasks.
# The script follows the project tasks and computes insurance_cost and subsequent deltas; shows a solid sequence of experiments.