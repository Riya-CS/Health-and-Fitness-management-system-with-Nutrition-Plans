from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1536x806")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    403.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    515.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    908.0,
    512.0,
    image=image_image_3
)

canvas.create_text(
    843.0,
    363.0,
    anchor="nw",
    text="Heart Rate                    BPM",
    fill="#3C98A4",
    font=("OtomanopeeOne Regular", 32 * -1)
)

canvas.create_text(
    843.0,
    273.0,
    anchor="nw",
    text="Blood Pressure              mmHg",
    fill="#3C98A4",
    font=("OtomanopeeOne Regular", 32 * -1)
)

canvas.create_text(
    440.0,
    273.0,
    anchor="nw",
    text="Height              cm                 ",
    fill="#3C98A4",
    font=("OtomanopeeOne Regular", 32 * -1)
)

canvas.create_text(
    440.0,
    363.0,
    anchor="nw",
    text="Weight              kg        ",
    fill="#3C98A4",
    font=("OtomanopeeOne Regular", 32 * -1)
)

canvas.create_text(
    440.0,
    443.0,
    anchor="nw",
    text="“this space here                              “      ",
    fill="#3C98A4",
    font=("OtomanopeeOne Regular", 32 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    908.0,
    115.0,
    image=image_image_4
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
    x=81.0,
    y=17.0,
    width=180.0,
    height=188.51348876953125
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    174.0,
    512.0,
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
    x=66.76922607421875,
    y=337.84423828125,
    width=214.46151733398438,
    height=72.76707458496094
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
    x=66.76922607421875,
    y=420.3134765625,
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
    x=66.76922607421875,
    y=593.984375,
    width=214.4615478515625,
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
    x=66.76922607421875,
    y=258.285400390625,
    width=214.46151733398438,
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
    x=66.76922607421875,
    y=504.723388671875,
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
    x=67.0,
    y=684.0,
    width=95.0,
    height=88.0
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
    x=174.0,
    y=684.0,
    width=95.0,
    height=88.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    656.5,
    294.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=612.5,
    y=267.0,
    width=88.0,
    height=53.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    656.5,
    390.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=612.5,
    y=363.0,
    width=88.0,
    height=53.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1206.5,
    294.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=1162.5,
    y=267.0,
    width=88.0,
    height=53.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1206.5,
    387.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=1162.5,
    y=360.0,
    width=88.0,
    height=53.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    908.0,
    636.0,
    image=image_image_6
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
    x=1319.0,
    y=422.0,
    width=83.0,
    height=84.0
)
window.resizable(True, True)
window.mainloop()
