# Tic Tac Toe game using tkinter
import random

# Importing modules
from tkinter import *
import tkinter.messagebox

# Window defined
root = Tk()

root.title('Tic-Tac-Toe')

root.resizable(False, False)

click = False

# Count variable to check the no. of turns
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

# Array to help the computer make the next move
board = [''] * 10

xPhoto = PhotoImage(file='X.png')
oPhoto = PhotoImage(file='O.png')


# Grid buttons
def start():

    button1 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn1,
                     command=lambda: press(1, 0, 0))
    button1.grid(row=0, column=0)

    button2 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn2,
                     command=lambda: press(2, 0, 1))
    button2.grid(row=0, column=1)

    button3 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn3,
                     command=lambda: press(3, 0, 2))
    button3.grid(row=0, column=2)

    button4 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn4,
                     command=lambda: press(4, 1, 0))
    button4.grid(row=1, column=0)

    button5 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn5,
                     command=lambda: press(5, 1, 1))
    button5.grid(row=1, column=1)

    button6 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn6,
                     command=lambda: press(6, 1, 2))
    button6.grid(row=1, column=2)

    button7 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn7,
                     command=lambda: press(7, 2, 0))
    button7.grid(row=2, column=0)

    button8 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn8,
                     command=lambda: press(8, 2, 1))
    button8.grid(row=2, column=1)

    button9 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn9,
                     command=lambda: press(9, 2, 2))
    button9.grid(row=2, column=2)

# Computer always starts first and picks a random corner
    rand = random.choice([1,3,7,9])
    if rand == 1:
        press(1,0,0)
    elif rand == 3:
        press(3,0,2)
    elif rand == 7:
        press(7,2,0)
    else:
        press(9,2,2)

# Checks if one wins the game from using the array values. Array values are hypothetical for a computer to use to avoid losing.
def checkWinAI():
    if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O' or
            board[4] == 'O' and board[5] == 'O' and board[6] == 'O' or
            board[7] == 'O' and board[8] == 'O' and board[9] == 'O' or
            board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or
            board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or
            board[3] == 'O' and board[6] == 'O' and board[9] == 'O' or
            board[1] == 'O' and board[5] == 'O' and board[9] == 'O' or
            board[3] == 'O' and board[5] == 'O' and board[7] == 'O' or
            board[1] == 'X' and board[2] == 'X' and board[3] == 'X' or
            board[4] == 'X' and board[5] == 'X' and board[6] == 'X' or
            board[7] == 'X' and board[8] == 'X' and board[9] == 'X' or
            board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or
            board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or
            board[3] == 'X' and board[6] == 'X' and board[9] == 'X' or
            board[1] == 'X' and board[5] == 'X' and board[9] == 'X' or
            board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        return True
    else:
        return False

# Computer prevents the user from winning in their next turn by blocking their winning slot.
def block_win():
    global board
    possible_moves = [x for x, letter in enumerate(board) if letter == '' and x != 0]
    for letter in ['O', 'X']:
        for x in possible_moves:
            board[x] = letter
            if checkWinAI():
                if x == 1:
                    press(1, 0, 0)
                    return
                elif x == 2:
                    press(2, 0, 1)
                    return
                elif x == 3:
                    press(3, 0, 2)
                    return
                elif x == 4:
                    press(4, 1, 0)
                    return
                elif x == 5:
                    press(5, 1, 1)
                    return
                elif x == 6:
                    press(6, 1, 2)
                    return
                elif x == 7:
                    press(7, 2, 0)
                    return
                elif x == 8:
                    press(8, 2, 1)
                    return
                else:
                    press(9, 2, 2)
                    return
            else:
                board[x] = ''

# If block_win returns and computer hasn't moved yet, then it picks one of the available corners to move.
def check_corner():

    global board
    open_corners = []
    possible_moves = [x for x, letter in enumerate(board) if letter == '' and x != 0]
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)

    if len(open_corners) > 0:
        corner = random.choice(open_corners)
        print(possible_moves)
        print(corner)

        if corner == 1:
            press(1, 0, 0)
        elif corner == 3:
            press(3, 0, 2)
        elif corner == 7:
            press(7, 2, 0)
        else:
            press(9, 2, 2)
        print(board)

# Computer's turn
def comp_move():
    block_win()
    if not click:
        check_corner()

# Changing the value of button and gives the move to the opponent
def press(num, r, c):
    global click, count, board
    if click:
        labelPhoto = Label(root, image=xPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('X')
            board[1] = 'X'
        elif num == 2:
            btn2.set('X')
            board[2] = 'X'
        elif num == 3:
            btn3.set('X')
            board[3] = 'X'
        elif num == 4:
            btn4.set('X')
            board[4] = 'X'
        elif num == 5:
            btn5.set('X')
            board[5] = 'X'
        elif num == 6:
            btn6.set('X')
            board[6] = 'X'
        elif num == 7:
            btn7.set('X')
            board[7] = 'X'
        elif num == 8:
            btn8.set('X')
            board[8] = 'X'
        else:
            btn9.set('X')
            board[9] = 'X'
        count += 1
        click = False
        checkWin()
        comp_move()

    else:
        labelPhoto = Label(root, image=oPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('O')
            board[1] = 'O'
        elif num == 2:
            btn2.set('O')
            board[2] = 'O'
        elif num == 3:
            btn3.set('O')
            board[3] = 'O'
        elif num == 4:
            btn4.set('O')
            board[4] = 'O'
        elif num == 5:
            btn5.set('O')
            board[5] = 'O'
        elif num == 6:
            btn6.set('O')
            board[6] = 'O'
        elif num == 7:
            btn7.set('O')
            board[7] = 'O'
        elif num == 8:
            btn8.set('O')
            board[8] = 'O'
        else:
            btn9.set('O')
            board[9] = 'O'
        count += 1
        click = True
        checkWin()


# Checks the winner
def checkWin():
    global count, click

    if (btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
            btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
            btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
            btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
            btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
            btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'X Wins !')
        click = False
        count = 0
        clear()
        start()

    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
          btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
          btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
          btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
          btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
          btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'O Wins !')
        click = False
        count = 0
        clear()
        start()

    elif count == 9:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Tie Game!')
        click = False
        count = 0
        clear()
        start()


# Clear the tiles after one wins or ties
def clear():
    global board
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    board = [''] * 10
    msg = tkinter.messagebox.askquestion('Message', 'Play Again?')
    if msg == 'no':
        root.quit()

start()
# Restarts the game if the user wishes so
root.mainloop()
