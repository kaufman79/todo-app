import PySimpleGUI as sg

# the argument for the Text type must be a string
label_feet = sg.Text("Enter feet: ")
label_inches = sg.Text("Enter inches: ")
input_box_feet = sg.InputText()
input_box_inches = sg.InputText()
convert_button = sg.Button("Convert")

layout = [
            [label_feet, input_box_feet],
            [label_inches, input_box_inches],
            [convert_button]
         ]

# window is the mother instance that contains the objects
# first arg is app title. layout gets a list of object instances (buttons, text boxes, etc).
# in layout, inner square brackets list(s) is a row, thus put in separate lists for separate rows.
# I used the cookbook for a different way to make the layout (defined above as a variable, input here)
window = sg.Window("Metric Conversion app", layout)

# this displays the window on the screen
window.read()
# at this point, the program holds open til closing. So here is where we will add certain commands.
window.close()
