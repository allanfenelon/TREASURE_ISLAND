class Item:
    def __init__(self,nome,tipo):
        self.nome = nome
        self.tipo = tipo
        self.tipos =  {
            # TIPO : (PTATAQUE, PTVIDA)
            1: (10, 0), # ITEM ATAQUE NV1
            2: (15, 0), # ITEM ATAQUE NV2
            3: (20, 0), # ITEM ATAQUE NV3
            4: (0, 5), # ITEM DE VIDA NV1
            5: (0, 10), # ITEM DE VIDA NV2
            6: (0, 15), # ITEM DE VIDA NV3
            7: (0,50), # ITEM REGENERA 50% DE VIDA
            8: (-10, -10) # ITEM DE VENENO
        }
        self.ptAtaque = self.tipos[int(tipo)][0]
        self.ptVida = self.tipos[int(tipo)][1]
    # FUNÇÃO QUE RETORNA O NOME DO ITEM
    def getNome(self):
        return self.nome
    # FUNÇÃO QUE RETORNA O TIPO DO ITEM
    def getTipo(self):
        return self.tipo
    # FUNÇÃO QUE RETORNA O ATAQUE QUE O ITEM OFERTA
    def getptAtaque(self):
        return self.ptAtaque
    # FUNÇÃO QUE RETORNA A VIDA QUE O ITEM OFERTA
    def getptVida(self):
        return self.ptVida


    