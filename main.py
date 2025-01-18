import os
from game.player import Player
from game.board import Board


def main():
    peter = Player(name="Peter", money=16, properties=[], currentPosition=0)
    billy = Player(name="Billy", money=16, properties=[], currentPosition=0)
    charlotte = Player(name="Charlotte", money=16, properties=[], currentPosition=0)
    sweedal = Player(name="Sweedal", money=16, properties=[], currentPosition=0)

    boardFile = os.path.join("data", "board.json")
    board = Board.fromJsonFile(boardFile)


if __name__ == "__main__":
    main()
