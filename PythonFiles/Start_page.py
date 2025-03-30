# Please change the file path accordingly

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\build\assets\frame0\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)
    canvas.create_oval(x1, y1, x1 + 2*radius, y1 + 2*radius, **kwargs)
    canvas.create_oval(x2 - 2*radius, y1, x2, y1 + 2*radius, **kwargs)
    canvas.create_oval(x1, y2 - 2*radius, x1 + 2*radius, y2, **kwargs)
    canvas.create_oval(x2 - 2*radius, y2 - 2*radius, x2, y2, **kwargs)

def open_gui1():
    subprocess.Popen(['python', r'C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\Log_in.py'])
    window.after(3000, window.destroy)  

def open_gui2():
    subprocess.Popen(['python', r'C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\Sign_up.py'])  # Adjust the command based on your environment
    window.after(3000, window.destroy)  
    
window = Tk()
window.geometry("1536x864")
window.configure(bg="#85D2D5")

canvas = Canvas(
    window,
    bg="#85D2D5",
    height=864,
    width=1536,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(768.0, 512.0, image=image_image_1)

create_rounded_rectangle(canvas, 487.0, 71.0, 1052.0, 794.0, radius=30, fill="#E7F2D6", outline="")

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(767.0, 329.0, image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui1,
    relief="flat",
    bg="#E7F2D6"
)
button_1.place(x=605.0, y=557.0, width=329.0, height=75.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
    relief="flat",
    bg="#E7F2D6"
)
button_2.place(x=604.0, y=677.0, width=329.0, height=75.0)

window.resizable(False, False)
window.mainloop()

#perfect
