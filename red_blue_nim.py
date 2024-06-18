# Import required modules
import sys
import math

# Function to check balls available in the piles and execute the game based on the rules
def game(remain_balls, version, start_player):
    print("Game Started")
    turn = start_player
    while remain_balls["red"] > 0 and remain_balls["blue"] > 0:
        print("----------------------------------------------------------")
        print(f"Balls left: {remain_balls}")
        if turn == 'human':
            current_player = 'human'
            pile = input(f"Pick a pile to take red or blue marbles? ")
            while pile not in ["red", "blue"] or remain_balls[pile] == 0:
                pile = input("Invalid move. Choose red or blue!")
            remain_balls[pile] -= 1
            print(f"Human picked one marble from the {pile} pile.")
        elif turn == 'computer':
            current_player = 'computer'
            pile, remove = player_computer(remain_balls, version)
            remain_balls[pile] -= remove
            print(f"Computer picked one marble from the {pile} pile.")
        turn = 'human' if turn == 'computer' else 'computer'
    print("Game Over")
    result, score = calc_win(remain_balls, version, current_player)
    print(f"<--------The {result} wins with a score of {score}-------->")

# MinMax search with alpha-beta pruning
def minmax(remain_balls, version, max_player, alpha=-float("inf"), beta=float("inf")):
    if remain_balls["red"] == 0 or remain_balls["blue"] == 0:
        return calc_points(remain_balls)
    if version == "misere":
        return minmax_misere(remain_balls, max_player, alpha, beta)
    elif version == "standard":
        return minmax_standard(remain_balls, max_player, alpha, beta)

def minmax_misere(balls_left, max_player, alpha, beta):
    move_order = ["blue", "red"]  # Adjust move order to prioritize blue balls in misere version
    if max_player:
        best_score = float("-inf")
        for current_color in move_order:
            for amount in range(1, balls_left[current_color] + 1):
                new_balls_left = balls_left.copy()
                new_balls_left[current_color] -= amount
                score = minmax_misere(new_balls_left, True, alpha, beta)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    return best_score
        return best_score
    else:
        best_score = float("inf")
        for current_color in move_order:
            for amount in range(1, balls_left[current_color] + 1):
                new_balls_left = balls_left.copy()
                new_balls_left[current_color] -= amount
                score = minmax_misere(new_balls_left, False, alpha, beta)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if alpha >= beta:
                    return best_score
        return best_score

# Minmax version for standard version
def minmax_standard(balls_left, max_player, alpha, beta):
    move_order = ["blue", "red"]  # Standard move ordering
    if balls_left["red"] == 0 or balls_left["blue"] == 0:
        return calc_points(balls_left)
    if max_player:
        best_score = float("-inf")
        for current_color in move_order:
            if balls_left[current_color] > 0:
                for amount in range(1, balls_left[current_color] + 1):
                    new_balls_left = balls_left.copy()
                    new_balls_left[current_color] -= amount
                    score = minmax_standard(new_balls_left, False, alpha, beta)
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        return best_score
        return best_score
    else:
        best_score = float("inf")
        for current_color in move_order:
            if balls_left[current_color] > 0:
                for amount in range(1, balls_left[current_color] + 1):
                    new_balls_left = balls_left.copy()
                    new_balls_left[current_color] -= amount
                    score = minmax_standard(new_balls_left, True, alpha, beta)
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        return best_score
        return best_score

# Function to determine the best move for the computer player
def player_computer(remain_balls, version):
    best_move = None
    max_score = float("-inf")
    for color, remove in moves_possible(remain_balls, version):
        new_remain_balls = remain_balls.copy()
        new_remain_balls[color] -= remove
        score = minmax(new_remain_balls, version, False)
        if score > max_score:
            best_move = (color, remove)
            max_score = score
    return best_move

# Function to calculate the score based on the balls left in the piles
def calc_points(remain_balls):
    return 2 * remain_balls["red"] + 3 * remain_balls["blue"]

# Function to generate possible moves based on the version
def moves_possible(remain_balls, version):
    possible_moves = []
    colors = ["red", "blue"]
    if version == "misere":
        colors = (colors)
    for color in colors:
        if remain_balls[color] > 0:
            possible_moves.append((color, 1))
    return possible_moves

# Function to calculate the winner based on the current player and the version
def calc_win(remain_balls, version, current_player):
    if version == "misere":
        if current_player == "human":
            winner = "computer" if remain_balls["red"] == 0 or remain_balls["blue"] == 0 else "human"
        else:
            winner = "human" if remain_balls["red"] == 0 or remain_balls["blue"] == 0 else "computer"
    else:  # Default version is "standard"
        if current_player == "human":
            winner = "human" if remain_balls["red"] == 0 or remain_balls["blue"] == 0 else "computer"
        else:
            winner = "computer" if remain_balls["red"] == 0 or remain_balls["blue"] == 0 else "human"
    score = 2 * remain_balls["red"] + 3 * remain_balls["blue"]
    return winner, score

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Input Format: red_blue_nim.py num-red num-blue version start-player")
        sys.exit()
    n_red = int(sys.argv[1])
    n_blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else "standard"
    start_player = sys.argv[4] if len(sys.argv) > 4 else "computer"
    remain_balls = {"red": n_red, "blue": n_blue}
    game(remain_balls, version, start_player)