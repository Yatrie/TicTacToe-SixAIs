#!/usr/bin/env python

__author__ = "Vivek M Agrawal, Eric Thoroe"
__version__ = "1.0"
__email__ = "yatrie@gmail.com"

""" Tic Tac Toe
    Implementation of six different Artificial Intelligences representing
    the mental models for: a Kindergartener, First Grader, Third Grader,
    and three Adults with one being Expert player.

    Models based on strategies defined in: Crowley, K., & Siegler, R. S.
    (1993). Flexible strategy use in young children's Tic Tac Toe.
    Cognitive Science, 17(4), 531561.
    
    Experiment Design & TKinter Interface Implementation: Eric Thoroe
    AI Strategies and Player Models : Vivek Agrawal
"""

import Tkinter
import threading
import Queue
import time
import datetime
import random
import AI_Strategies
import AI_Players

global game_board
global player
global Human_is_2
global ai_player
global player_matchups
global game_count

game_board = ['','','','','','','','','']
game_count = 0
player = 1
Human_is_2 = 1
ai_player = 0

""" player matchups notes:
    Randomly matches player with the 6 different AIs and one randomized AI
    for AI-first and Human-first scenarios, leading to 14 match tournament
    Human = 1, AI_Random = 2, AI Kindergartner = 3 etc.
    E.g. Player 1 = AI_Random, Player 2 = Human, then the list entry is 21
"""
player_matchups = [12,13,14,15,16,17,18,81,71,61,51,41,31,21]

# output file capturing order of AIs called during the matchup and results 
fname = "AI_Call_Order_And_Results.txt"
write_file = open(fname,'w')
write_file.write("2:Random,3:Kindergartner,4:FirstGrader,5:ThirdGrader,\
6:AdultDefensive,7:AdultAggressive,8:Expert \n\n")
write_file.write("Date,Timestamp,Game-No.,AI-Level,AI-First?,Result\n")

def update_player():
    global player
    
    if player == 1:
        player = 2
    else:
        player = 1

def time_stamp():
    start_time = datetime.datetime.now()
    date = str(start_time.month) +"_" + str(start_time.day) + "_" + \
        str(start_time.year)
    current_time = str (start_time.hour) + ":" + str(start_time.minute)+ ":" + \
        str(start_time.second)
    return (date,current_time)
        
class GUI:

    def __init__(self, master):
        
        self.master=master
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("250x250")
        
        self.cell_11 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_11,0)) 
        self.cell_12 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_12,1))
        self.cell_13 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_13,2))
                                                                         
        self.cell_21 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_21,3))
        self.cell_22 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_22,4))
        self.cell_23 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_23,5))
                                                                         
        self.cell_31 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_31,6))
        self.cell_32 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_32,7))
        self.cell_33 = Tkinter.Button(master, text='', \
            command = lambda: self.callback(self.cell_33,8))
        
        self.status = Tkinter.StringVar()
        self.status.set('')
        self.label_1 = Tkinter.Label(master, textvariable=self.status)
        self.label_1.pack()
        
        self.cell_11.place(x =50, y= 50,width =50,height=50)
        self.cell_12.place(x =100, y= 50,width =50,height=50)
        self.cell_13.place(x =150, y= 50,width =50,height=50)
       
        self.cell_21.place(x =50, y= 100,width =50,height=50)
        self.cell_22.place(x =100, y= 100,width =50,height=50)
        self.cell_23.place(x =150, y= 100,width =50,height=50)
        
        self.cell_31.place(x =50, y= 150,width =50,height=50)
        self.cell_32.place(x =100, y= 150,width =50,height=50)
        self.cell_33.place(x =150, y= 150,width =50,height=50)

        self.next_game(0)
    
    def process_queue(self):
        global game_board
        global player
        global ai_player
        global player_matchups
        global game_count
        
        try:
            msg = self.queue.get(0)
            if msg == "Human First":
                self.status.set('Your Turn!')
                self.label_1.update_idletasks()
                self.normal_button()
            elif msg == "Computer First":
                self.status.set('Opponent\'s Turn')
                self.disable_button()
                self.label_1.update_idletasks()
                
                if ai_player == 2:                    # AI_Random
                    [game_board,button] = AI_Players.AI_Random(\
                    game_board, player)
                
                elif ai_player == 3:                # AI_Kindergartner
                    [game_board,button] = AI_Players.AI_Kindergartner(\
                    game_board, player)
                
                elif ai_player == 4:                # AI_FirstGrader
                    [game_board,button] = AI_Players.AI_FirstGrader(\
                    game_board, player)
                
                elif ai_player == 5:                # AI_ThirdGrader
                    [game_board,button] = AI_Players.AI_ThirdGrader(\
                    game_board, player)
                
                elif ai_player == 6:                # AI_Adult - Defensive
                    [game_board,button] = AI_Players.AI_AdultS1(\
                    game_board, player)
                
                elif ai_player == 7:                 # AI_Adult - Aggressive
                    [game_board,button] = AI_Players.AI_AdultS2(\
                    game_board, player)
                
                elif ai_player == 8:                # AI_Expert
                    [game_board,button] = AI_Players.AI_Expert(\
                    game_board, player)
                
                # print game_board
                self.computer_update_GUI(button,game_board)
                update_player()
                self.status.set('Your Turn!')
                self.label_1.update_idletasks()
                self.normal_button()
            
            elif msg == 'Human Done':
                self.disable_button()
                
                # print game_board
                if  AI_Strategies.check_win(game_board) > 0:
                    winner = AI_Strategies.check_win(game_board)
                    self.status.set('Game Over -- You Win!')
                    self.label_1.update_idletasks()
                    time.sleep(2)
                    with self.queue.mutex:
                        self.queue.queue.clear()
                    self.next_game(winner)
                
                elif AI_Strategies.check_cats_game(game_board) == 1:
                    self.status.set('Cat\'s Game!')
                    self.label_1.update_idletasks()
                    time.sleep(2)
                    with self.queue.mutex:
                        self.queue.queue.clear()
                    self.next_game(2)
                
                else:
                    update_player()
                    self.status.set('Opponent\'s Turn')
                    self.label_1.update_idletasks()
                    
                    if ai_player == 2:                    # AI_Random
                        [game_board,button] = AI_Players.AI_Random(\
                        game_board, player)
                    
                    elif ai_player == 3:                # AI_Kindergartner
                        [game_board,button] = AI_Players.AI_Kindergartner(\
                        game_board, player)
                    
                    elif ai_player == 4:                # AI_FirstGrader
                        [game_board,button] = AI_Players.AI_FirstGrader(\
                        game_board, player)
                    
                    elif ai_player == 5:                # AI_ThirdGrader
                        [game_board,button] = AI_Players.AI_ThirdGrader(\
                        game_board, player)
                    
                    elif ai_player == 6:                # AI_Adult - Defensive
                        [game_board,button] = AI_Players.AI_AdultS1(\
                        game_board, player)
                    
                    elif ai_player == 7:                # AI_Adult - Aggressive
                        [game_board,button] = AI_Players.AI_AdultS2(\
                        game_board, player)
                    
                    elif ai_player == 8:                # AI_Expert
                        [game_board,button] = AI_Players.AI_Expert(\
                        game_board, player)
                    
                    # print game_board
                    self.computer_update_GUI(button,game_board)
                    
                    if AI_Strategies.check_win(game_board) > 0:
                        winner = AI_Strategies.check_win(game_board)
                        self.status.set('Game Over -- Better Luck Next Time')
                        self.label_1.update_idletasks()
                        time.sleep(2)
                        with self.queue.mutex:
                            self.queue.queue.clear()
                        self.next_game(winner)
                    
                    elif AI_Strategies.check_cats_game(game_board) == 1:
                        self.status.set('Cat\'s Game!')
                        self.label_1.update_idletasks()
                        time.sleep(2)
                        with self.queue.mutex:
                            self.queue.queue.clear()
                        self.next_game(2)
                    
                    else:
                        update_player()
                        self.status.set('Your Turn!')
                        self.label_1.update_idletasks()
                        self.normal_button()
                
        except Queue.Empty:
            self.master.after(100, self.process_queue)
    
    def callback(self,cell,board_pos):
        global game_board
        global player
        
        self.queue = Queue.Queue()
        self.master.after(100, self.process_queue)
            
        if game_board[board_pos] == 'X' or game_board[board_pos] == 'O':
            self.queue.put("Human First")
            
        elif game_board[board_pos] == '':
            if player == 1:
                game_board[board_pos] = 'X'
                cell.configure(text=game_board[board_pos])
                
            else:
                game_board[board_pos] = 'O'
                cell.configure(text=game_board[board_pos])
        
        self.queue.put("Human Done")

    def computer_update_GUI(self,button,game_board):    
        if button == 0:
            self.cell_11.configure(text=game_board[button])
        
        elif button == 1:
            self.cell_12.configure(text=game_board[button])
        
        elif button == 2:
            self.cell_13.configure(text=game_board[button])
        
        elif button == 3:
            self.cell_21.configure(text=game_board[button])
        
        elif button == 4:
            self.cell_22.configure(text=game_board[button])
        
        elif button == 5:
            self.cell_23.configure(text=game_board[button])
        
        elif button == 6:
            self.cell_31.configure(text=game_board[button])
        
        elif button == 7:
            self.cell_32.configure(text=game_board[button])
        
        elif button == 8:
            self.cell_33.configure(text=game_board[button])
    
    def disable_button(self):    
        self.cell_11.config(state="disabled")
        self.cell_12.config(state="disabled")
        self.cell_13.config(state="disabled")
        self.cell_21.config(state="disabled")
        self.cell_22.config(state="disabled")
        self.cell_23.config(state="disabled")
        self.cell_31.config(state="disabled")
        self.cell_32.config(state="disabled")
        self.cell_33.config(state="disabled")
    
    def normal_button(self):
        self.cell_11.config(state="normal")
        self.cell_12.config(state="normal")
        self.cell_13.config(state="normal")
        self.cell_21.config(state="normal")
        self.cell_22.config(state="normal")
        self.cell_23.config(state="normal")
        self.cell_31.config(state="normal")
        self.cell_32.config(state="normal")
        self.cell_33.config(state="normal")
    
    def next_game(self,winner):
        global game_board
        global player
        global Human_is_2
        global ai_player
        global player_matchups
        global game_count
        
        self.queue = Queue.Queue()
        self.master.after(100, self.process_queue)

        if (game_count == 0):
            self.label_1.update_idletasks()

        if winner > 0:
            if winner == 3:
                write_file.write("," + 'T')
            else:
                if Human_is_2 == 0: 
                    # Human is Player 1
                    if winner == 1:
                        write_file.write("," + 'L')
                    else:
                        write_file.write("," + 'W')
                else:                
                    # Human is Player 2
                    if winner == 1:
                        write_file.write("," + 'W')
                    else:
                        write_file.write("," + 'L')
                
            write_file.write("\n")        
            
        if (len(player_matchups) == 0):
            self.status.set('Thank you for your participation!')
            self.label_1.update_idletasks()
            time.sleep(2)
            self.master.quit()
        
        else:    
            game_count = game_count + 1
            game_board = ['','','','','','','','','']
            player = 1
            Human_is_2 = -1
            ai_player = 0
            
            while Human_is_2 == -1:
                # print player_matchups
                i = random.randrange(0,len(player_matchups))
                matchup = player_matchups[i]
                
                if matchup < 20:
                    Human_is_2 = 0 
                    # Human is Player 1 or 'X'
                    ai_player = (player_matchups[i] - 10)
                else:
                    Human_is_2 = 1 
                    # Human is Player 2 or 'O'
                    ai_player = (player_matchups[i] -1)/10
                
                player_matchups.remove(matchup)
            
            # clean the board
            self.cell_11.configure(text='')
            self.cell_12.configure(text='')
            self.cell_13.configure(text='')
            self.cell_21.configure(text='')
            self.cell_22.configure(text='')
            self.cell_23.configure(text='')
            self.cell_31.configure(text='')
            self.cell_32.configure(text='')
            self.cell_33.configure(text='')
            
            [date, time_1] = time_stamp()

            AI_first = "Y"
            if Human_is_2 != 1:
               AI_first = "N" 

            write_file.write(date + "," + time_1 + "," + str(game_count) + \
                "," + str(ai_player) + "," + str(AI_first))

            if Human_is_2 == 1:
                self.queue.put("Computer First")
            else:
                self.queue.put("Human First")
        
root = Tkinter.Tk()
main_ui = GUI(root)
root.mainloop()
