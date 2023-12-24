import PySimpleGUI as sg
import functions

sg.theme("Black")

label1 = sg.Text("Enter feet: ")
input_text1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches: ")
input_text2 = sg.Input(key="inches")
button = sg.Button("Convert")
label3 = sg.Text("", key="result")
button2 = sg.Button("Exit")
window = sg.Window("Convertor",
                   layout=[[label1, input_text1],
                           [label2, input_text2],
                           [button, button2, label3]])
while True:
    event, values = window.read()
    value_feet = float(values['feet'])
    value_inches = float(values['inches'])

    value_meter = functions.meter_converter(value_feet, value_inches)
    window['result'].update(value=f"{value_meter} m", text_color="red")

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

print("done")
window.close()