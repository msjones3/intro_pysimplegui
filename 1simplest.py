import PySimpleGUI

rows = [
    [PySimpleGUI.Text("Welcome")],
    [PySimpleGUI.ReadFormButton("Click me")]

]

form = PySimpleGUI.FlexForm("This is a form.")
form.Layout(rows)

button, value = form.Read()