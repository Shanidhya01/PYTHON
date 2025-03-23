"""
A simple game where the player has to catch eggs with a catcher.
"""

from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

# Game constants
canvas_width = 500
canvas_height = 600
root = Tk()
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue')

# Create the game elements
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

# Egg constants
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.9

# Catcher constants
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

# Create the catcher
catcher = c.create_arc(catcher_start_x, catcher_start_y,
                        catcher_start_x2, catcher_start_y2, start=200, extent=140,
                        style='arc', outline=catcher_color, width=3)

# Create the font
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)

# Initialize the score
score = 0
score_text = c.create_text(10, 10, anchor='nw', font=game_font, fill='darkblue', text='Score: ' + str(score))

# Initialize lives
lives_remaining = 3
lives_text = c.create_text(canvas_width - 10, 10, anchor='ne', font=game_font, fill='darkblue',
                            text='Lives: ' + str(lives_remaining))

# Initialize eggs
eggs = []

def create_egg():
    """
    Create a new egg.
    """
    x = randrange(10, canvas_width - egg_width - 10)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    """
    Move all eggs faster.
    """
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 15)  # Eggs fall faster
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(max(100, egg_speed - 50), move_eggs)  # Speed increases over time

def egg_dropped(egg):
    """
    Drop an egg.
    """
    if egg in eggs:
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('Game Over!', 'Final Score: ' + str(score))
        root.destroy()

def lose_a_life():
    """
    Lose a life.
    """
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))

def check_catch():
    """
    Check if an egg has been caught.
    """
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs[:]:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    """
    Increase the score and make the game harder by increasing egg speed.
    """
    global score, egg_speed, egg_interval
    score += points
    egg_speed = max(100, int(egg_speed * difficulty_factor))
    egg_interval = max(500, int(egg_interval * difficulty_factor))
    c.itemconfigure(score_text, text='Score: ' + str(score))

def move_left(event):
    """
    Move the catcher to the left.
    """
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    """
    Move the catcher to the right.
    """
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

# Bind keys to movement
c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()

# Start the game
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)

root.mainloop()
