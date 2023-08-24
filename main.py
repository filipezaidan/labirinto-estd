from pilha import PilhaArray
from gera_lab import gera_lab, print_lab
from labirinto import Labirinto

def eh_possivel_sair(labirinto):
    steps = PilhaArray()
    inicio = (1,0)
    fim =  (len(labirinto)-2, len(labirinto[0])-1)

    lab = Labirinto(labirinto,inicio,fim)
    lab.start()

    while lab.position != fim:
        line, col = lab.position

        if lab.isAvailable((line,col+1)):
            steps.push(lab.position)
            lab.toRight()
        elif lab.isAvailable((line+1, col)):
            steps.push(lab.position)
            lab.toDown()
        elif lab.isAvailable((line-1, col)):
            steps.push(lab.position)
            lab.toUp()
        elif lab.isAvailable((line,col-1)):
            steps.push(lab.position)
            lab.toLeft()
        else:
            if(lab.position != inicio):
                prevPosition = steps.pop()
                lab.goBack(prevPosition)
            else:
                break

    print_lab(lab._labirinto)
    if lab.position == fim:
        return True
    else:
        return False

labirinto = gera_lab(7,15)
print(eh_possivel_sair(labirinto))