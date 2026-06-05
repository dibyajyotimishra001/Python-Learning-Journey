readme_content = """# Snake, Water, Gun Game

## Description
"Snake, Water, Gun" is a simple Python command-line game, closely resembling the classic "Rock, Paper, Scissors". The user plays against the computer by choosing one of the three options, and the winner is determined based on a set of predefined rules.

## Rules of the Game
* **Snake vs. Water:** Snake drinks Water -> Snake wins
* **Water vs. Gun:** Water rusts Gun -> Water wins
* **Gun vs. Snake:** Gun shoots Snake -> Gun wins
* If both the player and the computer choose the exact same item, the game results in a Draw.

## How to Play
1. Run the Python script in your terminal or command prompt.
2. The game will prompt you to enter your choice.
3. Use the following keys to make your selection:
   * `s` for Snake
   * `w` for Water
   * `g` for Gun
4. Press Enter. The computer will randomly select its choice, and the final result will be displayed.

## Error Handling
If you enter an invalid character (anything other than 's', 'w', or 'g'), the game will notify you of the invalid input and exit safely.

## Requirements
* Python 3.x installed on your system.

## How to Run
Navigate to the directory containing the script and run: