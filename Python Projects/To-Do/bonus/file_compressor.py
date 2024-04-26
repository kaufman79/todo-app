import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key = "files") # this is a special button already programmed to select files

label2 = sg.Text("select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder") # this is a special button already programmed to browse files

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green") # empty instance for now. We will update it later in code.

layout = [
            [label1, input1, choose_button1],
            [label2, input2, choose_button2],
            [compress_button, output_label]
         ]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    dest_folder = values['folder']
    make_archive(filepaths, dest_folder)
    window["output"].update(value="Compression completed!") # we access the output key (part of our output label) and update it with a message

window.close()
