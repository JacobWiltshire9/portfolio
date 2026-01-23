# Create a list of gamers for those who are attending the event
gamers = []

# Define a funtion that will update the list of gamers
def add_gamer(gamer, gamers_list):
    if gamer.get("Name") and gamer.get("Availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer must have a name and availability status.")

# Set Kimberly's availability
kimberly = {'Name': 'Kimberly Warner', 'Availability': ['Monday', 'Tuesday', 'Friday']}

# Add Kimberly to the list of gamers using the function
add_gamer(kimberly, gamers)

# Add more gamers to the list
add_gamer({'Name':'Thomas Nelson','Availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'Name':'Joyce Sellers','Availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'Name':'Michelle Reyes','Availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'Name':'Stephen Adams','Availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'Name': 'Joanne Lynn', 'Availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'Name':'Latasha Bryan','Availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'Name':'Crystal Brewer','Availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'Name':'James Barnes Jr.','Availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'Name':'Michel Trujillo','Availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Create a function to calculate the nights of the week that will have the most participation
def build_daily_frequency_table():
    frequency_table = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    for gamer in gamers:
        for day in gamer['Availability']:
            if day in frequency_table:
                frequency_table[day] += 1
    return frequency_table

# Call function to save the count availability of gamers for each day of the week
count_availability = build_daily_frequency_table()
print(count_availability)

# Define a function to find the best night to host the event
def find_best_night(frequency_table):
    best_night = max(frequency_table, key=frequency_table.get)
    return best_night

# Call the function to find the best night and store it into game_night
game_night = find_best_night(count_availability)
print(f'Game night this be on {game_night}!')

# Create a function to find the gamers who can attend on the best night
def available_on_night(gamers_list, day):
    attendees = []
    for gamer in gamers_list:
        if day in gamer['Availability']:
            attendees.append(gamer['Name'])
    return attendees

# Call the function to determine the gamers who can attend on game_night
attending_game_night = available_on_night(gamers, game_night)
print(f'The following gamers can attend on {game_night}: {attending_game_night}')

# Define a string that notifys when the game can be played
form_email = """
Dear {name}, 
The Sorcery Society will be hosting a game night on {day_of_week}.
The game being played this week will be "{game}".
We hope you can make it and are very excited to have your company!

Your favorite comic book store,
Sorcery Society <3
"""
# Define a function to send emails to the attendees
def send_email(gamers_who_can_attend, day, game):
    for name in gamers_who_can_attend:
        print(form_email.format(name=name, day_of_week=day, game=game))

# Call the function to send emails to the attendees
send_email(attending_game_night, game_night, "Abruptly Goblins!")

# Get sorted unique attendance counts
sorted_counts = sorted(set(count_availability.values()), reverse=True)

# Second highest attendance number
second_highest = sorted_counts[1]

# Find the day that has that count
second_night = [
    day for day, count in count_availability.items()
    if count == second_highest
][0]

# Create a list of gamers who can attend on the second best night
attending_second_game_night = available_on_night(gamers, second_night)

# Email the gamers about the second game night
send_email(attending_second_game_night, second_night, "Abruptly Goblins!")


# AI Review - The code is well-structured and effectively accomplishes the task of organizing a game night event.
# It defines functions for adding gamers, calculating availability, finding the best night, and sending emails.
# The use of a frequency table to count availability is efficient, and the logic for determining the
# best and second-best nights is sound. The email template is clear and personalized.
# Overall, the code is clean, readable, and demonstrates good programming practices.