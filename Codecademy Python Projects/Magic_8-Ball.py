# Import the random function for the magic 8-ball response
import random

# Declare the user's name
name = input("Enter your name: ")

# User asks the magic 8-ball a question
question = input("Enter a 'yes' or 'no' question you'd like to ask the magic 8-ball:  ")

# This is where the answers of the magic 8-ball will be stored
answer = ""

# Variable to store random number
random_number = random.randint(1,11)

# Using the random number the If & Elif statements will use that number for the magic 8-ball response
#If a number that is not 1-11 is input, the 8-ball will reply with an error
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Withut a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Signs point to yes"
elif random_number == 11:
  answer = "Absolutely"
else:
  answer = "ERROR"

#If statement that makes sure the user entered a question, if not the user will be prompted with a message. If question is entered, the program will print the user's name (if entered), the question, and the magic 8-ball's answer.
if not question:
    print("You need to ask a question to get an answer!")
elif not name:
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)    

# AI Review - Your code aims to implement the Magic 8-Ball project by asking for a name and a yes/no question
# and returning a random fortune. It largely follows the task structure and runs without syntax errors.
# The program outputs the required format for name/question and the Magic 8-Ball's answer, matching the assignment expectations.
# Code is mostly readable with straightforward control flow and descriptive variable names.
# Some typos in the fortunes and inconsistent strings could confuse users; also minor indentation and spacing could be standardized for readability.
# Uses a single if/elif/else chain to map random_number to an answer, which is fine for 9+ options in a small app.
