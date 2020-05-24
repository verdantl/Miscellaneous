import random
from typing import List, Tuple, Dict

MOVES = ['Rock', 'Paper', 'Scissors']

COLOURS = [0, 1, 2]


TXT_POS = [['Start Game', (100, 500)], ['', (100, 1000)],
           ['', (100, 1500)]]

# player_move = input('What is your move?')


# need something that says when mouse is down, then if the mouse is on the
# button

class Move:
    """The move that a player makes."""
    player: str
    name: str

    def __init__(self, player: str, name: str) -> None:
        self.player = player
        self.name = name


class Button:
    """Button that a player clicks on."""
    text: str
    size: int
    location: Tuple[int, int]

    def __init__(self, text: str, location: Tuple[int, int]) -> None:
        self.text = text
        self.size = 10
        self.location = location


class Game:
    """Game type"""
    proceed: bool
    buttons: List[Button]
    game_over: bool
    state: int
    results: Dict[str, int]

    def __init__(self) -> None:
        self.rounds = 0
        self.buttons = []
        self.game_over = False
        self.state = 0
        self.results = {'Human': 0, 'Computer': 0}

    def empty(self):
        """Removes all buttons on screen"""
        while len(self.buttons) > 0:
            self.buttons.pop()

    def beginning(self) -> None:
        """Game choice at the beginning"""
        self.state = 1
        self.buttons.append(Button(TXT_POS[0][0], TXT_POS[0][1]))

    def moves_creator(self) -> None:
        """Removes all game choice buttons and creates move selection buttons"""
        self.state = 2
        self.empty()
        for i in range(len(MOVES)):
            self.buttons.append(Button(MOVES[i], TXT_POS[i][1]))

    def play_again(self):
        self.state = 0
        self.empty()

def random_computer_move() -> Move:
    """Chooses a random move."""
    return Move('The computer', random.choice(MOVES))


def possible(move: Move) -> List[str]:
    """Generates a list of move hierarchy based on move"""
    possible = [MOVES, [MOVES[1], MOVES[2], MOVES[0]],
                [MOVES[2], MOVES[0], MOVES[1]]]
    for lst in possible:
        if lst[0] == move.name:
            return lst


def evaluate_winner(move1: Move, move2: Move) -> str:
    """Finds the winner based on the moves that are made."""
    lst = possible(move1)
    if move2.name == lst[0]:
        return 'It\'s a tie!'
    elif move2.name == lst[1]:
        return move2.player + ' wins! :('
    else:
        return 'You win!'
