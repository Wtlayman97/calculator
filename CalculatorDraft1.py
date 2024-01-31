import tkinter as tk
window = tk.Tk()
button_values = ["7", "8", "9",
                 "4", "5", "6",
                 "1", "2", "3",
                 "0", "=", "C",
                 "+", "-", "*", "\u00F7"]
number_buttons = []
x = 1
y = 1
j = 0
for u in button_values[:10]:
    number_buttons.append(int(u))
    number_buttons[j] = tk.Button(text = f'{u}').grid(row = x, column = y)
    if y < 3:
        y+=1
    else:
        y = 1
        x+=1
    j+=1
    
for i in button_values[10:]:
    if i == "+":
        addButton = tk.Button(window, text = i)
        addButton.grid(column = 4, row = 1, rowspan = 3)
    elif i == "-":
        subtButton = tk.Button(window, text = i)
        subtButton.grid(column = 4, row = 4)
    elif i == "*":
        multButton = tk.Button(window, text = i)
        multButton.grid(column = 7, row = 7)
    elif i == "\u00F7":
        divButton = tk.Button(window, text = i)
        divButton.grid(column = 4, row = 3)
    elif i == "=":
        executeButton = tk.Button(window, text = i)
        executeButton.grid(column = 4, row = 5)
    elif i == "C":
        clearButton = tk.Button(window, text = i)
        clearButton.grid(column = 0, row =0)
            
window.mainloop()