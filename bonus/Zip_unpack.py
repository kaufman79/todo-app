import PySimpleGUI as sg
import zip_extract_backend as ZEB

label1 = sg.Text("select archive:", size=(15, 1))
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("select destination:", size=(15, 1))
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output")

layout = [
            [label1, input1, choose_button1],
            [label2, input2, choose_button2],
            [extract_button, output_label]
         ]

window = sg.Window("Archive Extractor", layout)

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    ZEB.extract_archive(archivepath, dest_dir)
    window["output"].update(value="extraction completed!")

window.read()
window.close()