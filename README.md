# woven_monopoly
This repository contains a Python implementation of the game Woven Monopoly, as presented in new_coding_test.zip

## Task Description
Below is the original task description provided for this coding test.

----

## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)

### Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?

The specifics and implementation of this code are completely up to you!

### What we are looking for:
* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code. You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.

---

## Implementation Overview and Design Decisions
This implementation was written in Python, following object-oriented principles to ensure clean, modular, and extensible code. The game logic has been implemented to adhere strictly to the given rules.
The solution includes the following key components:
1. **Player Management:** Each player is represented as an object, tracking their name, money, and position.
2. **Board Structure:** The board is loaded dynamically from a JSON file and supports various types of spaces such as "GO" and "Property."
3. **Game Logic:** Core game rules are implemented, including buying properties, paying rent, and determining winners.
4. **Deterministic Simulation:** The game uses dice rolls loaded from a JSON file, ensuring repeatable results.

---

## How to Run the Program
To execute the game simulation:
1. Ensure you have Python 3 installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/GanganiUduwerella/woven_monopoly.git
   ````
3. Navigate to the project directory:
   ```bash
   cd woven_monopoly
   ````
4. Run the program:
   ```bash
   python3 main.py
   ````

----

## How to Test the Implementation
Unit tests are provided in the `tests` folder to ensure the correctness of the implementation.
1. Navigate to the project directory.
2. Run the following command to execute all tests:
   ```bash
   python3 -m unittest discover tests
   ````
3. The test results will be displayed in the terminal, indicating any passed or failed tests.