from enum import Enum
import random

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

def random_move():
    '''
    Returns a random move
    '''
    return random.choice(list(Move))


def random_but_different(last_move):
    '''
    Returns a random move except the last move
    '''
    next_move = random_move()
    while next_move == last_move:
        next_move = random_move()
    return next_move


def evaluate_moves(move1, move2):
    if move1 == move2:
        return Outcome.DRAW

    if move1 == Move.ROCK:
        if move2 == Move.SCISSORS:
            return Outcome.WIN 
    elif move1 == Move.PAPER:
        if move2 == Move.ROCK:
            return Outcome.WIN
    elif move1 == Move.SCISSORS:
        if move2 == Move.PAPER:
            return Outcome.WIN 
    
    return Outcome.LOSE

def strategic_choice(opponent_move, outcome):
    '''
    If won, choose the opponents move as the next move
    If lost, play the move that would have beat the opponent move or in other words play the move which wasn't played that round.
    '''

    if not opponent_move: 
        return random_move()

    if outcome == Outcome.WIN:
        return opponent_move
    else:
        if opponent_move == Move.ROCK:
            return Move.PAPER
        elif opponent_move == Move.PAPER:
            return Move.SCISSORS
        else:
            return Move.ROCK
    
def biased_at_wins(last_move, outcome, bias = 0.5):
    '''
    The player changes his move when he has lost
    When he has won he will change his move in n amount of times where n is defined by the bias.
    A bias of 0.5 means he changes his move 50% of the time, 0.25 = 25% of the time etc.
    '''
    # if there was no last move choose randomly
    if not last_move:
        return random_move()

    if outcome == Outcome.WIN and random.random() <= bias or outcome == Outcome.LOSE:
        return random_but_different(last_move)

    return last_move 
        
PLAYS = 1000

# Both random strategies
print('Situation 1: Both choose randomly')
p1_wins = 0
p2_wins = 0
draws = 0
for i in range(0, PLAYS):
    p1_move = random_move()
    p2_move = random_move()

    outcome = evaluate_moves(p1_move, p2_move)
    if outcome == Outcome.WIN:
        p1_wins += 1
    elif outcome == Outcome.LOSE:
        p2_wins += 1
    else:
        draws += 1

print('Player 1 wins:\t' + str(p1_wins) + ' = ' + str(float(p1_wins) / PLAYS * 100) + '%')
print('Player 2 wins:\t' + str(p2_wins) + ' = ' + str(float(p2_wins) / PLAYS * 100) + '%')
print('Draws:\t\t' + str(draws) + ' = ' + str(float(draws) / PLAYS * 100) + '%')
print('')

# One chooses randomly  one strategic
print('Situation 2: One chooses randomly, one is strategic')
p1_wins = 0
p2_wins = 0
draws = 0
p1_last_move = None
last_outcome = None 
for i in range(0, PLAYS):
    p1_move = random_move() 
    p2_move = strategic_choice(p1_last_move, last_outcome)

    outcome = evaluate_moves(p1_move, p2_move)
    if outcome == Outcome.WIN:
        p1_wins += 1
    elif outcome == Outcome.LOSE:
        p2_wins += 1
    else:
        draws += 1
    p1_last_move = p1_move
    last_outcome = outcome
print('Player 1 wins:\t' + str(p1_wins) + ' = ' + str(float(p1_wins) / PLAYS * 100) + '%')
print('Player 2 wins:\t' + str(p2_wins) + ' = ' + str(float(p2_wins) / PLAYS * 100) + '%')
print('Draws:\t\t' + str(draws) + ' = ' + str(float(draws) / PLAYS * 100) + '%')
print('')

# One biased one strategic
print('Situation 3: One keeps move if won, one is strategic')
p1_wins = 0
p2_wins = 0
draws = 0
p1_last_move = None
last_outcome = None 
for i in range(0, PLAYS):
    p1_move = biased_at_wins(p1_last_move, last_outcome, 0.25)
    p2_move = strategic_choice(p1_last_move, last_outcome)

    outcome = evaluate_moves(p1_move, p2_move)
    if outcome == Outcome.WIN:
        p1_wins += 1
    elif outcome == Outcome.LOSE:
        p2_wins += 1
    else:
        draws += 1
    p1_last_move = p1_move
    last_outcome = outcome
print('Player 1 wins:\t' + str(p1_wins) + ' = ' + str(float(p1_wins) / PLAYS * 100) + '%')
print('Player 2 wins:\t' + str(p2_wins) + ' = ' + str(float(p2_wins) / PLAYS * 100) + '%')
print('Draws:\t\t' + str(draws) + ' = ' + str(float(draws) / PLAYS * 100) + '%')
print('')

# One biased one strategic changes move at draws
print('Sitation 4: One keeps move if won, one is strategic but changes move at draws')
p1_wins = 0
p2_wins = 0
draws = 0
p1_last_move = None
last_outcome = None 
for i in range(0, PLAYS):
    p1_move = biased_at_wins(p1_last_move, last_outcome, 0.25)
    if last_outcome == Outcome.DRAW:
        p2_move = random_move()
    else:
        p2_move = strategic_choice(p1_last_move, last_outcome)

    outcome = evaluate_moves(p1_move, p2_move)
    if outcome == Outcome.WIN:
        p1_wins += 1
    elif outcome == Outcome.LOSE:
        p2_wins += 1
    else:
        draws += 1
    p1_last_move = p1_move
    last_outcome = outcome
print('Player 1 wins:\t' + str(p1_wins) + ' = ' + str(float(p1_wins) / PLAYS * 100) + '%')
print('Player 2 wins:\t' + str(p2_wins) + ' = ' + str(float(p2_wins) / PLAYS * 100) + '%')
print('Draws:\t\t' + str(draws) + ' = ' + str(float(draws) / PLAYS * 100) + '%')
print('')

# Both are strategic
print('Situation 5: Both are strategic')
p1_wins = 0
p2_wins = 0
draws = 0
p1_last_move = None
p2_last_move = None
last_outcome = None
for i in range(0, PLAYS):
    p1_move = strategic_choice(p2_last_move, last_outcome) 
    p2_move = strategic_choice(p1_last_move, last_outcome)

    outcome = evaluate_moves(p1_move, p2_move)
    if outcome == Outcome.WIN:
        p1_wins += 1
    elif outcome == Outcome.LOSE:
        p2_wins += 1
    else:
        draws += 1
    p1_last_move = p1_move
    last_outcome = outcome
print('Player 1 wins:\t' + str(p1_wins) + ' = ' + str(float(p1_wins) / PLAYS * 100) + '%')
print('Player 2 wins:\t' + str(p2_wins) + ' = ' + str(float(p2_wins) / PLAYS * 100) + '%')
print('Draws:\t\t' + str(draws) + ' = ' + str(float(draws) / PLAYS * 100) + '%')
print('')
