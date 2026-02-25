# Jacob Wiltshire
# 02/23/2026

# Create a list of paintings
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Create a list with dates
dates = [1939, 1933, 1946, 1940]

# Zip the two lists together
paintings = list(zip(paintings, dates))

# Add last minute painting entries
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

# Find the length of the list
paintings_length = len(paintings)
print(f"\nThere are {paintings_length} in total.\n")

# Give each painting the audio tour number
audio_tour_number = list(range(1, paintings_length + 1))
print(f"Audio Tour Numbers: {audio_tour_number}\n")

# Zip the audio tour numbers with the paintings and save to a master list
master_list = list(zip(audio_tour_number,paintings))
print(f"Here is master list: {master_list}")

# AI Reiview - Your code follows the project goal of creating a master list of Frida Kahlo paintings with dates and an audio tour ID. It runs without syntax errors and completes Tasks 1–7, building a list of paintings, dates, zipping them, appending new entries, calculating length, generating IDs, and producing a master list.
# Good use of descriptive variable names and straightforward flow. The code is easy to follow and mirrors the task steps.
# Code uses list(zip(...)) correctly and avoids unnecessary complexity. Printing intermediate results helps verification.
