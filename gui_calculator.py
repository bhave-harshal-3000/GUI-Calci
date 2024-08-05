import tkinter as tk

root = tk.Tk()
root.title("gui calculator")

entry = tk.Entry(root, width=25, font=('Arial', 24), borderwidth=1, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

def click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            current_text=current_text.replace("^","**")
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
       
        entry.delete(0, tk.END)
    else:
       
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + button_text)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    '(',')','%','^'
]


row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=7, height=3, command=lambda t=button_text: click(t))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
