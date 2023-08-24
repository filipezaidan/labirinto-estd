from pilha import PilhaArray
from gera_lab import gera_lab, print_lab 
labirinto = gera_lab(7,15)

pilha = PilhaArray()
inicio = (1,0)
posicaoAtual = inicio
fim =  (len(labirinto)-2, len(labirinto[0])-1)


def toBack():
    global posicaoAtual
    posicaoAtual = pilha.pop()

def toRight():
    global posicaoAtual
    line, column = posicaoAtual
    newPosition = (line,column + 1)

    # if column + 1 <= len(labirinto[0]):
    labirinto[line][column+1] = "*"
    pilha.push(posicaoAtual)
    posicaoAtual = newPosition


def toLeft():
    global posicaoAtual
    line, column = posicaoAtual
    newPosition = (line,column - 1)

    # if column > 0:
    labirinto[line][column-1] = "*"
    pilha.push(posicaoAtual)
    posicaoAtual = newPosition

def toUp():
    global posicaoAtual
    line, column = posicaoAtual
    newPosition = (line-1,column)

    # if line > 0:
    labirinto[line-1][column] = "*"
    pilha.push(posicaoAtual)
    posicaoAtual = newPosition

def toDown():
    global posicaoAtual
    line, column = posicaoAtual
    newPosition = (line+1,column)

    # if line + 1 <= len(labirinto):
    labirinto[line+1][column] = "*"
    pilha.push(posicaoAtual)
    posicaoAtual = newPosition

def start(inicio):
    line, column = inicio
    labirinto[line][column] = "*"

start(inicio)


def isAvailable(position):
    line, column = position

    if labirinto[line][column] != "#" and labirinto[line][column] != "*":
       return True
    else:
        return False


while posicaoAtual != fim:
    line, column = posicaoAtual

    
    if isAvailable((line,column+1)):
        toRight()
    elif isAvailable((line+1, column)):
        toDown()
    elif isAvailable((line-1, column)):
        toUp()
    elif isAvailable((line,column-1)):
        toLeft()
    else:
        if(posicaoAtual != inicio):
            toBack()
        else:
            break
        
    

print(pilha)
print("posição atual: ", posicaoAtual)
print_lab(labirinto) #imprime o lab
