import PySimpleGUI as sg

label1 = sg.Text("select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose") # this is a special button already programmed to select files

label2 = sg.Text("select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose") # this is a special button already programmed to browse files

compress_button = sg.Button("Compress")

layout = [
            [label1, input1, choose_button1],
            [label2, input2, choose_button2],
            [compress_button]
         ]

window = sg.Window("File Compressor", layout)

window.read()
window.close()
