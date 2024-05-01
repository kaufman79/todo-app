import PySimpleGUI as sg
from converters14 import convert

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(tooltip="feet", key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(tooltip="inches", key="inches")

button = sg.Button("Convert")
output = sg.Text(key="output")

layout = [
            [feet_label, feet_input],
            [inches_label, inches_input],
            [button, output]
         ]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read() # values will be a dictionary
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    conversion = convert(feet, inches)
    window["output"].update(value=f"{conversion} m", text_color="white")

window.close