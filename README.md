# Red-Blue-Nim


Structuring of code

    1)First import Required Modules
    
    2)The primary function in the code is game. This function handles the main game logic. It simulates the game, alternating between the "human" and "computer" players, until the game is over.
   
    3)Next, the code includes a MinMax search algorithm with alpha-beta pruning to determine the best moves for the computer player. It has two separate functions, minmax_misere and minmax_standard, to handle different game versions ("misere" and "standard").
  
    4)The player_computer function is used to calculate the best move for the computer player. It iterates through possible moves and uses the MinMax algorithm to select the move with the highest score.
  
    5)Utility functions are defined to support the main game logic, including functions to calculate points (calc_points), generate possible moves (moves_possible), and determine the winner and score (calc_win).
   
    6)The code checks for command-line arguments to determine the initial number of red and blue marbles, the game version ("misere" or "standard"), and the starting player. If not provided, default values are used.

How to RUN the code 
    The .py file is in zip folder, you need to extract it.  
    
	You can call the function using the filename :- red_blue_nim.py followed by number of red marble and then the number of blue marbles.
	
Then you need to pass the version command which is as follows:
            for misere - "misere"
            for standard - "standard"
   
Then you need to pass the first players command which is as follows:
            for computer - "computer"
            for human - "human"

If no version is given then by default it'll take standard version and for first player if nothing is passed then by default player would be computer. 
	But if a wrong input will be given it will give error.	
	
Command line arguement to run the code
	red_blue_nim.py <num-red> <num-blue> <version> <first-player>
