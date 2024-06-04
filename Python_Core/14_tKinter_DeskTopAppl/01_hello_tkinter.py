# tKinter is the standard GUI library for python
# tKinter allows to create dialogs - - windows Desk Top application
# Create the application
# widgets - button, labels....
# pack the widgets to the window
# start the application
# Boiler plate code

import tkinter as tk
# Create the application
window = tk.Tk()
window.minsize(500,400)
window.title("Simple TKinter application")

# widgets
label = tk.Label(window, text="Message Display here", font=("Helvetica",16))
serial = 1
def set_message():
# global variable defined
    global serial
    label["text"] = f"Hello world! ({serial})"
    serial +=1

button = tk.Button(window, text="Submit", command=set_message,font=("Helvetica",16))

# pack the widgets to the window
label.pack(pady=20)
button.pack(pady=20)

# start the application
window.mainloop()
