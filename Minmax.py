def is_game_over(state):

    # Check if the game is over and return the winner or tie

    for row in state:

        if all(cell == 'X' for cell in row):

            return 'X'

        if all(cell == 'O' for cell in row):

            return 'O'



    for col in range(3):

        if all(state[row][col] == 'X' for row in range(3)):

            return 'X'

        if all(state[row][col] == 'O' for row in range(3)):

            return 'O'



    if all(state[i][i] == 'X' for i in range(3)) or all(state[i][2 - i] == 'X' for i in range(3)):

        return 'X'

    if all(state[i][i] == 'O' for i in range(3)) or all(state[i][2 - i] == 'O' for i in range(3)):

        return 'O'



    if all(cell != ' ' for row in state for cell in row):

        return None  # It's a tie



    return False  # Game is not over



def get_valid_moves(state):

    # Return a list of valid moves (empty cells) from the given state

    moves = []

    for row in range(3):

        for col in range(3):

            if state[row][col] == ' ':

                moves.append((row, col))

    return moves



def make_move(state, move, player):

    # Return a new state after applying the move to the given state

    new_state = [row.copy() for row in state]

    new_state[move[0]][move[1]] = player

    return new_state



def minimax(state, player):

    winner = is_game_over(state)

    if winner is not False:

        if winner == 'X':

            return 1

        elif winner == 'O':

            return -1

        else:  # Tie

            return 0



    moves = get_valid_moves(state)

    if player == 'X':

        best_score = float('-inf')

        for move in moves:

            new_state = make_move(state, move, player)

            score = minimax(new_state, 'O')

            best_score = max(score, best_score)

        return best_score

    else:  # player == 'O'

        best_score = float('inf')

        for move in moves:

            new_state = make_move(state, move, player)

            score = minimax(new_state, 'X')

            best_score = min(score, best_score)

        return best_score



# Example usage

if __name__ == "__main__":

    board = [['X', ' ', 'O'],

             ['O', 'X', ' '],

             ['X', 'O', ' ']]

    player = 'X'

    print("The Tic-Tac-Toe board state:")

    for row in board:

        print(" | ".join(row))

        print("-" * 9)

    score = minimax(board, player)

    print(f"The score for player {player} is: {score}")

