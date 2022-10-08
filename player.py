""" This is the player class for the Game."""

class Player:
    '''
    Class to represent a player
    ...

    Attributes
    ----------
    lives : int
        lives left for the player
    name : str
        name of the player
    score : int
        score of the player

    Methods
    -------
    update_lives(num):
        Updates the current lives of the player by the given num.
    update_score(num):
        Updates the current score of the player by the given num.
    ret_lives():
        Returns the current lives of the player for displaying.
    ret_name():
        Returns the name of the player.
    ret_score():
        Returns the current score of the player for displaying.

    '''

    def __init__(self, pname) -> None:
        """
        Constructs all the necessary attributes for the Player object.
        Sets the current score , lives of the player to 0 , 6 respectively.

        Parameters
        ----------
            name : str
                first name of the person
        """
        self.lives = 6
        self.name = pname
        self.score = 0

    def update_lives(self, num):
        '''Updates the current lives of the player by the given num'''
        self.lives += num

    def update_score(self, num):
        '''Updates the current score of the player by the given num'''
        self.score += num

    def ret_lives(self):
        '''Returns the current lives of the player for displaying'''
        return self.lives

    def ret_name(self):
        '''Returns the name of the player'''
        return self.name

    def ret_score(self):
        '''Returns the current score of the player for displaying'''
        return self.score
