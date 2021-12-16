#HUZZA, I MERLIN, HAVE DONE SOMETHING NO ONE ELSE HAS DONE, TEACH ROHAN WHY TO COMBINE DIFFERENT FUNCTIONS TO MAKE EPIC STUFF
import random, time, os

#Player class
class Player:
    def __init__(self, userName, points, wins, losses):
        self.userName = userName
        self.points = points
        self.wins = wins
        self.losses = losses

    def changeName(self, newName):
        self.userName = newName

    def __add__(self, amt):
        self.points += amt

    def __sub__(self, amt):
        self.points -= amt

def sleep_os(sleep_amt):
    time.sleep(sleep_amt)
    os.system('cls')

def getBall():
    return random.randint(1, 3)

def player_Guess():
    possible_guesses = ['1', '2', '3']
    num_guess = input('Which cup do you think the ball is in? (1 - 3) \n')
    while num_guess not in possible_guesses:
        print('Your guess was not in the possible guesses. Please guess again')
        num_guess = input('\n')

    return num_guess

def portion_G(p):
    Ball = str(getBall())
    p_G = player_Guess()
    if p_G != Ball:
        print('Oof {}! You did not guess the ball D: \n It was in cup #{}'.format(p.userName, Ball))
        p.losses += 1
        p.points += 10
    elif p_G == Ball:
        print('Yay {}! You gussed the cup which the ball is in! :D'.format(p.userName))
        p.wins += 1
        p.points += 100

    sleep_os(3.75)

    print('Username: {} \n Points: {} \n Wins: {} \n Losses: {} \n'.format(p.userName, p.points, p.wins, p.losses))

def aft_Game(p):
    portion_G(p)

    sleep_os(3.75)

    p_opts = input('Enter E to exit. Enter Y to play again. \n')

    while p_opts == 'Y':
        portion_G(p)

        sleep_os(3.25)

        p_opts = input('Enter E to exit. Enter Y to play again. \n')

    exit()

#The variubles
cupNum = None
player_1 = Player('Player 1', 0, 0, 0)

# Introduction to the game
print('{} {} Game made for education purposes {} {}'.format('-'*40, '\n', '\n', '-'*39))
sleep_os(3.75 / 2)
print('Welcome to the demonstration game! Here is how to play!', '\n', 'There are three cups, you have to guess which cup the ball is in by typing a number from 1 to 3')
sleep_os(3.75 * 2)
ask_start = input('Type in "Q" to setup your player. Type anything else to start. \n')

#Setting player's username
if ask_start == 'Q':
    print('What do you want your username to be?')
    player_1.changeName(input('\n'))
    print('Name changed to {}'.format(player_1.userName))

#The game itself
sleep_os(3.75)

aft_Game(player_1)
