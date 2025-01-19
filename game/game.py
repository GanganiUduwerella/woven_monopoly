import json
from game.board import Property


class Game(object):
    """
    Represents the main game logic for a board game. Manages players, the board, 
    and the sequence of play.
    """

    def __init__(self, board, playerList):
        """
        Initializes a new game instance.

        Args:
            board (Board): The game board containing spaces.
            playerList (list): A list of Player objects participating in the game.
        """
        self.board = board
        self.playerList = playerList
        self.bankruptPlayer = None

        # Place all players on their initial positions
        for player in playerList:
            currentPosition = self.board.spaceList[player.currentPosition]
            currentPosition.occupants.append(player)

    def movePlayer(self, playerIndex, spacesToMove):
        """
        Moves a player a specified number of spaces on the board.

        Args:
            playerIndex (int): The index of the player in the player list.
            spacesToMove (int): The number of spaces to move forward.
        """
        player = self.playerList[playerIndex]
        boardSize = len(self.board.spaceList)
        newPosition = (player.currentPosition + spacesToMove) % boardSize
        landedSpace = self.board.spaceList[newPosition]

        # Remove the player from the current space
        currentSpace = self.board.spaceList[player.currentPosition]
        currentSpace.occupants.remove(player)

        # Update the player's position
        player.moveTo(newPosition)

        # Handle property logic (buy or rent)
        if isinstance(landedSpace, Property) and landedSpace.owner is None:
            self._buyProperty(player=player, propertySpace=landedSpace)
        elif isinstance(landedSpace, Property) and landedSpace.owner is not None:
            self._rentProperty(player=player, propertySpace=landedSpace)

        # Add the player to the new space unless they are bankrupt
        if self.bankruptPlayer is None:
            landedSpace.occupants.append(player)

    def gameIsOver(self):
        """
        Checks if the game is over (If a player has gone bankrupt).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.bankruptPlayer is not None

    def getWinners(self):
        """
        Determines the winner(s) of the game based on the highest money balance.

        Returns:
            list: A list of Player objects with the highest money balance.
        """
        max_money = max(player.money for player in self.playerList)
        winners = [player for player in self.playerList if player.money == max_money]
        return winners

    def printResult(self):
        """
        Prints the game results, including the winner(s) and the final state of all players.
        """
        print("----------------")
        if self.gameIsOver():
            print("Game is over.")
            print("----------------\n")
            winners = self.getWinners()
            if len(winners) == 1:
                print(f"Winner of the game is {winners[0].name}.")
            else:
                winnerNames = [w.name for w in winners]
                print(f"Winners of the game are {winnerNames}.")
            print("")
        else:
            print("All given moves simulated, but the game is not yet over.")
            print("----------------\n")

        for player in self.playerList:
            if player.money < 0:
                print(f"Player {player.name} is bankrupt.")
            else:
                print(f"Player {player.name} ends up with ${player.money}.")

        print("")
        for player in self.playerList:
            spacePosition = player.currentPosition
            spaceName = self.board.spaceList[spacePosition].spaceName
            print(f"Player {player.name} finished on space {spacePosition} ({spaceName}).")

    def playFromJsonFile(self, filename):
        """
        Simulates the game using dice rolls from a JSON file.

        Args:
            filename (str): The path to the JSON file containing dice rolls.
        """
        print("----------------")
        print(f"Simulating game using moves from {filename}.")

        # Load dice rolls from the JSON file
        with open(filename, 'r') as file:
            dice_rolls = json.load(file)

        turn = 0
        while not self.gameIsOver() and turn < len(dice_rolls):
            playerIndex = turn % len(self.playerList)
            player = self.playerList[playerIndex]

            # Print player's current status
            currentSpace = self.board.spaceList[player.currentPosition]
            spaceName = currentSpace.spaceName
            print("----------------")
            print(f"Player {player.name} is at {player.currentPosition} ({spaceName}) with ${player.money}.")

            # Process the dice roll and move the player
            diceRoll = dice_rolls[turn]
            print(f"Dice roll: {diceRoll}")

            self.movePlayer(playerIndex=playerIndex, spacesToMove=diceRoll)
            print(f"Player {player.name} is now at {player.currentPosition} with ${player.money}.")

            turn += 1

        # Print the final game results
        self.printResult()

    def _buyProperty(self, player, propertySpace):
        """
        Handles the logic for a player buying a property.

        Args:
            player (Player): The player attempting to buy the property.
            propertySpace (Property): The property space being purchased.
        """
        player.money -= propertySpace.spacePrice
        if player.money < 0:
            self.bankruptPlayer = player
        else:
            propertySpace.owner = player

    def _rentProperty(self, player, propertySpace):
        """
        Handles the logic for a player paying rent on a property.

        Args:
            player (Player): The player paying the rent.
            propertySpace (Property): The property space being rented.
        """
        rent = propertySpace.spacePrice 
        # Double the rent if the owner owns all properties of the same color
        if self.board.ownerSameForColorOf(propertySpace):
            rent *= 2
        player.money -= rent
        propertySpace.owner.money += rent
        if player.money < 0:
            self.bankruptPlayer = player
