import tkinter as tk
import math
def button_click(value):
    global result, numberPressA, operatorPress
    if value == "C":
        entry_text.set("")
    elif value == "\u00B2":
        number = float((entry_text.get()))
        result = number**2
        entry_text.set(str(result))
    elif value in operators:
        numberPressA = entry_text.get()
        operatorPress = value
        entry_text.set("")
    elif result is not None:
        numberPressA = result
        result = None
    elif value == "\u221A":
        number = float((entry_text.get()))
        result = math.sqrt(number)
        entry_text.set(result)
    elif value == "=":
        try:
            expression = f"{numberPressA}{operatorPress}{entry_text.get()}"
            result = eval(expression)
            entry_text.set(str(result))
        except Exception as e:
            entry_text.set("Error: Press C and try again.")
    else:
        entryField.insert(tk.END, value)
window = tk.Tk()
window.title("Calculator")
button_values = ["7", "8", "9",
                 "4", "5", "6",
                 "1", "2", "3",
                 "0", "=", "C",
                 "+", "-", "*", "\u00F7"]
button_style = {
    "font": ("Arial", 16),
    "width": 7,
    "height": 3,
    "bg": "white",
    "fg": "black",
    "bd": 3,
    "relief": "raised"
}
entry_style = {
    "font": ("Arial", 36),   
    "width": 14,
    "bg": "white",
    "fg": "black",
    "bd": 2
}
operators = ["+","-","*","/"]
calculation_completed=False
result=None
numberPressA=None
numberPressB=None
operatorPress=None
number_buttons = []
entry_text = tk.StringVar()
entryField = tk.Entry(window, textvariable = entry_text, **entry_style, justify='right')
entryField.grid(column = 1, row = 0, columnspan = 4)
x = 2
y = 1
j = 0
for u in button_values[:9]:
    number_buttons.append(int(u))
    number_buttons[j] = tk.Button(window, text = f'{u}', **button_style, command=lambda selection=int(u): button_click(selection))
    number_buttons[j].grid(row = x, column = y)
    if y < 3:
        y+=1
    else:
        y = 1
        x+=1
    j+=1
zero_button = tk.Button(window, text= f'{0}', **button_style, command=lambda selection = "0": button_click(selection)).grid(row = 5, column = 1, columnspan = 2)
deciButton = tk.Button(window, text=".", **button_style, command = lambda selection = ".": button_click(selection)).grid(row = 5, column = 3)
sqrtButton = tk.Button(window, text="\u221A" + "x", **button_style, command=lambda selection = "\u221A": button_click(selection)).grid(row = 1, column = 2)
squareButton = tk.Button(window, text = "x" + "\u00B2", **button_style, command=lambda selection = "\u00B2": button_click(selection)).grid(row = 1, column = 1)
for i in button_values[10:]:
    if i == "+":
        addButton = tk.Button(window, text = i, **button_style, command=lambda selection="+": button_click(selection))
        addButton.grid(column = 4, row = 4)
    elif i == "-":
        subtButton = tk.Button(window, text = i, **button_style, command=lambda selection="-": button_click(selection))
        subtButton.grid(column = 4, row = 3)
    elif i == "*":
        multButton = tk.Button(window, text = i, **button_style, command=lambda selection="*": button_click(selection))
        multButton.grid(column = 4, row = 2)
    elif i == "\u00F7":
        divButton = tk.Button(window, text = i, **button_style, command=lambda selection="/": button_click(selection))
        divButton.grid(column = 4, row = 1)
    elif i == "=":
        executeButton = tk.Button(window, text = i, **button_style, command=lambda selection="=": button_click(selection))
        executeButton.grid(column = 4, row = 5)
    elif i == "C":
        clearButton = tk.Button(window, text = i, **button_style, command = lambda selection="C": button_click(selection))
        clearButton.grid(column = 3, row =1)
            
window.geometry("400x530")
window.mainloop()