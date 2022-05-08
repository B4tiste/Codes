from html.entities import entitydefs
from multiprocessing import parent_process
from matplotlib.pyplot import text
from ursina import *
import random
import lib

"""
    Sorting algorithm visualizer
    - Bubble
    - Quick
    - Insertion
    - Merge
"""

if __name__ == "__main__":
    app = Ursina()

"""
    Init
"""

# Camera
camera.position = (1, 1)

# Window
window.exit_button.visible = False
window.fps_counter.enabled = False
window.title = "Sort Visualizer"
window.borderless = False
window.forced_aspect_ratio = 16/9

# Constants
TABLE_SIZE = 100
BORDERS = [0, 100]

# Init values
init_table = lib.createRandomTable(TABLE_SIZE, BORDERS)

# function

text_menu = [
    "Reset table",
    "Bubble sort",
    "Quick sort",
    "Insertion sort",
    "Merge sort"
]

menu = []

for i in range(len(text_menu)):
    menu_btn = Button(parent=scene, text=f'{i+1}', scale=1, position=(i-1, -2))
    menu.append(menu_btn)

# Reset button
menu[0].color = color.red

# Menu text
t = """
    1 - Reset
    2 - Bubble Sort
    3 - Quick Sort
    4 - Insertion Sort
    5 - Merge sort
"""
titles = Text(text=t, position=(0.8, -0.3))

test = Entity(parent=scene, model='cube', position=(-1, 0), scale=0.1)

# Create a quad for each element in the quad and display them as bar graph
for i in range(TABLE_SIZE):
    quad = Entity(parent=scene, model='quad', scale=0.1, position=(i, init_table[i]))
    quad.color = color.light_gray



def update():
    if held_keys['escape']:
        quit()

# Run the app
app.run()