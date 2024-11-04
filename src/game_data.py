import numpy as np

game_board_position = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

winning_combination = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# Tablero de juego vacío inicial
initial_game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

game_positions = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

game_board = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])