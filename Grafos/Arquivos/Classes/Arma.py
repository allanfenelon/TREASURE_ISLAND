class Armas:
    def __init__(self,nome,nivel):
        self.nome = nome
        self.tipos =  {
            # TIPO : # ataque
            0: 0,
            1: 15, # ARMA NV1
            2: 20, # ARMA NV2
            3: 25 # ARMA NV3
        }
        self.ptAtaque = self.tipos[int(nivel)]
    # GETTERS
    def getNome(self):
        return self.nome
    def getPtAtaque(self):
        return self.ptAtaque