letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combine the two list so they have a key and value
letter_to_points = {i: value for i, value in zip(letters, points)}

# Add a key for blank tiles and a value of 0 to it
letter_to_points[" "] = 0
print(f"{letter_to_points}\n")

# Define a function to determine how many points a word is worth
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter,0)
  return point_total

# Create brownie_points variable
# brownie_points = score_word('BROWNIE')
# print(f"Brownie is worth {brownie_points} points!")

# Create dictionary with players words
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# Create an empty dictionary for player_to_points
player_to_points = {}

# Define a function to update point totals
def updated_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

# Update point totals
updated_point_totals()

# Define a function to add a word a player has used
def play_word(player, word):
  if player not in player_to_words:
    print(f"The player '{player}' is not in the game\n")
    return
  player_to_words[player].append(word)
  updated_point_totals()

# Test function
play_word('Jacob', 'ZOOM')
play_word('player1', 'PYTHON')

# Print out the added words and the updated scoreboard
print(f"{player_to_words}\n")
print(f"{player_to_points}\n")

# AI Review - Your Scrabble project creates a working point-tracking system using dictionaries and functions to compute word scores.
# It maps letters to points, handles blank tiles, and computes total scores for players.
# The code demonstrates the intended tasks by defining letter_to_points, score_word, and player_to_words structures, plus functions to update totals and add words.
# Functions are named clearly and the flow is easy to follow. The use of upper() ensures consistency when scoring letters.
# The code recalculates totals after every added word, which is fine for small datasets, but could be optimized by only updating affected player totals.