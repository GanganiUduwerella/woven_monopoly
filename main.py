import os
from game.player import Player
from game.board import Board
from game.game import Game


def main():
    peter = Player(name="Peter", money=16, properties=[], currentPosition=0)
    billy = Player(name="Billy", money=16, properties=[], currentPosition=0)
    charlotte = Player(name="Charlotte", money=16, properties=[], currentPosition=0)
    sweedal = Player(name="Sweedal", money=16, properties=[], currentPosition=0)

    boardFile = os.path.join("data", "board.json")
    board = Board.fromJsonFile(boardFile)

    monopolyGame = Game(board=board, playerList = [peter, billy, charlotte, sweedal])

    print(f"Billy is at {billy.currentPosition} with ${billy.money}")
    monopolyGame.movePlayer(playerIndex=1, spacesToMove=2)
    print(f"Billy is now at {billy.currentPosition} with ${billy.money}")
    print(f"Game is over: {monopolyGame.gameIsOver()}")


if __name__ == "__main__":
    main()
