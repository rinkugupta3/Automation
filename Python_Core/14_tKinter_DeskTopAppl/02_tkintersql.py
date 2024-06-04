import tkinter as tk
import sqlite3
import maskpass


# create the database
conn = sqlite3.connect('students_av.db')

# cursor - enables to traverse along/over the data
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS student_table(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL)""")

def add_new_user():
    newUsername = username.get()
    newPassword = password.get()

    cur.execute("select * from student_table where username=?",(newUsername,))
    result = cur.fetchall()

    if result:
        feedback_label.config(text="Username already exists. Please choose another.")   
    
    else:
        cur.execute("INSERT INTO student_table(username,password) VALUES (?,?)",(newUsername,newPassword))
        conn.commit()
        print(f"Added user : {newUsername}")

        # clear the text boxes
        username.delete(0, tk.END)
        password.delete(0,tk.END)

        username.focus_set()



def pwd_display():
    global hide
    if hide:
        password.config(show="*")
    else:
        password.config(show=pwd)
    hide = not hide

hide = False

# Create the application(Widow )
window = tk.Tk()
window.minsize(500,400)
window.title("Log-in Tkinter app")

label1 = tk.Label(window, text="Enter Username: ")
label1.place(x=30, y= 40)
username = tk.Entry(text = "")
username.place(x=150, y = 40, width=200, height=25)

label2 = tk.Label(window, text="Enter Password: ")
label2.place(x=30, y= 80)
password = tk.Entry(text = "", show="*")
password.place(x=150, y = 80, width=200, height=25)
pwd = password.cget("text")

button = tk.Button(window, text="Submit",command=add_new_user )
button.place(x=200, y = 120, width=75, height=35)
buttonpwd = tk.Button(window, text="Display Password",command = pwd_display )
buttonpwd.place(x=200, y = 200, width=175, height=35)

#Create and place the feedback label
feedback_label = tk.Label(window, text="")
feedback_label.place(x=30, y= 160)


window.mainloop()