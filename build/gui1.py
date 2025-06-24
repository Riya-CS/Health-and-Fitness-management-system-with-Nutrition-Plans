#Nutrition Logs Page

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1536x817")
window.configure(bg = "#84A928")


canvas = Canvas(
    window,
    bg = "#84A928",
    height = 817,
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
    910.0,
    512.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    916.0,
    103.0,
    image=image_image_4
)

canvas.create_text(
    620.0,
    58.0,
    anchor="nw",
    text="NUTRITION LOGS",
    fill="#FFB001",
    font=("Otomanopee One", 64 * -1)
)

canvas.create_text(
    445.0,
    265.0,
    anchor="nw",
    text="Date",
    fill="#84A928",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    793.0,
    466.0,
    anchor="nw",
    text="Fats",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    433.0,
    329.0,
    anchor="nw",
    text="Meal",
    fill="#84A928",
    font=("Otomanopee One", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    799.0,
    292.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=715.5,
    y=265.0,
    width=167.0,
    height=53.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    737.0,
    493.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFB001",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=718.5,
    y=466.0,
    width=37.0,
    height=53.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    969.5,
    494.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFB001",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=952.0,
    y=466.0,
    width=35.0,
    height=54.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1001.5,
    356.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=715.5,
    y=329.0,
    width=572.0,
    height=53.0
)

canvas.create_text(
    433.0,
    395.0,
    anchor="nw",
    text="Calories",
    fill="#84A928",
    font=("Otomanopee One", 36 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    799.0,
    420.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#B2D658",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=715.5,
    y=393.0,
    width=167.0,
    height=53.0
)

canvas.create_text(
    445.0,
    466.0,
    anchor="nw",
    text="Proteins",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    970.0,
    465.0,
    anchor="nw",
    text="Carbs",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1239.5,
    488.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFB001",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=1222.0,
    y=460.0,
    width=35.0,
    height=54.0
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
    x=1315.0,
    y=448.0,
    width=83.0,
    height=84.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    915.0,
    654.0,
    image=image_image_5
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
    x=85.0,
    y=20.0,
    width=180.0,
    height=188.51348876953125
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    178.0,
    515.0,
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
    x=70.769287109375,
    y=340.84423828125,
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
    x=70.769287109375,
    y=423.3134765625,
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
    x=70.769287109375,
    y=596.984375,
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
    x=70.769287109375,
    y=261.285400390625,
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
    x=70.769287109375,
    y=507.723388671875,
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
    x=71.0,
    y=687.0,
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
    x=178.0,
    y=687.0,
    width=95.0,
    height=88.0
)
window.resizable(True, True)
window.mainloop()
