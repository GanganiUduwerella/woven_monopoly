import os
from game.player import Player
from game.board import Board
from game.game import Game
from util import selectFile


def main():
    peter = Player(name="Peter", money=16, currentPosition=0)
    billy = Player(name="Billy", money=16, currentPosition=0)
    charlotte = Player(name="Charlotte", money=16, currentPosition=0)
    sweedal = Player(name="Sweedal", money=16, currentPosition=0)
    playerList = [peter, billy, charlotte, sweedal]

    boardFile = selectFile("board.json")
    board = Board.fromJsonFile(boardFile)

    monopolyGame = Game(board=board, playerList = playerList)

    rollsFile = selectFile("rolls_*.json")
    monopolyGame.playFromJsonFile(rollsFile)

if __name__ == "__main__":
    main()
