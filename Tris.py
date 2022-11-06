# -*- coding: utf-8 -*-
"""
@author: Francesco Govigli
"""

import tkinter as tk
import random
import numpy as np




def b_click(button,label):

    """
    b_click is the function triggered when clicking a button
    
    Parameters
    ----------
    button: the button clicked by the user that must be updated
    label: text used to show the current player on the UI

    """ 
    
    label['text'] = "It is Player {} turn ".format(game.swap_players())
    
    row = button.grid_info()['row']      # Row of the button
    col = button.grid_info()['column'] 
    row += 1
    col += 1
    print(game.board_matrix())
    if(not game.check_move(row,col)):
        tk.messagebox.showinfo(window,"Info","Already placed move")
        
    if(button['text'] == " " and game.check_move(row,col)):
        button['text'] = game.current_player
        game.add_move(row,col)
        game.turn +=1
        if game.check_win():
            tk.messagebox.showinfo("Win game","Player " + game.current_player + " has won!")
            game.reset_game()
            reset_board()
            
        game.current_player = game.swap_players()

    if game.turn == 9 :
        tk.messagebox.showinfo("Draw game","It is a draw")
        game.reset_game()
        reset_board()

def create_board():

    """
    create_board generates the board in the UI.
    
    Parameters
    ----------
    window: is the root of the UI, used to add sub-elements in it
    game: object of type Tris used to implement the game logic

    """ 
    window.geometry("400x500")
    window.minsize(400,500)
    window.maxsize(400,500)
    window.config(bg='black')
    frame_title = tk.Frame(window)
    frame_grid = tk.Frame(window)
    frame_label = tk.Frame(window)
    
    title = tk.Label(frame_title,text= " WELCOME TO TRIS ",font=('Segoe Script',20),bg="black",fg="white",justify="left")
    label = tk.Label(frame_label,text = " It is Player {} turn ".format(game.current_player),font=('Helvetica',20),bg="black",fg="white")
    label.pack()
    title.pack()

    frame_title.pack(padx=10,pady=10)
    frame_grid.pack(padx=1,pady=1)
    frame_label.pack(padx=10,pady=10)

    b1 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b1,label))
    b2 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b2,label))       
    b3 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b3,label))
    b4 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b4,label))
    b5 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b5,label))
    b6 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b6,label))
    b7 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b7,label))
    b8 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b8,label))
    b9 = tk.Button(frame_grid,text=" ",font=('Segoe Script',20,"bold"),height=2,width=6,bg="#500550",fg="white",command = lambda: b_click(b9,label))
    
    
    
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    
def reset_board():
    
    for b in window.winfo_children()[1].winfo_children():
        b['text'] = " "

    
def start_game():

    create_board()
    
    window.title('Tris')
    window.iconbitmap("C:/Users/Francesco/Downloads/tic-tac-toe.ico")
  

    window.mainloop()






class Tris:

   """
    A class used to represent Tris game

    ...

    Attributes
    ----------
    board : np.array
        A numpy array to store the game internal state
    turn : int
        An integer counting the total turns performed in the game
    current_player : str
        A string storing the current player of a turn

    Methods
    -------
    __init__():
        Object constructor
        
    starting_player():
        ...
    check_move(row,col):
        ...
        
    ...
   """

   def __init__(self):
        self.board = np.array([["-","-","-"],
                               ["-","-","-"],
                               ["-","-","-"]])
        
        self.turn = 0
        
        self.current_player = self.starting_player()
        
   def starting_player(self):
        
        return random.choice(["X","O"])
   
   def check_move(self,row,col):
           
        if (row < 1 or row > 3) or (col < 1 or col > 3):
                return False
        elif(self.board[row-1][col-1] != "-"):
                return False
        else:
                return True
            
   def check_win(self):
        
        if all(x == self.current_player for x in self.board[0]):
            return True
        if all(x == self.current_player for x in self.board[1]):
            return True
        if all(x == self.current_player for x in self.board[2]):
          return True  
        if all(x == self.current_player for x in self.board[:,0]):
            return True
        if all(x == self.current_player for x in self.board[:,1]):
            return True
        if all(x == self.current_player for x in self.board[:,2]):
            return True
        
        diag1 = [self.board[0,0],self.board[1,1],self.board[2,2]]
        diag2 = [self.board[0,2],self.board[1,1],self.board[2,0]]

        if all(x == self.current_player for x in diag1):
            return True
        if all(x == self.current_player for x in diag2):
            return True
        return False
    
   def swap_players(self):
        
        return "X" if self.current_player == "O" else "O"
    
   def add_move(self,row,col):
        
        self.board[row-1][col-1] = self.current_player
        
   def board_matrix(self):
        
        for row in self.board:
            for val in row:   
                print('{:4}'.format(val),end='')
            print()
   
   def reset_game(self):

        self.board = np.array([["-","-","-"],
                               ["-","-","-"],
                               ["-","-","-"]])
        self.turn = 0
        
        self.current_player = self.starting_player()
            
if __name__ == "__main__":
    game = Tris()
    window = tk.Tk()
    start_game()   
     

               