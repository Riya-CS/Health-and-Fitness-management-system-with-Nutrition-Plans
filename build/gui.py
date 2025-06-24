#Nutrition Plans Page

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1536x806")
window.configure(bg = "#84A928")


canvas = Canvas(
    window,
    bg = "#84A928",
    height = 806,
    width = 1536,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    768.0,
    512.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    512.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    944.0,
    509.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    745.0,
    103.0,
    image=image_image_4
)

canvas.create_text(
    447.0,
    58.0,
    anchor="nw",
    text="NUTRITION PLAN",
    fill="#FFB001",
    font=("OtomanopeeOne Regular", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1116.0,
    y=27.0,
    width=379.0,
    height=152.0
)

canvas.create_text(
    507.0,
    281.0,
    anchor="nw",
    text="Age",
    fill="#84A928",
    font=("OtomanopeeOne Regular", 36 * -1)
)

canvas.create_text(
    1002.0,
    272.0,
    anchor="nw",
    text="Gender",
    fill="#84A928",
    font=("OtomanopeeOne Regular", 36 * -1)
)

canvas.create_text(
    474.0,
    336.0,
    anchor="nw",
    text="Meal type",
    fill="#84A928",
    font=("OtomanopeeOne Regular", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    768.0,
    300.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=744.0,
    y=267.0,
    width=48.0,
    height=64.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1306.0,
    300.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1282.0,
    y=267.0,
    width=48.0,
    height=64.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1075.0,
    374.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=744.0,
    y=341.0,
    width=662.0,
    height=65.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    941.0,
    584.0,
    image=image_image_5
)

canvas.create_text(
    490.0,
    455.0,
    anchor="nw",
    text="Your Meal Plan -",
    fill="#FFB001",
    font=("OtomanopeeOne Regular", 36 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=83.0,
    y=10.0,
    width=180.0,
    height=188.51348876953125
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    176.0,
    505.0,
    image=image_image_6
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=68.76922607421875,
    y=330.84423828125,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=68.76922607421875,
    y=413.3134765625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=68.76922607421875,
    y=586.984375,
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=68.76922607421875,
    y=251.285400390625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=68.76922607421875,
    y=497.723388671875,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=69.0,
    y=677.0,
    width=95.0,
    height=88.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=176.0,
    y=677.0,
    width=95.0,
    height=88.0
)
window.resizable(True, True)
window.mainloop()
