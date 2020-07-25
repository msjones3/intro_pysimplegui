import PySimpleGUI as PSG

rows = [
    [PSG.Text("Welcome")],
    [PSG.ReadFormButton("Click me")]
]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

button, value = form.Read()

