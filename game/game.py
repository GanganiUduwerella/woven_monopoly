from game.board import Property

class Game(object):
    def __init__(self, board, playerList):
        self.board = board
        self.playerList = playerList
        self.bankruptPlayer = None
        for player in playerList:
            currentPosition = self.board.spaceList[player.currentPosition]
            currentPosition.occupants.append(player)
    
    def movePlayer(self, playerIndex, spacesToMove):
        player = self.playerList[playerIndex]
        boardSize = len(self.board.spaceList)
        newPosition = (player.currentPosition + spacesToMove) % boardSize
        landedSpace = self.board.spaceList[newPosition]
        
        currentSpace = self.board.spaceList[player.currentPosition]
        currentSpace.occupants.remove(player)
        player.moveTo(newPosition)

        if isinstance(landedSpace, Property) and landedSpace.owner is None:
            self._buyProperty(player=player, propertySpace=landedSpace)
        elif isinstance(landedSpace, Property) and landedSpace.owner is not None:
            self._rentProperty(player=player, propertySpace=landedSpace)
        
        if self.bankruptPlayer is None:
            landedSpace.occupants.append(player)
    
    def gameIsOver(self):
        return self.bankruptPlayer is not None
    
    def getWinners(self):
        max_money = max(player.money for player in self.playerList)
        winners = [player for player in self.playerList if player.money == max_money]
        return winners
    
    def printResult(self):
        if not self.gameIsOver():
            print("Game is not yet over.")

        winners = self.getWinners()
        if len(winners) == 1:
            print(f"Winner of the game is {winners[0].name}")
        else:
            winnerNames = [w.name for w in winners]
            print(f"Winners of the game are {winnerNames}")
        
        for player in self.playerList:
            if player.money < 0:
                print(f"Player {player.name} is bankrupt.")
            else:
                print(f"Player {player.name} ends up with ${player.money}.")
    
        for player in self.playerList:
            spacePosition = player.currentPosition
            spaceName = self.board.spaceList[spacePosition].spaceName
            print(f"Player {player.name} finish on space {spacePosition} ({spaceName}).")

    def _buyProperty(self, player, propertySpace):
        player.money -= propertySpace.spacePrice
        if player.money < 0:
            self.bankruptPlayer = player
        else:
            propertySpace.owner = player

    def _rentProperty(self, player, propertySpace):
        rent = propertySpace.spacePrice
        if self.board.ownerSameForColorOf(propertySpace):
            rent *= 2
        player.money -= rent
        propertySpace.owner.money += rent
        if player.money < 0:
            self.bankruptPlayer = player
