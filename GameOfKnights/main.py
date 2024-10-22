import numpy as np
from easyAI import TwoPlayerGame

# Kierunki poruszania się figury
DIRECTIONS = list(map(np.array, [[1, 2], [-1, 2], [1, -2], [-1, -2],
                                 [2, 1], [2, -1], [-2, 1], [-2, -1]]))

"""
    Converts coordinates (x, y) to a chess square (e.g., (3, 7) to 'D8').
    
    Args:
    x (int): The column index (0-7).
    y (int): The row index (0-7).
    
    Returns:
    str: The chess square in format 'LetterNumber' (e.g., 'D8').
"""
pos2string = lambda pos: "ABCDEFGH"[pos[0]] + str(pos[1] + 1)
"""
    Converts a chess square (e.g., 'D8') to coordinates (7, 7).
    
    Args:
    square (str): The chess square in format 'LetterNumber' (e.g., 'D8').
    
    Returns:
    tuple: A tuple (x, y) where x is the column (0-7) and y is the row (0-7).
"""
string2pos = lambda str: np.array(["ABCDEFGH".index(str[0]), int(str[1]) - 1])

class Knights(TwoPlayerGame):
    """
        Game Rules:
        1.	Board: The game is played on a board ranging from 4x4 to 8x8.
        2.	Game Start: Players start in opposite corners of the board (e.g., one in corner A1 and the other in corner H8 on an 8x8 board).
        3.	Pieces: Each player has one piece - a knight. The knight moves as in traditional chess, which means it jumps to a square that is two squares in one direction and one square in another direction (a total of eight possible moves).
        4.	Objective: Players must force their opponent into a situation where they have no available moves.
        5.	Moves:
        •	A square that has been visited cannot be occupied again by the knight.
        •	Players take turns making moves, starting with the player who occupies the corner of the board (e.g., A1).
        6.	Loss: The player who cannot make any moves during their turn loses.

        Authors:
        Karol Sielski
        Tomasz Wasielewski

        Requirements:
        •	Python
        •	Numpy
        •	easyAI
    """

    def __init__(self, players, board_size=(8, 8)):
        """
        Initializes all values needed to start the game.

        :param players: A two-element array of Player objects.
        :param board_size: A tuple representing the size of the board (width, height).
        :return:
        """
        board_size = self.set_board_size(board_size)

        self.players = players
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype=int)
        self.board[0, 0] = 1
        self.board[board_size[0] - 1, board_size[1] - 1] = 2
        players[0].pos = np.array([0, 0])
        players[1].pos = np.array([board_size[0] - 1, board_size[1] - 1])
        self.current_player = 1
        self.current_player = self.current_player

    def set_board_size(self, board_size):
        """
        Validates and sets the board size based on the provided dimensions.

        This method ensures that the board size falls within the allowed range
        (minimum 4x4 and maximum 8x8). If the provided dimensions are outside
        this range, they are adjusted to fit within the valid limits.

        :param board_size: A tuple representing the desired size of the board
                           (width, height). Both width and height should be
                           integers.
        :return: A tuple (width, height) representing the validated board size,
                 adjusted to be within the range of 4 to 8.
        """
        width, height = board_size
        width = max(4, width)
        height = max(4, height)
        width = min(width, 8)
        height = min(height, 8)
        return (width, height)

    def possible_moves(self):
        """
        Calculates and returns a list of valid possible moves for the current player.

        This method determines the potential positions the current player can move to
        based on the current position of their knight. The method considers predefined
        directions (defined in DIRECTIONS) and checks whether each calculated position
        is within the board boundaries and not already occupied.

        :return: A list of strings representing valid positions the current player
                 can move to. Each position is formatted as a string (e.g., 'D5').
        """
        endings = [self.players[self.current_player - 1].pos + d for d in DIRECTIONS]
        return [pos2string(e) for e in endings
                if (0 <= e[0] < self.board_size[0]) and
                (0 <= e[1] < self.board_size[1]) and
                self.board[e[0], e[1]] == 0]

    def make_move(self, pos):
        """
        Updates the game state by moving the current player's knight to a new position.

        This method performs the following actions:
        1. Marks the current position of the player's knight as blocked on the board.
        2. Updates the player's position to the new specified position.
        3. Places the player’s knight at the new position on the board.

        :param pos: A string representing the new position to move to (e.g., 'D5').
                    This position is converted to board coordinates using the
                    string2pos function.
        :return: None
        """
        x, y = self.players[self.current_player - 1].pos
        self.board[x, y] = 3  # 3 means blocked
        self.players[self.current_player - 1].pos = string2pos(pos)
        x, y = self.players[self.current_player - 1].pos
        self.board[x, y] = self.current_player  # place player on board

    def ttentry(self):
        """
        Creates a tuple representing the current state of the game board and player positions.

        This method constructs a tuple that includes:
        1. The current state of the board as a tuple of tuples.
        2. The position of Player 1 converted to a string.
        3. The position of Player 2 converted to a string.

        This representation can be used for techniques like transposition tables
        in game algorithms to efficiently store and retrieve game states.

        :return: A tuple containing:
                 - A tuple of tuples representing the current state of the board.
                 - A string representing Player 1's position.
                 - A string representing Player 2's position.
        """
        e = [tuple(row) for row in self.board]
        e.append(pos2string(self.players[0].pos))
        e.append(pos2string(self.players[1].pos))
        return tuple(e)

    def ttrestore(self, entry):
        """
        Restores the game state from a given transposition table entry.

        This method updates the current game board and player positions based on
        the provided entry, which contains the serialized state of the game.
        It assigns the board's state and restores the positions of both players.

        :param entry: A tuple representing a saved game state. The tuple consists of:
                      - A series of tuples representing the board state.
                      - A string representing Player 1's position.
                      - A string representing Player 2's position.
        :return: None
        """
        for x, row in enumerate(entry[:self.board_size[0]]):
            for y, n in enumerate(row):
                self.board[x, y] = n
        self.players[0].pos = string2pos(entry[-2])
        self.players[1].pos = string2pos(entry[-1])

    def show(self):
        """
        Displays the current state of the game board in a human-readable format.

        This method prints the game board to the console, including:
        - A header row showing the column numbers.
        - Each row of the board represented by letters (A-H) followed by the contents of that row.
        - The board uses specific characters to represent different states:
            - '.' for unoccupied squares
            - '1' for Player 1's knight
            - '2' for Player 2's knight
            - 'X' for blocked squares

        The output provides a visual representation of the board, making it easier for players
        to understand the current state of the game.

        :return: None
        """
        header = '  ' + ' '.join(map(str, range(1, self.board_size[1] + 1)))
        print('\n' + '\n'.join([header] +
                               ['ABCDEFGH'[k] +
                                ' ' + ' '.join([['.', '1', '2', 'X'][self.board[k, i]]
                                                for i in range(self.board_size[1])])
                                for k in range(self.board_size[0])] + ['']))

    def lose(self):
        """
        Determines if the current player has lost the game.

        A player is considered to have lost if they have no possible moves available.
        This is checked by calling the `possible_moves` method.

        :return: True if the current player has lost; otherwise, False.
        """
        return self.possible_moves() == []

    def scoring(self):
        """
        Calculates the score for the current player.

        The scoring is determined based on the game's state:
        - Returns -100 if the player has lost (i.e., no possible moves).
        - Returns 0 if the player has not lost.

        :return: An integer score representing the player's current state.
        """
        return -100 if self.lose() else 0

    def is_over(self):
        """
        Checks if the game is over for the current player.

        The game is considered over if the current player has lost,
        which is determined by calling the `lose` method.

        :return: True if the game is over (the current player has lost); otherwise, False.
        """
        return self.lose()


if __name__ == "__main__":
    """
    Initializes and plays a game of Knights between a human player and an AI player.

    This function sets up the game by creating a Negamax AI with a specified depth for decision-making. 
    It initializes the game with a human player and the AI player, then starts the gameplay loop. 
    After the game concludes, it prints the result indicating which player has lost.

    :return: None
    """
    from easyAI import AI_Player, Human_Player, Negamax

    ai_algorythm = Negamax(5)  # AI depth for decision-making
    game = Knights([Human_Player(), AI_Player(ai_algorythm)], (1, 1))  # Human vs AI
    game.play()
    print("Player %d loses" % game.current_player)
