# Import the different scripts from game.py
from src.game import Game, Status

'''Game Creation and Default Value Tests '''

# Create Backlog Game
backlog_test = Game("Elden Ring", 2022, "RPG")

# Test if the values of backlog_test are correct
assert backlog_test.name == "Elden Ring", "Name Wrong"
assert backlog_test.year_released == 2022, "Year Release Wrong"
assert  backlog_test.genre == "RPG", "Genre Wrong"
assert backlog_test.hours_played == 0, "Hours Wrong"
assert  backlog_test.platform is None, "Platform Wrong"
assert backlog_test.rating is None, "Rating Wrong"
assert backlog_test.completion == Status.BACKLOG, "Completion Wrong"

print("Backlog Test Passed") # Print if all above asserts are correct and don't print errors

# Create Complete Game Entry
full_test = Game("Fortnite", 2022, "Battle Royale", 53.64, "Xbox", 4.5, Status.CURRENTLY_PLAYING)

# Test if the values of full_test are correct
assert full_test.name == "Fortnite", "Name Wrong"
assert full_test.year_released == 2022, "Year Release Wrong"
assert full_test.genre == "Battle Royale", "Genre Wrong"
assert full_test.hours_played == 53.64, "Hours Wrong"
assert full_test.platform == "Xbox", "Platform Wrong"
assert full_test.rating == 4.5, "Rating Wrong"
assert full_test.completion == Status.CURRENTLY_PLAYING, "Completion Wrong"

print("Full Test Passed") # Print if all above asserts are correct and don't print errors