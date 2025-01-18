from game.board import Property

class Game(object):
    def __init__(self, board, playerList):
        self.board = board
        self.playerList = playerList
        self.bankruptPlayer = None
        goSpace = self.board.spaceList[0]
        goSpace.occupants.extend(playerList)
    
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
    
    def getWinner(self):
        max(self.playerList, key=lambda player: player.money)

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
