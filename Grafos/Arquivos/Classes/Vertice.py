from Arquivos.Classes import Arma, Item, SerVivo


class Vertice:
    def __init__(self,nome):
        self.nome = nome # NOME DO VÉRTICE
        self.temCriaturas = False # SE HÁ CRIATURA NO VÉRTICE
        self.temItem = False # SE HÁ ITEM NO VÉRTICE
        self.temArma = False # SE HÁ ARMA DO VÉRTICE
        self.criaturas = None # VARIÁVEL QUE VAI RECEBER O OBJETO DA CRIATURA
        self.itens = None 
        self.arma = None
        self.CheckPoint = False
        self.quantidadeDetesouro = 500000
        self.coordX = 0
        self.coordY = 0
    # SETA AS COORDENADAS DO VÉRTICE
    def setCoordenadas(self,x,y):
        self.coordX = x
        self.coordY = y
    # RETORNA AS COORDENADAS DO VÉRTICE
    def getCoordenadas(self):
        return self.coordX, self.coordY
    # SETA NA VARIÁVEL BOOBLEANA SE TEM ARMA
    def setTemArma(self):
        self.temArma = True
    # SETA NA VARIÁVEL BOOLEANA SE TEM ARMA
    def setTemCriaturas(self,valor = False):
        if isinstance(valor, bool):
            self.temCriaturas = valor
    # SETA NA VARIÁVEL BOOLEANA SE TEM ITEM
    def setTemItem(self,valor = False):
         if isinstance(valor, bool):
            self.temItem = valor
    # FUNÇÃO QUE ATIVA CHECKPOINT
    def setAtivarCheckPoint(self):
        self.CheckPoint = True
        self.temCriaturas = False
        self.criaturas = 0
    # FUNÇÃO QUE DESATIVA CHECKPOINT
    def setDesativarCheckPoint(self):
        self.CheckPoint = False
    # SETA O OBJETO CRIATURA NO VÉRTICE
    def setCriatura(self,nome,atq):
        self.criaturas = SerVivo.SerVivo(nome, ataque=atq)
        self.setTemCriaturas(True)
    # RETORNA O OBJETO CRIATURA QUE HÁ NO VÉRTICE
    def getCriatura(self):
        if self.temCriaturas:
            return self.criaturas
        return None
    # FUNÇÃO QUE SETA O OBJETO ITEM NO VÉRTICE
    def setItem(self,nome,tipo):
        self.itens = Item.Item(nome,tipo)
        self.setTemItem(True)
    # FUNÇÃO QUE RETORNA O OBJETO ITEM QUE HÁ NO VÉRTICE
    def getItem(self):
        if self.temItem:
            return self.itens
        return None
    # FUNÇÃO QUE SETA UMA ARMA NO VÉRTICE
    def setArma(self,nome,tipo):
        self.arma = Arma.Armas(nome,tipo)
        self.setTemArma()
    # FUNÇÃO QUE RETORNA A ARMA QUE HÁ NO VÉRTICE
    def getArma(self):
        if self.temArma:
            return self.arma
        return None
    # RETORNA SE É CHECKPOINT ESSE VÉRTICE
    def getECheckPoint(self):
        return self.CheckPoint
    # RETORNA O NOME DO VÉRTICE
    def getNome(self):
        return self.nome
    # RETORNA SE TEM ARMA NP VÉRTICE
    def getTemArma(self):
        return self.temArma
    # RETORNA SE HÁ CRIATURAS NO VÉRTICE
    def getTemCriaturas(self):
        return self.temCriaturas
    # RETORNA SE HÁ ITENS NO VÉRTICE
    def getTemItens(self):
        return self.temItem


    
    