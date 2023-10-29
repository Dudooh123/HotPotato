
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\b.possani\Desktop\interface hotpotato\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1250x720")
window.configure(bg = "#EEEDE8")


canvas = Canvas(
    window,
    bg = "#EEEDE8",
    height = 720,
    width = 1250,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    x=711.0,
    y=549.0,
    width=486.0,
    height=112.0
)

canvas.create_rectangle(
    711.0,
    382.0,
    1197.0,
    502.0,
    fill="#E11923",
    outline="")

canvas.create_rectangle(
    711.0,
    180.0,
    1197.0,
    300.0,
    fill="#E11923",
    outline="")

canvas.create_text(
    711.0,
    347.0,
    anchor="nw",
    text="Numero de rounds",
    fill="#000000",
    font=("RobotoRoman Bold", 32 * -1)
)

canvas.create_text(
    711.0,
    144.0,
    anchor="nw",
    text="Participante:",
    fill="#000000",
    font=("RobotoRoman Bold", 32 * -1)
)

canvas.create_rectangle(
    52.0,
    144.0,
    626.0,
    661.0,
    fill="#E11923",
    outline="")

canvas.create_text(
    433.0,
    41.0,
    anchor="nw",
    text="HOT POTATO",
    fill="#000000",
    font=("RobotoRoman Bold", 64 * -1)
)
window.resizable(False, False)
window.mainloop()
