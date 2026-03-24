from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import random
import time

root = Tk()
root.geometry("520x666")
root.title("Memory Game!")
# Creates a frame to grid the buttons inside
button_frame = Frame(root)
button_frame.pack(pady = 60)

# Initializes helpful variables
score = 20
start_points = 20
count = 0
answer_list = []
answer_dict = {}
tot_matches = 0
back_color = "#2f2f2f"
display_color_names = True
display_incorrect_message = False
use_check_match = True
print_colors = False
start = time.time()

def reset_game(start_score = 20):
    global score, count, answer_list, answer_dict, tot_matches, all_colors, start, box_list, back_color, start_points
    # Reset global vars
    score = start_score
    start_points = start_score
    count = 0
    answer_list = []
    answer_dict = {}
    tot_matches = 0
    start = time.time()
    # Reset colors
    all_colors = ['white', 'white', 'black', 'black', 'red', 'red', 'green', 'green', 'blue', 'blue', 'cyan', 'cyan', 'yellow', 'yellow', 'magenta', 'magenta']
    random.shuffle(all_colors)
    # Reset score label
    score_label.config(text = ("Score: " + str(score)))
    # Reset buttons
    for button in box_list:
        button.config(text = " ", state = "normal", highlightbackground = back_color)
    check_button.config(state = "normal")

def change_score():
    print("Type in the number of points you want to start out with to reset the game with that as your starting points. Type 'quit' to prevent the game from resetting")
    new_score = input("New starting points: ")
    if new_score == 'quit':
        return
    elif new_score.isnumeric():
        reset_game(int(new_score))
    else:
        print('\nType only numbers please!\n')
        change_score()

def change_color():
    global back_color, box_list
    # Lets user pick a color
    colors = colorchooser.askcolor()
    # Changes backgrounds based on user input
    root.config(bg=colors[1])
    button_frame.config(background = colors[1])
    for box in box_list:
        box.config(background = colors[1])
        box.config(highlightbackground = colors[1])
    back_color = colors[1]

# Creates and shuffles list of all colors
all_colors = ['white', 'white', 'black', 'black', 'red', 'red', 'green', 'green', 'blue', 'blue', 'cyan', 'cyan', 'yellow', 'yellow', 'magenta', 'magenta']
random.shuffle(all_colors)

def button_click(box, num):
    global count, answer_list, answer_dict, tot_matches
    # Make a move if less than two have been made without checking matches
    if box["text"] == " " and count < 2:
        # Allow user to see text and visual for box color
        if display_color_names:
            box["text"] = all_colors[num]
        box["highlightbackground"] = all_colors[num]
        # Update answer list and dict with button and number
        answer_list.append(num)
        answer_dict[box] = all_colors[num]
        count += 1
        if print_colors:
            print(f"Color {count}: {all_colors[num]}")
        if not use_check_match:
            check_match()
        
            
def check_match():
    global score, count, answer_list, answer_dict, tot_matches
    if count == 2:
        if print_colors:
            print("---------------------------------------------")
        # Check for a match
        if all_colors[answer_list[0]] == all_colors[answer_list[1]]:
            # Disable matched buttons
            for button in answer_dict:
                button["state"] = "disabled"
            # Update global variables
            count = 0
            answer_list = []
            answer_dict = {}
            tot_matches += 2
            # Check game status
            if tot_matches == len(all_colors):
                win()
        else:            
            # Reset unmatched boxes
            for button in answer_dict:
                button["text"] = " "
                button["highlightbackground"] = back_color
            # Update global variables
            count = 0
            answer_list = []
            answer_dict = {}
            score -= 1
            score_label.config(text = ("Score: " + str(score)))
            # Check game status
            if score <= 0:
                return game_over()
            if display_incorrect_message:
                messagebox.showinfo("Wrong choice", "Sorry, those two weren't matches.")


def win():
    global box_list, start
    tot_time = round((time.time() - start))
    if start_points-score <= 4:
        messagebox.showinfo("Game Finished!", "Incredible Job! You only lost " + str(start_points-score) + " points and took " + str(tot_time) + " seconds!")
    else:
        messagebox.showinfo("Game Finished!", "Nice Job! You beat the game while losing " + str(start_points-score) + " points in " + str(tot_time) + " seconds!")
    # Updates boxes when user wins
    for button in box_list:
        button["text"] = "Matched!"
        button["background"] = "#ffd700"
        button["highlightbackground"] = "#ffd700"

def game_over():
    global box_list
    messagebox.showinfo("Game Over", "Oops! Better luck next time! You can play again by hitting reset in the options menu.")
    for button in box_list:
        button["state"] = "disabled"
    check_button.config(state = "disabled")

def change_color_names():
    global display_color_names
    display_color_names = not display_color_names

def change_incorrect_message():
    global display_incorrect_message
    display_incorrect_message = not display_incorrect_message

def change_print_colors():
    global print_colors
    print_colors = not print_colors

def change_check_match():
    global use_check_match
    use_check_match = not use_check_match


# Creates and grids all 16 buttons
box0 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box0, 0), relief = "groove")
box1 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box1, 1), relief = "groove")
box2 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box2, 2), relief = "groove")
box3 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box3, 3), relief = "groove")

box4 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box4, 4), relief = "groove")
box5 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box5, 5), relief = "groove")
box6 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box6, 6), relief = "groove")
box7 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box7, 7), relief = "groove")

box8 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box8, 8), relief = "groove")
box9 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box9, 9), relief = "groove")
box10 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box10, 10), relief = "groove")
box11 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box11, 11), relief = "groove")

box12 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box12, 12), relief = "groove")
box13 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box13, 13), relief = "groove")
box14 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box14, 14), relief = "groove")
box15 = Button(button_frame, text = " ", highlightbackground = None, highlightthickness = 6, disabledforeground = 'black', font = ('Helvetica', 16), height = 4, width = 5, command = lambda: button_click(box15, 15), relief = "groove")

box0.grid(row = 0, column = 0, padx=3, pady=3)
box1.grid(row = 1, column = 0, padx=3, pady=3)
box2.grid(row = 2, column = 0, padx=3, pady=3)
box3.grid(row = 3, column = 0, padx=3, pady=3)

box4.grid(row = 0, column = 1, padx=3, pady=3)
box5.grid(row = 1, column = 1, padx=3, pady=3)
box6.grid(row = 2, column = 1, padx=3, pady=3)
box7.grid(row = 3, column = 1, padx=3, pady=3)

box8.grid(row = 0, column = 2, padx=3, pady=3)
box9.grid(row = 1, column = 2, padx=3, pady=3)
box10.grid(row = 2, column = 2, padx=3, pady=3)
box11.grid(row = 3, column = 2, padx=3, pady=3)

box12.grid(row = 0, column = 3, padx=3, pady=3)
box13.grid(row = 1, column = 3, padx=3, pady=3)
box14.grid(row = 2, column = 3, padx=3, pady=3)
box15.grid(row = 3, column = 3, padx=3, pady=3)

# Creates a score label to display at the top of the screen
score_label = Label(text = ("Score: " + str(score)), background = 'gray', foreground = 'black', font = ('Helvetica', 20), height = 2, width = 22)
score_label.place(x = 0, y = 0)

# Creates a button to check matches at the top of the screen
check_button = Button(text = "Check match", background = 'gray', foreground = 'black', disabledforeground = 'black', font = ('Helvetica', 20), height = 2, width = 20, command = check_match, relief = "flat")
check_button.place(x = 245, y = 0)

# One more useful variable!
box_list = [box0, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15]


# Creates options menu
main_menu = Menu(root)
root.config(menu = main_menu)
optionsMenu = Menu(main_menu)
main_menu.add_cascade(label = "Options", menu = optionsMenu)
optionsMenu.add_command(label = "Start / Reset", command = reset_game)
optionsMenu.add_separator()
optionsMenu.add_command(label = "Change Starting Score (Check Terminal)", command = change_score)
optionsMenu.add_separator()
optionsMenu.add_command(label = "Change background color", command = change_color)
optionsMenu.add_separator()
optionsMenu.add_checkbutton(label = "Don't display color names (Hard Mode)", command = change_color_names)
optionsMenu.add_separator()
optionsMenu.add_checkbutton(label = "Display incorrect messages", command = change_incorrect_message)
optionsMenu.add_separator()
optionsMenu.add_checkbutton(label = "Print colors to terminal (Easy Mode)", command = change_print_colors)
optionsMenu.add_separator()
optionsMenu.add_checkbutton(label = "Don't require check match button (Only displays first color)", command = change_check_match)
optionsMenu.add_separator()
optionsMenu.add_command(label = "Exit Game", command = root.quit)


root.mainloop()