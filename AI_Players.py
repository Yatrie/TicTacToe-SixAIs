#!/usr/bin/env python

__author__ = "Vivek M Agrawal"
__version__ = "1.0"
__email__ = "yatrie@gmail.com"

""" AI Player Models
    Player models based on combination of different strategies describes in:
    Crowley, K., & Siegler, R. S. (1993). Flexible strategy use in young 
    children's Tic Tac Toe. Cognitive Science, 17(4), 531561.
"""

import random
import AI_Strategies

def AI_Random(game_board, player):
    s = AI_Strategies.get_symbol(player)
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_Kindergartner(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win 45% of time
    a = random.randint(1,100)
    if a <= 45:
        Next_Move = AI_Strategies.blockWinMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_FirstGrader(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Take the centre space
    Next_Move = AI_Strategies.takeCenter(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win 80% of time
    a = random.randint(1,100)
    if a <= 80:
        Next_Move = AI_Strategies.blockWinMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Look for a Fork 10% of time
    a = random.randint(1,100)
    if a <= 10:
        Next_Move = AI_Strategies.forkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_ThirdGrader(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Take the centre space
    Next_Move = AI_Strategies.takeCenter(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win
    Next_Move = AI_Strategies.blockWinMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Fork 65% of time
    a = random.randint(1,100)
    if a <= 65:
        Next_Move = AI_Strategies.forkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_AdultS1(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Take the centre space
    Next_Move = AI_Strategies.takeCenter(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win
    Next_Move = AI_Strategies.blockWinMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Fork 82% of time
    a = random.randint(1,100)
    if a <= 82:
        Next_Move = AI_Strategies.forkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Look for a Block Fork 65% of time
    a = random.randint(1,100)
    if a <= 65:
        Next_Move = AI_Strategies.blockForkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Look for a the next best move
    Next_Move = AI_Strategies.nextSmartMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_AdultS2(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win
    Next_Move = AI_Strategies.blockWinMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Try and take the corner space opposite to previously occupied corner
    Next_Move = AI_Strategies.takeOpposingCorner(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Take the corner space
    Next_Move = AI_Strategies.takeCorner(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Fork 82% of time
    a = random.randint(1,100)
    if a <= 82:
        Next_Move = AI_Strategies.forkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Look for a Block Fork 65% of time
    a = random.randint(1,100)
    if a <= 65:
        Next_Move = AI_Strategies.blockForkMove(game_board, s)
        if (Next_Move >= 0):
            game_board[Next_Move] = s
            return (game_board, Next_Move)
    
    #Look for a the next best move
    Next_Move = AI_Strategies.nextSmartMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

def AI_Expert(game_board, player):
    s = AI_Strategies.get_symbol(player)
    
    #Take the centre space
    Next_Move = AI_Strategies.takeCenter(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Win
    Next_Move = AI_Strategies.winMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Win
    Next_Move = AI_Strategies.blockWinMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Fork
    Next_Move = AI_Strategies.forkMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Look for a Block Fork
    Next_Move = AI_Strategies.blockForkMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)

    #Look for a the next best move
    Next_Move = AI_Strategies.nextSmartMove(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
    
    #Just make a random move otherwise
    Next_Move = AI_Strategies.random_move(game_board, s)
    if (Next_Move >= 0):
        game_board[Next_Move] = s
        return (game_board, Next_Move)
