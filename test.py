from tictactoe import minimax, winner, actions, result, maximizer, minimizer

EMPTY = None
X = "X"
O = "O"

board = [[X, O, X],
            [O, X, X],    
            [O, X, O]]
print(minimizer(board=board))