import tkinter as tk #tk- interface(GUI library)

def set_tile(row, column):
    global current_player

    if(game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player #mark the board

    if current_player == playerO: #switch player
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player + "'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns +=1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"]==board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground = color_yellow, background=color_light_gray)
            game_over = True
            return
        
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"]==board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground = color_yellow, background=color_light_gray)
            game_over = True
            return 
        
    #diagonally
    if(board[0][0]["text"]==board[1][1]["text"] == board [2][2]["text"]
       and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background = color_light_gray)
        game_over = True
        return
    
    #anti-diagonally
    if(board[0][2]["text"]==board[1][1]["text"] == board [2][0]["text"]
       and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background = color_light_gray)
        board[1][1].config(foreground=color_yellow, background = color_light_gray)
        board[2][0].config(foreground=color_yellow, background = color_light_gray)
        game_over = True
        return
    
    #tie condition
    if (turns == 9):
        game_over = True
        label.config(text = "Tie!", foreground=color_yellow)
    
def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    label.config(text=current_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text = "", foreground= color_blue, background = color_gray)

#Game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0 ,0],
         [0, 0 ,0],
         [0, 0, 0]]

color_blue  = "#9370DB"
color_yellow = "#FFA500"
color_gray = "#D0F0C0"
color_light_gray = "#FFE4E1"

turns = 0
game_over = False

#window setup
window = tk.Tk() # Create the game window
window.title("Tic-Tac-Toe") 
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text = current_player+"'s Turn", font = ("Consolas", 20), background=color_gray,
                 foreground="white")
label.grid(row = 0, column= 0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text ="", font =("Consolas", 50, "bold"),
                                       background=color_gray, foreground=color_blue, width=4, height=1,
                                       command=lambda row=row, column=column:set_tile(row, column))
                                       
        board[row][column].grid(row=row+1, column = column)

button = tk.Button(frame, text="Restart", font = ("Consolas", 20), background=color_gray,
                   foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_heigth/2) - (window_height/2))

#format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()  #keeps the window actibeactive until the user closes it
