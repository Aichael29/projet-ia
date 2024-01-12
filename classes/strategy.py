import random
import numpy as np

import classes.logic as logic

# When implementing a new strategy add it to the `str2strat`
# dictionary at the end of the file


class PlayerStrat:
    def __init__(self, _board_state, player):
        self.root_state = _board_state
        self.player = player

    def start(self):
        """
        This function select a tile from the board.

        @returns    (x, y) A tuple of integer corresponding to a valid
                    and free tile on the board.
        """
        raise NotImplementedError


class Node(object):
    """
    This class implements the main object that you will manipulate : nodes.
    Nodes include the state of the game (i.e. the 2D board), children (i.e. other children nodes), a list of
    untried moves, etc...
    """

    def __init__(self, board, move=(None, None), wins=0, visits=0, children=None):
        # Save the #wins:#visited ratio
        self.state = board
        self.move = move
        self.wins = wins
        self.visits = visits
        self.children = children or []
        self.parent = None
        self.untried_moves = logic.get_possible_moves(board)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


class Random(PlayerStrat):
    def start(self):
        """
        This function select a tile from the board.

        @returns    (x, y) A tuple of integer corresponding to a valid
                    and free tile on the board.
        """
        print("Random strategy selected")
        return random.choice(logic.get_possible_moves(self.root_state))


class MiniMax(PlayerStrat):
    def __init__(self, _board_state, player):
        super().__init__(_board_state, player)
        self.enemy = 3 - self.player

    def start(self):
        """
        This function select a tile from the board.

        @returns    (x, y) A tuple of integer corresponding to a valid
                    and free tile on the board.
        """
        print("MiniMax strategy selected")
        return self.minimax()

    def minimax(self):
        return self.max_value(self.root_state, self.player)[1]

    def max_value(self, board, player):
        if (
            logic.is_game_over(player, board)
            or len(logic.get_possible_moves(board)) == 0
        ):
            return self.evaluate(player, board), None

        best_score = -np.Infinity
        best_move = None

        for action in logic.get_possible_moves(board):
            x, y = action
            board[x][y] = player

            score, _ = self.min_value(board, self.enemy)
            board[x][y] = 0

            if score == 1:
                return score, action

            if score > best_score:
                best_score = score
                best_move = action

        return best_score, best_move

    def min_value(self, board, player):
        if (
            logic.is_game_over(player, board)
            or len(logic.get_possible_moves(board)) == 0
        ):
            return self.evaluate(player, board), None

        best_score = np.Infinity
        best_move = None

        for action in logic.get_possible_moves(board):
            x, y = action
            board[x][y] = player
            score, _ = self.max_value(board, self.player)
            board[x][y] = 0

            if score == -1:
                return score, action

            if score < best_score:
                best_score = score
                best_move = action

        return best_score, best_move

    def evaluate(self, player, board):
        """
        This function evaluates the given board and returns a score.
        The score is evaluated by counting the number of connected tiles and distance to the border.

        @param board: The board to evaluate.
        @return: The score of the board.
        """
        if player == self.player and logic.is_game_over(player, board) == player:
            return +1

        return -1


str2strat: dict[str, PlayerStrat] = {
    "human": None,
    "random": Random,
    "minimax": MiniMax,
}
