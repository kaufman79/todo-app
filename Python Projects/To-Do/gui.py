import functions
import PySimpleGUI as sg

# stuff related to adding a to_do
label = sg.Text("Type in a to-do") # the argument must be a string
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")

# existing to_do stuff
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=False, size=[45,10])
edit_button = sg.Button("Edit")


layout = [
            [label],
            [input_box, add_button],
            [list_box, edit_button]
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
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n" # this gives us the value of the key to_do, assigning it to a var
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
