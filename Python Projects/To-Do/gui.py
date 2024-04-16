import functions
import PySimpleGUI as sg

# the argument must be a string
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")


layout = [
            [label],
            [input_box, add_button],
         ]

# window is the mother instance that contains the objects
# first arg is app title. layout gets a list of object instances (buttons, text boxes, etc).
# in layout, inner square brackets list(s) is a row, thus put in separate lists for separate rows.
# I used the cookbook for a different way to make the layout (defined above as a variable, input here)
window = sg.Window("To-Do App", layout, font=('Helvetica', 20))

while True:
# window.read displays the window on the screen, and also returns events, i.e. the user clicking buttons and such
# attached to an event, it also returns a dictionary, with the key being 0 by default,
# or whatever we assign it to in the code for the input box above; the value is what the user entered.
    event, values = window.read() # yes, we can assign 2 vars to a list or tuple
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] # this gives us the value of the key to_do, assigning it to a var
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
