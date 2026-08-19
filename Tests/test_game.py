# Import the different scripts from game.py
from src.game import Game, Status

''' Game Creation and Default Value Tests:
    * Ensure that both partial (Backlog) and fully populated Game Object Instances can be created
    * Check that Default parameters are set correctly in Game Object Constructor  
'''

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

print("backlog_test Instance Tests Passed") # Print if all above asserts are correct and don't print errors

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

print("full_test Instance Tests Passed") # Print if all above asserts are correct and don't print errors

''' Game Object Behavior Tests:
    * Test set_rating() using full_test and backlog_test to check both removing rating and giving a rating
    * Test set_hours_played() using backlog_test
    * Test add_hours_played() using full_test
    * Test set_platform() using backlog_test
    * Test set_completion() using backlog_test and full_test
'''

# Perform methods on backlog_test
backlog_test.set_rating(3.0)
backlog_test.set_hours_played(10.12)
backlog_test.set_platform("Xbox")
backlog_test.set_completion(Status.CURRENTLY_PLAYING)

# Test if the values of backlog_test are correct
assert backlog_test.hours_played == 10.12, "set_hours_played() Error"
assert  backlog_test.platform == "Xbox", "set_platform() Error"
assert backlog_test.rating == 3.0, "set_rating() Error"
assert backlog_test.completion == Status.CURRENTLY_PLAYING, "set_completion() Error"

print("backlog_test Method Tests Passed") # Print if above assertions are correct/All methods ran as intended

# Perform methods on full_test
full_test.set_rating(None) # Remove Rating
full_test.add_hours_played(.36)
full_test.set_completion(Status.ABANDONED)

# Test if the values of full_test are correct
assert full_test.hours_played == 54, "add_hours_played() Error"
assert full_test.rating is None, "set_rating Error"
assert full_test.completion == Status.ABANDONED, "set_completion() Error"

print("full_test Method Tests Passed") # Print if above assertions are correct/All methods ran as intended
