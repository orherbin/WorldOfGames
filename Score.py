# Function for updating the user's score file according to his wins.
def add_score(difficulty):

    # Opening the scores file, and saving the current score as a variable.
    score_file = open("Scores.txt", 'w+')
    current_score = score_file.read()

    # Adding to the current score the points earned from wining the games.
    points_of_winning = (difficulty * 3) + 5
    current_score += points_of_winning
    score_file.write(current_score)
    score_file.close()