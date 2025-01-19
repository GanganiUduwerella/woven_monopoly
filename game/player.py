class Player(object):
    """
    Represents a player in the game with attributes for their name, 
    current amount of money, and current position on the board.
    """

    def __init__(self, name, money, currentPosition=0):
        """
        Initializes a Player instance.

        Args:
            name (str): The name of the player.
            money (int): The initial amount of money the player has.
            currentPosition (int): The starting position of the player on the board (default is 0).
        """
        self.name = name
        self.money = money
        self.currentPosition = currentPosition

    def moveTo(self, newPosition):
        """
        Moves the player to a new position on the board.
        If the new position causes the player to pass 'Go', 
        they receive $1.

        Args:
            newPosition (int): The new position to move the player to.
        """

        previousPosition = self.currentPosition
        self.currentPosition = newPosition
        
        # If the player passes 'Go' (new position is less than the previous position),
        # they collect $1
        if self.currentPosition < previousPosition:
            self.money += 1
