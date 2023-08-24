class Labirinto:
    def __init__(self, lab, inicio, fim):
        self._labirinto = lab
        self._inicio = inicio
        self._fim = fim
        self.position = inicio

    def start(self):
        line, col  = self._inicio
        self._labirinto[line][col] = "*"

    def toRight(self):
        line, col = self.position
        new_postion = (line,col+1)
        self._labirinto[line][col+1] = "*"
        self.position = new_postion

    def toLeft(self):
        line, col = self.position
        new_postion = (line,col-1)
        self._labirinto[line][col-1] = "*"
        self.position = new_postion

    def toUp(self):
        line, col = self.position
        new_postion = (line-1,col)
        self._labirinto[line-1][col] = "*"
        self.position = new_postion

    def toDown(self):
        line, col = self.position
        new_postion = (line+1,col)
        self._labirinto[line+1][col] = "*"
        self.position = new_postion

    def goBack(self, position):
        self.position = position

    def isAvailable(self, position):
        lab = self._labirinto
        line, col = position

        if lab[line][col] != "#" and lab[line][col] != "*":
            return True
        else:
            return False