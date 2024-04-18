from Arquivos.Classes.SerVivo import SerVivo
from Arquivos.Classes.Arma import Armas

class Pessoa(SerVivo):
    def __init__(self,nome):
        super().__init__(nome,100,50,1)
        self.arma = None
        self.Tesouro = 0
        self.capacidadeTesouro = (super().getVida())/100
        self.LocalizacaoCheckPoint = 1 #POIS O VERTICE 1 É O COMEÇO
        self.OndeEsta = 1
    # RESETAR CHECKPOINT DO PERSONAGEM
    def tirarChekPoint(self):
        self.LocalizacaoCheckPoint = 1
    # VERIFICA SE HÁ CHECKPOINT ATIVO DO PERSONAGEM
    def temCheckAtivado(self):
        if self.LocalizacaoCheckPoint !=1:
            return True
        return False
    # RETORNA O VÉRTICE ATUAL DO PERSONAGEM (APENAS O VALOR OU NOME)
    def getOndeEsta(self):
        return self.OndeEsta
    # SETA O VÉRTICE ONDE O PERSONAGEM ESTÁ (APENAS O VALOR OU NOME)
    def setOndeEsta(self,valor):
        self.OndeEsta = valor
    # RETORNA O VÉRTICE A QUAL O PERSONAGEM ATIVOU O CHECKPOINT
    def getLocalizacaoCheckPoint(self):
        return self.LocalizacaoCheckPoint
    # SETA O VÉRTICE A QUAL O PERSONAGEM ATIVOU O CHECKPOINT
    def setLocalizacaoCheckPoint(self,localizacao):
        self.LocalizacaoCheckPoint = localizacao
    # FUNÇÃO QUE ATUALIZA A CAPACIDADE QUE PODE LEVAR DO TESOURO
    def atualizarCapacidadeTesouro(self):
        self.capacidadeTesouro = (super().getVida())/100 # PERTENCE AO INTERVALO [0,1]
    # FUNÇÃO QUE ATUALIZA A QUANTIDADE DE OURO QUE O PERSONAGEM ESTÁ LEVANDO
    def atualizarCapacidadeDoTesouroNaMao(self):
        quantidade = abs(self.Tesouro*self.getCapacidadeTesouro()/100)
        self.Tesouro = self.Tesouro - quantidade/50
    # FUNÇÃO QUE ARMAZENA A QUANTIDADE DE TESOURO DE ACORDO COM A SUA CAPACIDADE DE LEVAR
    def carregarTesouro(self,qtdDeTesouro):
        print(f"{self.getCapacidadeTesouro()},{qtdDeTesouro}")
        quantidade = abs(qtdDeTesouro*self.getCapacidadeTesouro()/100)
        self.Tesouro = quantidade
    # RETORNA A QUANTIDADE DE TESOURO LEVADA
    def getTesouro(self):
        return round(self.Tesouro,2)
    # RETORNA A CAPACIDADE QUE O PERSONAGEM TÊM DE LEVAR O TESOURO
    def getCapacidadeTesouro(self):
        return self.capacidadeTesouro
    # O PERSONAGEM LEVA DANO
    def levarDano(self,dano):
        if dano > 0:
            super().diminuirVida(dano)
            self.atualizarCapacidadeDoTesouroNaMao()
    # FUNÇÃO DE CONSUMIR ITEM
    def consumirItem(self,item):
        ptVida = item.getptVida()
        ptAtaque = item.getptAtaque()
        if ptVida >=0 and ptAtaque >=0:
            super().aumentarVida(ptVida)
            super().aumentarAtaque(ptAtaque)
            self.atualizarCapacidadeTesouro()
        elif ptVida >=0 and ptAtaque <0:
            super().aumentarVida(ptVida)
            self.diminuirAtaque(ptAtaque)
            self.atualizarCapacidadeTesouro()
        elif ptVida <0 and ptAtaque >=0:
            self.diminuirVida(ptVida)
            super().aumentarAtaque(ptAtaque)
            self.atualizarCapacidadeTesouro()
        else:
            self.diminuirVida(ptVida)
            self.diminuirAtaque(ptAtaque)
            self.atualizarCapacidadeTesouro()
    # FUNÇÃO QUE EQUIPA ARMA
    def equiparArma(self,arma):
        self.arma = arma
        self.atualizarCapacidadeTesouro()
    # FUNÇÃO QUE RETORNA SE TEM ARMA
    def getTemArma(self):
        if self.arma==None:
            return False
        return True
    # FUNÇÃO DE RECOMEÇAR PERSONAGEM
    def recomercarPersonagem(self):
        self.arma = None
        self.vida = 100
        self.atualizarCapacidadeTesouro()
        self.ataque = 50