import random
import time
from tkinter import Tk, Button, PhotoImage

# Function to display the symbol when a button is clicked
def show_image(x, y):
    global first, previousX, previousY

    # Show the symbol on the button
    buttons[x, y].config(image=button_images[x, y])
    buttons[x, y].update_idletasks()

    if first:
        # Store the coordinates of the first clicked button
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        # Check if the second button clicked is different from the first one
        if button_images[previousX, previousY] != button_images[x, y]:
            # If symbols don't match, wait for a moment and then hide both symbols
            time.sleep(0.5)
            buttons[previousX, previousY].config(image=default_image)
            buttons[x, y].config(image=default_image)
        else:
            # If symbols match, disable the buttons
            buttons[previousX, previousY].config(state="disabled")
            buttons[x, y].config(state="disabled")
        first = True

# Initialize the main window
root = Tk()
root.title("Memory Match Game")
root.geometry("800x800")
root.resizable(width=False, height=False)

# Initialize game variables
buttons = {}
button_images = {}
first = True
previousX = previousY = None

# Load images with error handling
try:
    default_image = PhotoImage(file="default.png")
    images = [PhotoImage(file=f"img{i}.png") for i in range(1, 19)]
    images *= 2  # Double the images for pairs
    random.shuffle(images)
except Exception as e:
    print(f"Error loading images: {e}")
    root.destroy()
    exit()

# Create buttons and assign images
for x in range(6):
    for y in range(6):
        button = Button(
            root,
            width=100,
            height=100,
            image=default_image,
            bg="black",  # Set background color to black
            command=lambda x=x, y=y: show_image(x, y)
        )
        button.grid(row=x, column=y, padx=5, pady=5)
        buttons[x, y] = button
        button_images[x, y] = images.pop()

# Start the Tkinter event loop
root.mainloop()
