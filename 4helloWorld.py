import PySimpleGUI as PSG

message = PSG.Text("Welcome")

rows = [
            [message],
            [PSG.ReadFormButton("Click me")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

button, value = form.Read()

if button == "Click me":
    message.Update("Hello World")