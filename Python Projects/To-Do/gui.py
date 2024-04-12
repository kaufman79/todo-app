import functions
import PySimpleGUI as sg

# the argument must be a string
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")

layout = [
            [label],
            [input_box, add_button]
         ]

# window is the mother instance that contains the objects
# first arg is app title. layout gets a list of object instances (buttons, text boxes, etc).
# in layout, inner square brackets list(s) is a row, thus put in separate lists for separate rows.
# I used the cookbook for a different way to make the layout (defined above as a variable, input here)
window = sg.Window("To-Do App", layout, font=('Helvetica', 20))

# window.read displays the window on the screen, and also returns events, i.e. the user clicking buttons and such
event = window.read()
print(event)
# at this point, the program holds open til closing. So here is where we will add certain commands.
window.close()
