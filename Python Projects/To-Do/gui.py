import functions
import PySimpleGUI as sg

# the argument must be a string
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add_button = sg.Button("Add")

# window is the mother instance that contains the objects
# first arg is app title. layout gets a list of object instances (buttons, text boxes, etc).
# in layout, inner square brackets list(s) is a row, thus put in separate lists for separate rows
window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])

# this displays the window on the screen
window.read()
# at this point, the program holds open til closing. So here is where we will add certain commands.
window.close()
