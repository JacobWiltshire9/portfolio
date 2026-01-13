# Grades from last semester stored
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Set the subjects list 
subjects = ["physics", "calculus", "poetry", "history"]

# Set the grades list
grades = [98, 97, 85, 88]

# Combine both lists without using methods and assign it gradebook
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# Check the output of gradebook
print(gradebook, "\n")

# Add computer science grade to gradebook
gradebook.append(["computer science", 100])

# Add visual arts grade
gradebook.append(["visual arts", 93])

# Add 5 extra credit points to the visual arts grade
gradebook[5][1] += 5

# Remove number grade from poetry class
gradebook[2].remove(85)

# Add 'Pass' to poetry grade
gradebook[2].append("Pass")


# Create full gradebook variable to combie last semester and this semester gradebook
full_gradebook = last_semester_gradebook + gradebook

# Print completed gradebook
print(full_gradebook)

# AI Review - The code successfully creates and manages a gradebook for a student by combining last semester's grades with the current semester's grades.
# It demonstrates the use of lists to store subjects and their corresponding grades, as well as list methods to modify the gradebook (adding new subjects, updating grades, and removing grades).
# The final output combines both semesters' gradebooks into a single comprehensive list. The code is clear and functional, effectively meeting the requirements of the task.
# Some comments describe each step, but formatting consistency could be improved for readability (e.g., consistent indentation and spacing).
# Simple list operations are used directly; for small datasets this is fine and readable.
# Consider avoiding hard-coded indices by using variables or iterating when updating nested lists to reduce risk of mistakes if the structure changes.