import os
import random
from game.player import Player
from game.board import Board
from game.game import Game


def main():
    peter = Player(name="Peter", money=16, currentPosition=0)
    billy = Player(name="Billy", money=16, currentPosition=0)
    charlotte = Player(name="Charlotte", money=16, currentPosition=0)
    sweedal = Player(name="Sweedal", money=16, currentPosition=0)
    playerList = [peter, billy, charlotte, sweedal]

    boardFile = os.path.join("data", "board.json")
    board = Board.fromJsonFile(boardFile)

    monopolyGame = Game(board=board, playerList = playerList)

    print("----------------")
    print("Simulating game")
    turn = 0
    while not monopolyGame.gameIsOver():
        playerIndex = turn % len(monopolyGame.playerList)
        player = monopolyGame.playerList[playerIndex]
        print("----------------")
        print(f"Player {player.name} is at {player.currentPosition} with ${player.money}.")

        diceRoll = random.randint(1, 6)
        print(f"Dice roll: {diceRoll}")

        monopolyGame.movePlayer(playerIndex=playerIndex, spacesToMove=diceRoll)
        print(f"Player {player.name} is now at {player.currentPosition} with ${player.money}.")

        turn += 1

    print("----------------")
    print(f"Game is over: {monopolyGame.gameIsOver()}")
    print("----------------\n")
    monopolyGame.printResult()

if __name__ == "__main__":
    main()
