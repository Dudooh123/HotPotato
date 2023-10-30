from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def jogo(participantes,tempo, nomes, slah):

    def lista_vazia(array):
        if not array:
            return None
        else:
            return array

    def enQueue(array, valor): 
        array.append(valor)
        return array


    def dequeue(array):
        if not array: 
            return None  
        return array.pop(0)


    def fila_circular(array,tempo):
        if len(array) < 2:
            print("--------------------")
        else:
            tempo = int(tempo)
            for event in range(tempo): 
                primeiro_elemento = array[0]
                array[0:-1] = array[1:]  
                array[-1] = primeiro_elemento  
        dequeue(array)
        return array


    on = True
    participantes = participantes
    while on:
        nome_participante = nomes
        participantes = enQueue(participantes, nome_participante) 
        participantes.pop()
        if slah == "1":
            print(" \n Vamos começar...")
            lista_vazia(participantes)
            while len(participantes) > 0:
                fila_circular(participantes, tempo)
                if len(participantes) > 1:
                    print(participantes)
                if len(participantes) == 1:
                    print(f"O vencedor foi {participantes[0]}")
                    on = False



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./interface atualizada/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1250x720")
window.configure(bg = "#EEEDE8")

participantes = []

def obter_texto_participantes_e_numero_jogadores():
    texto_participantes = entry_2.get()
    tempo = entry_1.get()
    nomes =  texto_participantes.split(",")
    participantes.extend(nomes)
    print("Texto na caixa de participantes:", participantes)
    print("Número de rounds:", tempo)
    #botar o comando para iniciar aqui
    jogo(participantes,tempo, nomes, slah="1")

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
    command=obter_texto_participantes_e_numero_jogadores,
    relief="flat"
)
button_1.place(
    x=711.0,
    y=549.0,
    width=486.0,
    height=112.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    954.0,
    442.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E11923",
    fg="#000716",
    highlightthickness=0,
    font=40
)
entry_1.place(
    x=711.0,
    y=382.0,
    width=486.0,
    height=118.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    954.0,
    240.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E11923",
    fg="#000716",
    highlightthickness=0,
    font=40
)
entry_2.place(
    x=711.0,
    y=180.0,
    width=486.0,
    height=118.0
)

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

canvas.create_rectangle(
    52.0,
    144.0,
    626.0,
    661.0,
    fill="#E11923",
    outline=""
)
output_text = Text(
    window,
    bd=0,
    bg="#E11923",
    fg="#000716",
    highlightthickness=0,
    font=("RobotoRoman Bold", 18),  # Adjust font and size as needed
)
output_text.place(
    x=52.0,
    y=144.0,
    width=574.0,  
    height=517.0,
)
output_text.config(state="disabled")  

def custom_print(*args):
    output_text.config(state="normal")  
    text_to_insert = " ".join(map(str, args))  
    output_text.insert("end", text_to_insert + "\n")  
    output_text.config(state="disabled") 
    output_text.see("end")  

print = custom_print

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
