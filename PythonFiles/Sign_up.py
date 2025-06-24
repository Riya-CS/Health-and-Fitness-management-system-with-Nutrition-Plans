import mysql.connector
import re
from datetime import datetime
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import pop_ups
import subprocess
from db_config import DB_CONFIG


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / 'build/assets/frame02'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui1():
    script_path = OUTPUT_PATH / "Start_page.py"
    subprocess.Popen(['python', str(script_path)])
    window.after(000, window.destroy)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)
    canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, **kwargs)

def insert_user(username, email, password, registration_date):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO User (username, email, password,registrationdate )
    VALUES (%s, %s, %s, %s)
    """, (username,email, password,registration_date ))
    conn.commit() 
    conn.close()
 


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def is_valid_username(username):
    username_regex = r'^[a-zA-Z0-9_]+$'
    return re.match(username_regex, username)

def is_valid_password(password):
    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(password_regex, password)

def check_username_exists(username):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM user WHERE username = %s", (username.lower(),))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def sign_up():
    username = entry_1.get()
    email = entry_4.get()
    password = entry_2.get()
    confirm_password = entry_3.get()
    registration_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD
    
    

    
    if not is_valid_username(username):
        pop_ups.popup_message("Username can only contain\nalphanumeric characters and underscores!")
        return

    
    if check_username_exists(username):
        pop_ups.popup_message("Username already exists!")
        return

    
    if not is_valid_email(email):
        pop_ups.popup_message("Invalid email format!")
        return

    
    if not is_valid_password(password):
        pop_ups.popup_message("Password must be at least 8 characters long\nand contain both letters and numbers!")
        return

   
    if password != confirm_password:
        pop_ups.popup_message("Passwords do not match!")
        return
    registration_date=datetime.now().date()
   
    insert_user(username, email, password, registration_date)
    pop_ups.popup_message("Registration successful!")  # Confirmation message on successful registration
    open_gui1()
    

# Initialize main window
window = Tk()
window.geometry("1536x864")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=864,
    width=1536,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(720.0, 512.0, image=image_image_1)

canvas.create_rectangle(768.0, 0, 1548.0, 1316.0, fill="#E7F2D6", outline="")
create_rounded_rectangle(canvas, 897.0, 177.0, 1418.0, 713.0, radius=30, fill="#82BBB5", outline="")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"), 
    relief="flat",
    bg="#E7F2D6"
)
button_1.place(x=962.0, y=55.0, width=392.0, height=98.39810180664062)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up, 
    relief="flat",
    bg="#E7F2D6"
)
button_2.place(x=1028.0, y=737.0, width=259.984375, height=77.0)

canvas.create_text(927.0, 214.0, anchor="nw", text="Username:", fill="#E7F2D6", font=("Merriweather Bold", 32 * -1))
canvas.create_text(925.0, 333.0, anchor="nw", text="Email:", fill="#E7F2D6", font=("Merriweather Bold", 32 * -1))
canvas.create_text(925.0, 559.0, anchor="nw", text="Confirm Password:", fill="#E7F2D6", font=("Merriweather Bold", 32 * -1))
canvas.create_text(925.0, 446.0, anchor="nw", text="Password:", fill="#E7F2D6", font=("Merriweather Bold", 32 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(1156.0, 293.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, font=("Merriweather", 26))
entry_1.place(x=935.0, y=259.0, width=442.0, height=66.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(1156.0, 519.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, show="*", font=("Merriweather", 26))
entry_2.place(x=935.0, y=485.0, width=442.0, height=66.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(1156.0, 632.0, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, show="*", font=("Merriweather", 26))  
entry_3.place(x=935.0, y=598.0, width=442.0, height=66.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(1156.0, 406.0, image=entry_image_4)
entry_4 = Entry(bd=0, bg="#E7F2D6", fg="#000716", highlightthickness=0, font=("Merriweather", 26))  
entry_4.place(x=935.0, y=372.0, width=442.0, height=66.0)

eye_open_icon = PhotoImage(file=relative_to_assets("image_2.png"))

def toggle_password(entry_field, state):
    if state[0]:  #
        entry_field.config(show="*")
    else:
        entry_field.config(show="")
    state[0] = not state[0] 

show_password1 = [False]
show_password2 = [False]

eye_button_1 = Button(image=eye_open_icon, command=lambda: toggle_password(entry_2, show_password1),
                      borderwidth=0, bg="#82BBB5", relief="flat")
eye_button_1.place(x=1077, y=450, width=30, height=30)

eye_button_2 = Button(image=eye_open_icon, command=lambda: toggle_password(entry_3, show_password2),
                      borderwidth=0, bg="#82BBB5", relief="flat")
eye_button_2.place(x=1200, y=565, width=30, height=30)


window.resizable(False, False)
window.mainloop()

