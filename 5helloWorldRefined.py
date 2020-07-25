import PySimpleGUI as PSG

message = PSG.Text("Welcome to PySimpleGUI")

rows = [
            [message],
            [PSG.ReadFormButton("Click me")],
            [PSG.ReadFormButton("Clear"), PSG.Cancel()]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()

    if button == "Click me":
        message.Update("Hello, World!")
    elif button == "Clear":
        message.Update("")

    else:
        break