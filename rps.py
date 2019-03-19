# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# Default player.
# A player that always plays 'rock'
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move
        return


# A player that chooses its moves randomly.
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        while True:

            rps = input("Rock, paper, scissors? > ")
            if rps.lower()not in moves:
                print("Try Again!")
            else:
                return(rps.lower())


# A player that remembers and imitates what the
# human player did in the previous round.
class ReflectPlayer(Player):
    def __init__(self):
        self.temp_move = random.choice(moves)

    def move(self):
        return self.temp_move

    def learn(self, my_move, their_move):
        self.temp_move = their_move


# A player that cycles through the three moves
class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return "rock"
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


# Rules of the game
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    # With this initializer we create 2 random players
    # for objects created from this class
    def __init__(self, cp, hp):
        self.cp = cp
        self.hp = hp
        self.hp_score = 0
        self.cp_score = 0

    # This method puts everything together and plays the game
    def play_game(self):
        print("GAME START!\n")
        while True:
            try:
                rounds = int(input("How many rounds "
                             "would you like to play? >"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        for round in range(1, rounds+1):
            print(f"\nRound {round} -")
            move1 = self.hp.move()
            move2 = self.cp.move()
    # print out the results for each player
            print(f"You played {move1}\nOpponent played {move2}")
            self.hp.learn(move1, move2)
            self.cp.learn(move2, move1)
            if beats(move1, move2):
                self.hp_score += 1
                print("** PLAYER ONE WINS **")

            elif beats(move2, move1):
                self.cp_score += 1
                print("** PLAYER TWO WINS **")
            else:
                print("TIE!")
            print(f"Score: Player 1: {self.hp_score} "
                  "Player 2: {self.cp_score}")
        print("GAME OVER!\n")
        print("-----------------------------------")
        print("** FINAL SCORE **")
        print(f"Score: Player 1: {self.hp_score}, Player 2: {self.cp_score}")
        if self.hp_score > self.cp_score:
            print("** PLAYER ONE WON **")
        elif self.hp_score < self.cp_score:
            print("** PLAYER TWO WON **")
        else:
            print("** TIE **")
        play_again = valid_input("Would you like to play again? (y,n)",
                                 "y", "n")
        if 'n' in play_again:
            print("Goodbye.")
        elif 'y' in play_again:
            self.hp_score = 0
            self.cp_score = 0
            self.play_game()


# create a new instance with the Game class that has
# 2 random player objects from the RandomPlayer class
if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    # play the game with the random players
    game.play_game()
