import PySimpleGUI as sg
from metric_conversion_module import convert

sg.theme("Black")

# the argument for the Text type must be a string
label_feet = sg.Text("Enter feet: ")
input_box_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches: ")
input_box_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("", key="output")


layout = [
            [label_feet, input_box_feet],
            [label_inches, input_box_inches],
            [convert_button, exit_button, output_label]
         ]

# window is the mother instance that contains the objects
# first arg is app title. layout gets a list of object instances (buttons, text boxes, etc).
# in layout, inner square brackets list(s) is a row, thus put in separate lists for separate rows.
# I used the cookbook for a different way to make the layout (defined above as a variable, input here)
window = sg.Window("Metric Conversion app", layout)

while True:
    event, values = window.read()
    match event:
            case "Exit":
                break
            case sg.WIN_CLOSED:
                break
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])

        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="LightGreen")
    except ValueError:
        sg.Popup("Please provide two numbers", font=("Helvetica", 20))
# at this point, the program holds open til closing. So here is where we will add certain commands.
window.close()
