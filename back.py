#enqueue - adicionar elemento na fila
#dequeue - remover elemento da fila

#Funcionalidades do jogo:
#1. usuario digita o nome dos participantes
# JOGO COMEÇA
#2. a batata quente sera passada para seu vizinho  #BATATA QUENTE SERA O PRIMEIRO INDICE
#3. onde a batata quente parar a pessoa tera de sair do jogo
#4. ganha quem ficar por ultimo

def tirarquadrado():
    return None

def lista_vazia(array):
    if not array:
        print("Elementos insuficentes.")
        return None
    else:
        return array

def enQueue(array, valor): #Adiciona elementos na fila sendo que o primeiro elemento ficara no indice zero(vulgo primeiro indice)
    array.append(valor)
    return array


def dequeue(array):
    if not array:  # Verifica se a lista esta vazia
        return None  # retorna nulo caso esteja
    tirarquadrado()
    return array.pop(0)


def fila_circular(array):
    if len(array) < 2:
        print("Elementos insuficientes.")
    else:
        for event in range(tempo): #Roda array 5 vezes sendo que os elemmentoss do array se movem para a equerda
            primeiro_elemento = array[0]
            array[0:-1] = array[1:]  # Movendo todos os elementos uma posição para a esquerda
            array[-1] = primeiro_elemento  # Colocando o primeiro elemento na última posição
    dequeue(array) #Remove o indice zero do  array(vulgo primeiro elemento)
    return array


on = True
participantes = []
count = 1
tempo = int(input("Informe quantos rounds: "))
while on:
    nome_participante = input(f'\n Informe o nome do participante {count} \n Ou digite (1) para inicar o jogo: ').lower()
    participantes = enQueue(participantes, nome_participante) #Adicionando dados a fila
    count += 1
    if nome_participante == "1":
        participantes.pop()
        print(" \n Vamos começar...")
        lista_vazia(participantes)
        # Jogo iniciado
        while len(participantes) > 1:
            fila_circular(participantes)
            print(participantes)
            print(f"A sequencia de contagem foi {tempo}.")
        on = False
