# Projet calculatrice Ursina

# Imports
from ursina import *

app = Ursina()


"""
    Init values
"""

# Camera
camera.position = (1.5, 1.5)

# Window
window.forced_aspect_ratio = 4/3
window.exit_button.visible = False 
window.fps_counter.enabled = False
window.title = "Calculatrice"
window.borderless = False

schema = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "<", "=", "+"]
]

# Store all buttons in a table
calculatrice_board = [[None for i in range(4)] for i in range(4)]
debug_text = [[None for _ in range(4)] for _ in range(4)]

clicked = False
value = None

cur_equation = ""
res = False

for i in range(4):
    for j in range(4):
        case_btn = Button(parent=scene, text=schema[::-1][j][i], scale=0.8, position=(i, j))
        
        def on_click(b=case_btn):
            global clicked, value

            clicked = True
            value = b.text

        case_btn.on_click = on_click
        calculatrice_board[i][j] = case_btn

# Contenu de la zone de texte
user_input = Text(parent=scene, text="", color=color.light_gray, position=(0, 4), size=0.4, origin=(-0.5, 0.5))
warning = Text(parent=scene, text="", color=color.red, position=(0,4.5), size=0.5, origin=(-0.5, 0.5))
result = Text(parent=scene, text="", color=color.yellow, position=(0, -1), size=0.4)

# Check all event
def update():
    global clicked, value, cur_equation, res

    # Exit the app by pressing ESCAPE
    if held_keys['escape'] :
        quit()
    
    # Managing all input from the calculator
    if clicked :
        clicked = False
        if len(user_input.text) > 12 :
            warning.text = "Max size reached !"
        else :
            warning.text = ""
        
        match value :
            # Digits
            case "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9":

                if res:
                    result.text = ""

                if user_input.text == "...":
                    user_input.text = ""
                
                if warning.text == "" :
                    user_input.text += value
                    

            # Operators
            case "/" | "*" | "-" | "+":
                op = value

                for digit in user_input.text:
                    if digit in "0123456789":
                        res = False

                if res:
                    warning.text = "Enter a number !"

                elif cur_equation != "" :
                    if cur_equation[-1] in "/*-+" :
                        warning.text = "Enter a number !"

                else :
                    match op :
                        case "/":
                            cur_equation += f"{user_input.text}/"
                            user_input.text = "..."

                        case "*":
                            cur_equation += f"{user_input.text}*"
                            user_input.text = "..."

                        case "-":
                            cur_equation += f"{user_input.text}-"
                            user_input.text = "..."

                        case "+":
                            cur_equation += f"{user_input.text}+"
                            user_input.text = "..."
                    
                    if res :
                        res = False
                        result.text = ""

                    result.text += f"{cur_equation[0:-1]} {op}..."
            
            # Backspace
            case "<":
                if "." not in user_input.text:
                    user_input.text = user_input.text[0:-1]

                if user_input.text == "":
                    user_input.text = "..."

            # Result
            case "=":

                res = True

                result.text = f'{cur_equation + user_input.text} = {eval(cur_equation + user_input.text)}'

                user_input.text = ""
                cur_equation = ""


if __name__ == '__main__':
    # Run the application
    app.run()