from game.player import Player
from game.board import Board
from game.game import Game
from util import selectFile


def main():
    """
    The main function initializes players, sets up the board, 
    and starts the Monopoly game simulation based on rolls from a JSON file.
    """
    # Create player instances with initial money and starting position
    peter = Player(name="Peter", money=16, currentPosition=0)
    billy = Player(name="Billy", money=16, currentPosition=0)
    charlotte = Player(name="Charlotte", money=16, currentPosition=0)
    sweedal = Player(name="Sweedal", money=16, currentPosition=0)
    playerList = [peter, billy, charlotte, sweedal]

    # Prompt the user to select the board configuration file
    boardFile = selectFile("board.json")
    # Load the board configuration from the selected JSON file
    board = Board.fromJsonFile(boardFile)

    # Create a Game instance with the initialized board and players
    monopolyGame = Game(board=board, playerList=playerList)

    # Prompt the user to select the rolls file containing dice rolls for the simulation
    rollsFile = selectFile("rolls_*.json")
    # Play the game using the dice rolls from the selected file
    monopolyGame.playFromJsonFile(rollsFile)


if __name__ == "__main__":
    # Entry point of the program
    main()
