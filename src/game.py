from enum import Enum
# Status Enum Class (will be used by completion in Game class)
class Status (Enum):
    BACKLOG = 1
    CURRENTLY_PLAYING = 2
    COMPLETED = 3
    ABANDONED = 4

class Game:
    '''
    Game Class/Object Design:
        Game Data:
            * Game Name
            * Year_Released
            * Game_Genre

        Playthrough Data:
            * Hours_Played
            * Platform this log is being played on (Ex: Computer, Xbox, PlayStation, etc.)
            * Rating (Out of 5 stars like letterboxd)
            * Completion (enum status for now, could change later)
                * Status (Not Played Yet (Backlog), Currently Playing, Completed, Abandoned)
                * Level for games like Fortnite or COD or Marvel Rivals
                * % Trophies
            * Replayed: Different Entry
        Behavior:
            * set_rating()
            * set_hours_played()
            * add_hours_played()
            * set_platform()
            * set_completion()
    '''
    # Constructor to initialize all attributes (Uses default values to account for partial entries)
    def __init__(self, name, year_released, genre, hours_played = 0, platform = None, rating = None, completion = Status.BACKLOG):
        self.name = name
        self.year_released = year_released
        self.genre = genre
        self.hours_played = hours_played
        self.platform = platform
        self.rating = rating
        self.completion = completion

    ''' Behaviors '''

    # Set Rating out of 5 stars (Include half stars but reject any other decimals)
    def set_rating(self, rating):
        self.rating = rating

    # Set the hours you played
    def set_hours_played(self, hours_played):
        self.hours_played = hours_played

    # Add hours played to current log
    def add_hours_played(self, added_hours):
        self.hours_played += added_hours

    # Set the platform tthe entry is played on (Used mainly to change backlog to current)
    def set_platform(self, platform):
        self.platform = platform

    # Set the Completion
    def set_completion(self, completion):
        self.completion = completion


