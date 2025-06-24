
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import mysql.connector
import pop_ups
import subprocess
from db_config import DB_CONFIG

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / "build/assets/frame01"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui1(username):
    script_path = OUTPUT_PATH / "User_dashboard.py"
    subprocess.Popen(['python', str(script_path), username])


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)
    canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, **kwargs)

def toggle_password():
    if entry_2.cget('show') == '*':
        entry_2.config(show='')  
    else:
        entry_2.config(show='*')  

def check_username_exists(username):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM user WHERE username = %s", (username.lower(),))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def validate_login():
    username = entry_1.get()
    password = entry_2.get()
    
    if check_username_exists(username):
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM user WHERE username = %s", (username.lower(),))
        stored_password = cursor.fetchone()
        conn.close()
        
        if stored_password and stored_password[0] == password and password!="":
            pop_ups.popup_message("Login Successful", "Welcome!")
            open_gui1(username)
        else:
            pop_ups.popup_message("Incorrect password!")
    else:
        pop_ups.popup_message("Username does not exist!")

window = Tk()
window.geometry("1536x864")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=864, width=1536, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(720.0, 512.0, image=image_image_1)

canvas.create_rectangle(768.0, 0, 1548.0, 1316.0, fill="#E7F2D6", outline="")

create_rounded_rectangle(canvas, 897.0, 214.0, 1418.0, 652.0, radius=30, fill="#82BBB5", outline="")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#E7F2D6"
).place(x=962.0, y=55.0, width=392.0, height=98.4)

canvas.create_text(927.0, 302.0, anchor="nw", text="Username:", fill="#E7F2D6", font=("Merriweather Bold", 36 * -1))
canvas.create_text(927.0, 446.0, anchor="nw", text="Password:", fill="#E7F2D6", font=("Merriweather Bold", 36 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(1158.0, 386.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, font=("Merriweather", 26))
entry_1.place(x=937.0, y=347.0, width=442.0, height=76.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(1158.0, 530.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, font=("Merriweather", 26), show='*')
entry_2.place(x=937.0, y=491.0, width=442.0, height=76.0)

eye_icon = PhotoImage(file=relative_to_assets("image_2.png"))
peek_button = Button(
    image=eye_icon,
    command=toggle_password,
    relief="flat",
    bg="#82BBB5",
    borderwidth=0,
    highlightthickness=0
)
peek_button.place(x=1100, y=455)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=validate_login,
    relief="flat",
    bg="#E7F2D6"
).place(x=1028.0, y=696.0, width=260.0, height=77.0)



window.resizable(False, False)
window.mainloop()
