# Developed by user "Http-404" for use in a NIMSES raffle on 06/11/19.

from random import shuffle, randint

# Users who have entered the raffle:
# [<USER ID>, <NUMBER OF TICKETS>].
users = [
    ['Scardy',          5],
    ['Ben',             10],
    ['👌👌',            250],
    ['nagol929',        25],
    ['abomination.',    1],
    ['micahmoo5e',      1],
    ['mudi',            11],
    ['liberatedhat',    10],
    ['lizzie',          1],
    ['Marshall Stward', 4],
    ['stankydanky',     40],
    ['Mark',            6],
    ['alexander6061',   11],
    ['dj_playback',     20],
    ['denosaurus813',   1],
    ['Duane Hickman',   21],
    ['Felipe Borges',   1],
    ['Madalyn Rose',    5],
    ['grantgamefreak',  10],
    ['stef',            1],
    ['jaaavi',          3],
    ['hunter',          6]]

# Sum of all tickets for probability-of-success calculation.
total_entries = sum(row[1] for row in users)

# List of all tickets to be populated by userID.
raffle = []

user_index = 0
# Iterate through all participants.
for user_data in users:
    ticket_index = 0
    # Append tickets to RAFFLE until all tickets are accounted for.
    while ticket_index < users[user_index][1]:
        # Append user's ticket to current RAFFLE list.
        raffle.append(users[user_index][0])
        ticket_index += 1
    # Append (rounded) probability-of-success to user data.
    users[user_index].append(round((users[user_index][1] / total_entries) * 100, 4))
    user_index += 1

# Shuffle all RAFFLE entries to allow for random selection.
shuffle(raffle)

# Build string of user probabilities.
probability_output = ''
for user_data in users:
    probability_output += ' "' + user_data[0] + '" had a ' + str(user_data[2]) + '% chance with ' + str(user_data[1])\
                          + ' ticket(s)...'
print(probability_output)

# Generate a random integer value for index selection.
print('"' + raffle[randint(0, total_entries)] + '" has won the raffle!')
