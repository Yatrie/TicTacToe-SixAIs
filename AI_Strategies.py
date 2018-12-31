#!/usr/bin/env python

__author__ = "Vivek M Agrawal"
__version__ = "1.0"
__email__ = "yatrie@gmail.com"

""" AI Strategies
    Implementation based on: Crowley, K., & Siegler, R. S. (1993). 
    Flexible strategy use in young children's Tic Tac Toe.
    Cognitive Science, 17(4), 531561.
"""

import random

def get_symbol(player):
    if player == 1:
        s = 'X'
    else:
        s ='O'
    return s

def checkForWin(b, s):
    # Check for win on the board 'b' for symbol 's'
    
    # Intialize flag
    winFlag = False
    
    # Check for win
    winFlag = ((b[0] == s and b[1] == s and b[2] == s) or
            (b[3] == s and b[4] == s and b[5] == s) or
            (b[6] == s and b[7] == s and b[8] == s) or
            # above checks rows
            (b[0] == s and b[3] == s and b[6] == s) or
            (b[1] == s and b[4] == s and b[7] == s) or
            (b[2] == s and b[5] == s and b[8] == s) or
            # above checks columns
            (b[0] == s and b[4] == s and b[8] == s) or
            (b[2] == s and b[4] == s and b[6] == s)
            # above checks diagonals
            )
    return winFlag
    
def nextSmartMove(b, s):
    #print('In nextSmartMove')
    # gives an illusion of intelligence on next set of moves
    c = copyBoard(b)
    for i in range (0, 9):
        if b[i] == '':
            c[i] = s
            for j in range (0, 9):
                if c[j] == '':
                    if checkForWin(c, s):
                        return i
    return -1
    
def copyBoard(b):
    # This form of copy is needed to avoid refrencing problems in Python
    copy = []
    for s in b:
        copy.append(s)
    return copy

def random_move (b,s):
    #print('In random_move')
    move_made = 0
    while move_made == 0:
        i = random.randint(0,8)
        #print i
        if b[i] == '':
            return i
    
def takeCenter(b, s):
    # AI mode that aims at taking center
    #print('In take Center')
    if (b[4] == ''): 
        return 4
    else: 
        return -1

def takeCorner(b, s):
    #print('In takeCorner')
    # AI mode that aims at taking one of the corners
    
    # Initialize list of open corners
    c = []
    
    # check for open corners
    if (b[0] == ''): c.append(0)
    if (b[2] == ''): c.append(2)
    if (b[6] == ''): c.append(6)
    if (b[8] == ''): c.append(8)
    
    # randomly return one of the open corners
    if not c:
        # if no open corners exist
        return -1
    else:
        # else select one item randomly from the list
        return c[random.randint(0, len(c)-1)]

def takeOpposingCorner(b, s):
    #print('In takeOpposingCorner')
    # AI mode that aims at taking one of the opposing corners
    
    # check for open corners
    if (b[0] == s and b[8] == ''): 
        return 8
    if (b[8] == s and b[0] == ''): 
        return 0
    if (b[2] == s and b[6] == ''): 
        return 6
    if (b[6] == s and b[2] == ''): 
        return 2
        
    return -1

def takeSide(b, s):
    #print('In takeSide')
    # AI mode that aims at taking one of the side squares

    # Initialize list of side squares
    c = []

    # check for empty side squares
    if (b[1] == ''): c.append(1)
    if (b[3] == ''): c.append(3)
    if (b[5] == ''): c.append(5)
    if (b[7] == ''): c.append(7)

    # randomly return one of the open side squares
    if not c:
        # if no open side squares exist
        return -1
    else:
        # else select one item randomly from the list
        return c[random.randint(0, len(c)- 1)]

def winMove(b, s):
    #print('In winMove')
    # AI mode that aims at winning on next move
    
    # test for the winning configuration
    for i in range(0, 9):
        # copy board 'b' to temporary board 'c'
        c = copyBoard(b)
        if (c[i] == ''):
            # if location empty, copy symbol 's' to the copied board
            # and check if the new configuration is a win condition
            c[i] = s
            if (checkForWin(c, s) == True):
                return i
    return -1
    
def forkMove(b, s):
    #print('In forkMove')
    # AI mode that aims at forking
    
    # test for empty corners  
    if (b[0] == ''):
        # Test for membership of horizontal, diagornal and vertical arcs
        # such that one of the elements is self symbol and the other is
        # the empty symbol
        r0h = (b[1] == s and b[2] == '') or (b[1] == '' and b[2] == s)
        r0d = (b[4] == s and b[8] == '') or (b[4] == '' and b[8] == s)
        r0v = (b[3] == s and b[6] == '') or (b[3] == '' and b[6] == s)
    
        # Test if the condition is met for any pair of two arcs
        if ((r0h and r0d) or (r0h and r0v) or (r0d and r0v)):
            # If so, return the corner value
            return 0
    
    if (b[2] == ''):
        # Test for membership of horizontal, diagornal and vertical arcs
        # such that one of the elements is self symbol and the other is
        # the empty symbol
        r2h = (b[1] == s and b[0] == '') or (b[1] == '' and b[0] == s)
        r2d = (b[4] == s and b[6] == '') or (b[4] == '' and b[6] == s)
        r2v = (b[5] == s and b[8] == '') or (b[5] == '' and b[8] == s)
    
        # Test if the condition is met for any pair of two arcs
        if ((r2h and r2d) or (r2h and r2v) or (r2d and r2v)):
            # If so, return the corner value
            return 2
    
    if (b[6] == ''):
        # Test for membership of horizontal, diagornal and vertical arcs
        # such that one of the elements is self symbol and the other is
        # the empty symbol
        r6h = (b[7] == s and b[8] == '') or (b[7] == '' and b[8] == s)
        r6d = (b[4] == s and b[2] == '') or (b[4] == '' and b[2] == s)
        r6v = (b[3] == s and b[0] == '') or (b[3] == '' and b[0] == s)
    
        # Test if the condition is met for any pair of two arcs
        if ((r6h and r6d) or (r6h and r6v) or (r6d and r6v)):
            # If so, return the corner value
            return 6
    
    if (b[8] == ''):
        # Test for membership of horizontal, diagornal and vertical arcs
        # such that one of the elements is self symbol and the other is
        # the empty symbol
        r8h = (b[7] == s and b[6] == '') or (b[7] == '' and b[6] == s)
        r8d = (b[4] == s and b[0] == '') or (b[4] == '' and b[0] == s)
        r8v = (b[2] == s and b[5] == '') or (b[2] == '' and b[5] == s)
    
        # Test if the condition is met for any pair of two arcs
        if ((r8h and r8d) or (r8h and r8v) or (r8d and r8v)):
            # If so, return the corner value
            return 8
    
    # default return to None if no forking configuration is found
    return -1

def blockWinMove(b, s):
    #print('In blockWinMove')
    # AI mode that aims at blocking opponent's win on next move
    # Determine opponent's symbol
    if (s == 'X'): 
        e = 'O'
    else: e = 'X'
    # Reuse winMove method to check for oppnents win
    x = winMove(b, e)
    
    if x is None: 
        return -1
    else: return x

def blockForkMove(b, s):
    #print('In blockForkMove')
    # AI mode that aims at blocking opponent's forking opportunity
    # Determine opponents symbol
    if (s == 'X'): 
        e = 'O'
    else: e = 'X'

    # Reuse forkMove method to check for oppnents win
    x = forkMove(b, e)

    if x is None: 
        return -1
    else: return x

def check_win(game_board):
    #print('Checking for win')
    if (game_board[0] == 'X' and game_board[1] =='X' and game_board[2] == 'X'):
        #print('Player 1 wins')
        return 1
    elif game_board[0] == 'O' and game_board[1] =='O' and game_board[2] == 'O':
        #print('Player 2 wins')
        return 2
    
    elif game_board[3] == 'X' and game_board[4] =='X' and game_board[5] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[3] == 'O' and game_board[4] =='O' and game_board[5] == 'O':
        #print('Player 2 wins')
        return 2
    
    elif game_board[6] == 'X' and game_board[7] =='X' and game_board[8] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[6] == 'O' and game_board[7] =='O' and game_board[8] == 'O':
        #print('Player 2 wins')
        return 2
    
    # Check Columns
    elif game_board[0] == 'X' and game_board[3] =='X' and game_board[6] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[0] == 'O' and game_board[3] =='O' and game_board[6] == 'O':
        #print('Player 2 wins')
        return 2
    
    elif game_board[1] == 'X' and game_board[4] =='X' and game_board[7] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[1] == 'O' and game_board[4] =='O' and game_board[7] == 'O':
        #print('Player 2 wins')
        return 2
    
    elif game_board[2] == 'X' and game_board[5] =='X' and game_board[8] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[2] == 'O' and game_board[5] =='O' and game_board[8] == 'O':
        print('Player 2 wins')
        return 2
 
    # Check Diagonals
    elif game_board[0] == 'X' and game_board[4] =='X' and game_board[8] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[0] == 'O' and game_board[4] =='O' and game_board[8] == 'O':
        #print('Player 2 wins')
        return 2
    
    elif game_board[6] == 'X' and game_board[4] =='X' and game_board[2] == 'X':
        #print('Player 1 wins')
        return 1
    elif game_board[6] == 'O' and game_board[4] =='O' and game_board[2] == 'O':
        #print('Player 2 wins')
        return 2
    else:
        #print('No winner yet')
        return 0

def check_cats_game(b):
    #print('Checking cats game')
    count = 0
    for i in b:
        if (i == 'X' or i == 'O'):
            count = count + 1
    #print('total moves: ' + str(count))
    if count == 9:
        return 1
    else:
        return 0
    
