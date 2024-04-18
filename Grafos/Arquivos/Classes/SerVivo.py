
class SerVivo:
    def __init__(self, nome,vida=50,ataque=25,tipo=2):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo # 1 = PESSOA 2 = CRIATURA

    # RETORNA O NOME DO PERSONAGEM OU CRIATURA
    def getNome(self):
        return self.nome
    # RETORNA A VIDA DO PERSONAGEM OU CRIATURA
    def getVida(self):
        return self.vida
    # RETORNA O ATAQUE DO PERSONAGEM OU CRIATURA
    def getAtaque(self):
        return self.ataque
    # RETORNA O TIPO DO SERVIVO
    def getTipo(self):
        return self.tipo
    # AUMENTO A VIDA DO SER VIVO
    def aumentarVida(self,valor):
        if self.vida < 100: 
            if valor + self.vida > 100 and self.vida>=0:
                vida_faltante = 100 - (self.vida + valor)
                self.vida += vida_faltante
            else:
                self.vida += valor
    # DIMINUI A VIDA DO SERVIVO
    def diminuirVida(self,valor):
        if self.vida > 0:
            if self.vida - valor <0:
                self.vida = 0
            else:
                self.vida -= valor
    # VERIFICA SE O SER VIVO ESTÁ VIVO
    def estaVivo(self):
        if self.vida > 0:
            return True
        else:
            return False
    # FUNÇÃO DE REVIVER SER VIVO
    def reviverSerVivo(self,vida,ataque): 
        if not self.estaVivo():
            self.vida = vida
            self.ataque = ataque
    # FUNÇÃO QUE AUMENTA O ATAQUE DO SER VIVO 
    def aumentarAtaque(self,valor):
        if self.ataque <100:
            if valor + self.ataque > 100:
                ataque_faltante = 100 - (self.ataque + valor)
                self.ataque += ataque_faltante
            else:
                self.ataque += valor
    # FUNÇÃO QUE DIMINUI ATAQUE DO SER VIVO
    def diminuirAtaque(self,valor):
        if self.ataque > 0:
            if self.ataque + valor > 0:
                self.ataque += valor
            else:
                self.ataque = 0
