#FUNCOES USADAS MAIN
import pygame
import numpy as np
import time

from funcoes_tela.inicio import *
from Arquivos.Classes.Grafo import Grafo
from Arquivos.Classes.Pessoa_ import Pessoa



###################################################### (1)
gf = Grafo()  # GRAFO
personagem = Pessoa("Pedro") #PESSOA
inicializarVertices(gf) # INICIALIZA OS VERTICES
inicializarArestas(gf) # INICIALIZA AS ARESTAS
######################################################
print("Lista de Adjacência")
gf.imprimirListaAdj()
###################################################### (2)
pygame.init() # Inicializa o Pygame
screen_width = 800 # Define as dimensões da tela do Pygame
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) # DEFINE A TELA
clock = pygame.time.Clock() # CLOCK
pygame.time.Clock().tick(60)  # 60 frames por segundo
######################################################

###################################################### (3)
# -> CARREGAMENTO DAS FONTES
font = pygame.font.Font(None, 25)
fonte = pygame.font.SysFont('Arial', 30)
# -> CORES
WHITE = (255, 255, 255) # Define a cor branca
BLACK = (0, 0, 0) # Define a cor preta para o texto
GRAY = (200, 200, 200)# Define a cor cinza para o fundo
PRETO = (0, 0, 0) # PRETO
BRANCO = (255, 255, 255) # BRANCO
CINZA_CLARO = (200, 200, 200) #CINZA
# -> IMAGEMS
personagemIMG = pygame.image.load('./Arquivos/image/people.png')
onca = pygame.image.load('./Arquivos/image/onca.png')
crocodilo = pygame.image.load('./Arquivos/image/crocodilo.png')
formiga = pygame.image.load('./Arquivos/image/formiga.png')
game_over = pygame.image.load('./Arquivos/image/Game_Over.jpg') 
combate_img = pygame.image.load('./Arquivos/image/img_combate.jpg') 
# REDIMENSIONAMENTO DAS IMAGENS
game_over = pygame.transform.scale(game_over, (800, 600))
combate_img = pygame.transform.scale(combate_img, (800, 600))
personagemIMG = pygame.transform.scale(personagemIMG, (40, 50))
onca = pygame.transform.scale(onca, (40, 50))
crocodilo = pygame.transform.scale(crocodilo, (40, 50))
formiga = pygame.transform.scale(formiga, (40, 50))
personagemIMGMaior = pygame.transform.scale(personagemIMG, (200, 210))
oncaMaior = pygame.transform.scale(onca, (200, 210))
crocodiloMaior = pygame.transform.scale(crocodilo, (200, 210))
formigaMaior = pygame.transform.scale(formiga, (200, 210))

# -> BOTÕES
# Crie retângulos para os botões
largura_botao = 200
altura_botao = 50
posicao_botao_desistir = (600 // 2 - largura_botao // 2, 800 // 2 - 50)
posicao_botao_continuar = (600 // 2 - largura_botao // 2, 800 // 2 + 50)
posicao_botao_fugir = (600 // 2 - largura_botao // 2, 800 // 2 - 50)
posicao_botao_batalhar = (600 // 2 - largura_botao // 2, 800 // 2 + 50)
retangulo_botao_desistir = pygame.Rect(posicao_botao_desistir, (largura_botao, altura_botao))
retangulo_botao_continuar = pygame.Rect(posicao_botao_continuar, (largura_botao, altura_botao))
retangulo_botao_batalhar = pygame.Rect(posicao_botao_batalhar, (largura_botao, altura_botao))
retangulo_botao_fugir = pygame.Rect(posicao_botao_fugir, (largura_botao, altura_botao))
######################################################

###################################################### (4)
# FUNÇÕES
def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def plotar_personagem(tela, personagemIMG= personagemIMG, posx=575+3, posy=499+5):
    tela.blit(personagemIMG, (posx, posy))

# FUNÇÃO QUE AUXILIAR DA FUNÇÃO (PLOT PRINCIAPL)
def plotInfoPessoa():
    text = font.render(f"Vida: {personagem.getVida()}pts  |  Ataque: {personagem.getAtaque()}pts  |  qtd Tesouro carregando: R${personagem.getTesouro()}", True, (0, 0, 0))
    text_rect = text.get_rect(top=10, centerx=screen_width/2)# Obtém as dimensões do texto
    padding = 10 # Define as dimensões do retângulo do fundo
    bg_rect = pygame.Rect(text_rect.left - padding, text_rect.top - padding, text_rect.width + padding*2, text_rect.height + padding*2)
    draw_rounded_rect(screen, GRAY, bg_rect, 10)# Desenha o retângulo de fundo com bordas arredondadas
    screen.blit(text, text_rect) # Desenha o texto na tela
# FUNÇÃO QUE PLOTA O TEMPO RESTANTE DO JOGO, O VÉRTICE PARA ONDE ESTÁ INDO E O VÉRTICE CHECKPOINT
def plotOndeEstaETempo(tempo):
    minutos, segundos = retorneOtempo(tempo)
    personagem_OndeEsta = "Indo para: " + str(personagem.getOndeEsta())
    tempo_restante = "Tempo Restante: " + f"{minutos}:{segundos}"
    Check = "Local de Renascimento: " + f"{personagem.getLocalizacaoCheckPoint()}"
    largura_tela, altura_tela = 800, 600  # Dimensões da tela
    # Definindo a caixa que conterá as informações do personagem e do tempo restante
    caixa_largura, caixa_altura = 180, 100
    caixa_info = pygame.Rect(largura_tela - caixa_largura, altura_tela - caixa_altura, caixa_largura, caixa_altura)
    # Desenhar a caixa com bordas arredondadas
    rect = pygame.Rect(largura_tela - caixa_largura, altura_tela - caixa_altura, caixa_largura, caixa_altura)
    color = (100, 100, 100)
    radius = 20
    alpha = 128
    pygame.draw.rect(screen, (0, 0, 0, alpha), rect)
    pygame.draw.rect(screen, color, rect, border_radius=radius)
    # Desenhar informações do personagem e tempo restante dentro da caixa
    fonte = pygame.font.Font(None, 20)
    texto_personagem_OndeEsta = fonte.render(personagem_OndeEsta, True, (255, 255, 255))
    texto_tempo_restante = fonte.render(tempo_restante, True, (255, 255, 255))
    Check = fonte.render(Check, True, (255, 255, 255))
    # Ajuste das posições do texto
    posicao_y = altura_tela - caixa_altura + 10
    screen.blit(texto_personagem_OndeEsta, (largura_tela - caixa_largura + 10, posicao_y))
    screen.blit(texto_tempo_restante, (largura_tela - caixa_largura + 10, posicao_y + 20))
    screen.blit(Check, (largura_tela - caixa_largura + 10, posicao_y + 40))
# FUNÇÃO QUE PLOTA A LOCALIDADE QUE CADA VERTICE A ANIMAIS
def plotar_localidades():
    locais = gf.getObjectVertice() # OBTÉM A LISTA DE OBJETOS VÉRTICES 
    fonte = pygame.font.Font(None, 36)  
    for i in locais:
        nome = str(i.getNome()) # PEGA O NOME DO VÉRTICE
        coordenadas = i.getCoordenadas() # PEGA AS COORDENADAS DO VÉRTICE
        if i.getECheckPoint() and not personagem.temCheckAtivado(): 
            # Desenhar a bolinha verde como fundo
            pygame.draw.circle(screen, (0, 255, 0), coordenadas, 20)  # Cor verde, raio 20
        if i.getTemCriaturas():
            if i.getCriatura().getNome() == "Crocodilo Gigante" and i.getCriatura().estaVivo():
                screen.blit(crocodilo, coordenadas)
            elif i.getCriatura().getNome() == "Onça Pintada Mitica" and i.getCriatura().estaVivo():
                screen.blit(onca, coordenadas)
            elif i.getCriatura().getNome() == "Formiga Quimera" and i.getCriatura().estaVivo():
                screen.blit(formiga, coordenadas)
        texto = fonte.render(nome, True, (255, 255, 255))  # Cor do texto: branco
        posicao_texto = texto.get_rect(center=coordenadas)  # Centraliza o texto na coordenada
        screen.blit(texto, posicao_texto)  # Desenha o texto na tela
# PLOTA A VIDA, ATAQUE E QUANTIDADE DE TESOURO DO PERSONAGEM
def plotPrincipal(tempo):
        ###############################################
        screen.blit(fundo, (0, 0))    # Desenhar imagem de fundo
        plotInfoPessoa()
        plotar_localidades()
        plotOndeEstaETempo(tempo)
        ###############################################
# PLOTA A IMAGEM DA CRIATURA NA LUTA       
def plotauxLuta(criatura):
    if criatura.getNome() == "Crocodilo Gigante" and criatura.estaVivo():
        screen.blit(crocodiloMaior, (400,300))
    elif criatura.getNome() == "Onça Pintada Mitica" and criatura.estaVivo():
        screen.blit(oncaMaior, (400,300))
    elif criatura.getNome() == "Formiga Quimera" and criatura.estaVivo():
        screen.blit(formigaMaior, (400,300))
# FUNÇÃO AUXILIAR
def desenhar_texto1(texto, cor, retangulo):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = retangulo.center
    screen.blit(texto_surface, texto_rect)
# TELA DE LUTA PERSONAGEM
def plotBatalhar(tempo,personagem,criatura):
    luta = True
    jalutou = False
    ataque_efetivo_criatura = 0
    
    while luta:
        condicaotempo = retorneOtempo(tempo_inicial)
        for event in pygame.event.get():# Processa eventos do Pygame
            if event.type == pygame.QUIT:
                repeticao = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botao_batalhar.collidepoint(event.pos):
                        plotBatalhar(tempo,personagem,criatura)
                        luta = False
                        jalutou = True
                    elif retangulo_botao_fugir.collidepoint(event.pos):
                        screen.fill((0, 0, 0))
                        desenhar_texto(screen, f'VOCÊ LEVOU {ataque_efetivo_criatura} DE DANO!', 400,100)
                        pygame.display.flip()
                        personagem.levarDano(ataque_efetivo_criatura)
                        pygame.time.delay(1000)
                        pygame.display.flip()
                        luta = False
                        jalutou = True
                        break
                    if retangulo_botao_desistir.collidepoint(event.pos):
                        screen.blit(game_over, (0, 0))
                        luta = False
                        pygame.quit()
                        sys.exit()
                    
        if not jalutou:              
            for i in range(1,4):
                if condicaotempo[0]<0 and condicaotempo[1]<0:
                    screen.blit(game_over, (0, 0))
                condicaotempo = retorneOtempo(tempo_inicial)
                for event in pygame.event.get():# Processa eventos do Pygame
                    if event.type == pygame.QUIT:
                        repeticao = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if retangulo_botao_desistir.collidepoint(event.pos):
                            screen.blit(game_over, (0, 0))
                            luta = False
                            pygame.quit()
                            sys.exit()
                        elif retangulo_botao_continuar.collidepoint(event.pos):
                            personagem.recomercarPersonagem()
                            luta = False
                
                vida_personagem = personagem.getVida()
                vida_criatura = criatura.getVida()
                if personagem.estaVivo() and criatura.estaVivo():
                    if criatura.getAtaque()>0:
                        ataque_efetivo_criatura = random.randint(1, criatura.getAtaque()//i)
                    else:
                        ataque_efetivo_criatura = 0
                    if personagem.getAtaque() > 0:
                        ataque_efetivo_personagem = random.randint(1, personagem.getAtaque() // i)
                    else: 
                        ataque_efetivo_personagem = 0
                    if condicaotempo[0]<0 and condicaotempo[1]<0:
                        screen.blit(game_over, (0, 0))
                    vida_personagem -= ataque_efetivo_criatura
                    screen.blit(combate_img, (0, 0))
                    desenhar_texto(screen, f'TEMPO: {condicaotempo[0]}:{condicaotempo[1]}', 400,60)
                    desenhar_texto(screen, f'ROUND: {i}', 400,80)
                    plotInfoPessoa()
                    plotar_personagem(screen, personagemIMGMaior, 200,300)
                    plotauxLuta(criatura)
                    criatura.diminuirVida(ataque_efetivo_personagem)
                    desenhar_texto(screen, f'VOCÊ ATACOU E TIROU {ataque_efetivo_personagem}PTS DA CRIATURA', 400,100)
                    desenhar_texto(screen, f'VIDA DA CRIATURA: {criatura.getVida()}', 500,300)
                    pygame.time.delay(1000)
                    pygame.time.delay(1000)
                    pygame.time.delay(1000)
                    pygame.display.flip()
                    if criatura.estaVivo():
                        screen.blit(combate_img, (0, 0))
                        condicaotempo = retorneOtempo(tempo_inicial)
                        desenhar_texto(screen, f'TEMPO: {condicaotempo[0]}:{condicaotempo[1]}', 400,60)
                        desenhar_texto(screen, f'ROUND: {i}', 400,80)
                        plotInfoPessoa()
                        plotar_personagem(screen, personagemIMGMaior, 200,300)
                        plotauxLuta(criatura)
                        vida_criatura -= ataque_efetivo_personagem
                        personagem.levarDano(ataque_efetivo_criatura // 3)
                        desenhar_texto(screen, f'VIDA DA CRIATURA: {criatura.getVida()}',500,300)
                        desenhar_texto(screen, f'VOCÊ FOI ATACADO E LEVOU -{ataque_efetivo_criatura // 3}PTS DE DANO', 400,100)
                        pygame.time.delay(1000)
                        pygame.time.delay(1000)
                        pygame.display.flip()
                        jalutou = True
                    
                    elif not criatura.estaVivo(): 
                        pygame.time.delay(1000)
                        screen.fill((0, 0, 0))
                        desenhar_texto(screen, f'VOCÊ MATOU A CRIATURA, PARABÉNS', 400,100)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        pygame.time.delay(1000)
                        pygame.display.flip()
                        luta = False
                        jalutou = True
                elif i == 3 and (personagem.estaVivo() and criatura.estaVivo()):
                    jalutou = True
                elif not personagem.estaVivo():
                    screen.fill((0, 0, 0))
                    desenhar_texto(screen, f'VOCÊ FOI MORTO!', 400,100)
                    # Desenhe os botões na tela
                    pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_desistir)
                    pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_continuar)
                    desenhar_texto1("Desistir", PRETO, retangulo_botao_desistir)
                    desenhar_texto1("Continuar", PRETO, retangulo_botao_continuar)
                    jalutou = True
                    luta = False
                    pygame.display.flip()
                elif not criatura.estaVivo():
                    screen.fill((0, 0, 0))
                    desenhar_texto(screen, f'VOCÊ MATOU A CRIATURA, PARABÉNS', 400,100)
                    pygame.time.delay(1000)
                    pygame.time.delay(1000)
                    pygame.display.flip()
                    luta = False
                    jalutou = True
                elif condicaotempo[0]<0 and condicaotempo[1]<0:
                    screen.blit(game_over, (0, 0))
                pygame.display.flip()
        elif personagem.estaVivo() and criatura.estaVivo():
            screen.fill((0, 0, 0))
            desenhar_texto(screen, f'VOCÊ NÃO MORREU E NEM MATOU A CRIATURA!', 400,100)
            # Desenhe os botões na tela
            pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_batalhar)
            pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_fugir)
            desenhar_texto1("LUTAR", PRETO, retangulo_botao_batalhar)
            desenhar_texto1("FUGIR", PRETO, retangulo_botao_fugir)
            pygame.display.flip()
        if not personagem.estaVivo():
            screen.fill((0, 0, 0))
            desenhar_texto(screen, f'VOCÊ FOI MORTO!', 400,100)
            # Desenhe os botões na tela
            pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_desistir)
            pygame.draw.rect(screen, CINZA_CLARO, retangulo_botao_continuar)
            desenhar_texto1("Desistir", PRETO, retangulo_botao_desistir)
            desenhar_texto1("Continuar", PRETO, retangulo_botao_continuar)
            pygame.display.flip()

        pygame.display.flip()
# FUNÇÃO QUE ITERATIVAMENTE É CHAMADA PARA FAZER A VERIFICAÇÃO DO TEMPO DO JOGO
def retorneOtempo(tempo_inicial):
    # Verifique o tempo atual
    tempo_atual = time.time()
    tempo_decorrido = tempo_atual - tempo_inicial

    # Desenhe o tempo decorrido na tela
    tempo_restante = max(0, 5 * 60 - int(tempo_decorrido))
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    return minutos,segundos
    
# Função para calcular o trajeto de linha reta entre dois pontos
def calcular_trajeto(k, p):
    trajeto = []
    x1, y1 = k
    x2, y2 = p
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return [k]
    else:
        for i in range(steps):
            x = round(x1 + dx * i / steps)
            y = round(y1 + dy * i / steps)
            trajeto.append((x, y))
        return trajeto
######################################################


###################################################### (5)
# VARIÁVEIS DE AUXILIO
indice_trajeto=0
ondeEsta = personagem.getOndeEsta()
tempo_inicial = time.time() # TEMPO AQUI
repeticao = True
indoCond = True
voltandoCond = False
estaIndo = True
indice_trajeto=0
######################################################

# CHAMANDO A TELA DE INICIO
tela_inicial(screen,screen_width,screen_height)
# INICIANDO O JOGO QUANDO SAI DA TELA INICIAL
while repeticao:
    for event in pygame.event.get():# Processa eventos do Pygame
        if event.type == pygame.QUIT:
            repeticao = False
            pygame.quit()
            sys.exit()
    # AQUI VERIFICA A DIREÇÃO DO PERCURSO (IDA E VOLTA)
    if estaIndo:
        Percuso_Persona = gf.dijkstra(1,14)
        personagem.setOndeEsta(1)
    elif not estaIndo:
        Percuso_Persona = gf.dijkstra(14,1)
        personagem.tirarChekPoint()
        personagem.setOndeEsta(14)
    print("Caminho que o personagem vai fazer:")
    print(Percuso_Persona)
   
    # FOR DO PERCURSO
    for j in range(1,len(Percuso_Persona)):
        
        for event in pygame.event.get():# Processa eventos do Pygame
            if event.type == pygame.QUIT:
                repeticao = False
                pygame.quit()
                sys.exit()
        i = Percuso_Persona[j] # PEGA O VÉRTICE A QUAL ESTÁ NO PERCURSO
        condicaoTempo = retorneOtempo(tempo_inicial)
        plotPrincipal(tempo_inicial) # PLOTA A TELA PRINCIPAL
        EstaVivo = personagem.estaVivo() # VARIÁVEL AUX (TRUE: VIVO, FALSE: MORTO)
        if EstaVivo:
            personagem.setOndeEsta(i) #ATUALIZA A LOCALIZAÇÃO DO PERSONAGEM
            i_dow = Percuso_Persona[j-1] #PEGA A POSIÇÃO QUE ESTAVA
            # CALCULA O TRAJETO DE DA POSIÇÃO I-1 A I
            trajeto = calcular_trajeto(gf.getVertice(i_dow).getCoordenadas(),gf.getVertice(i).getCoordenadas()) 
            animacao = True
            indice =0
            # ANIMAÇÃO DA MOVIMENTAÇÃO DO PERSONAGEM
            while animacao:
                plotPrincipal(tempo_inicial)
                plotar_personagem(screen, personagemIMG,trajeto[indice][0],trajeto[indice][1])
                # Verifica se ainda há trajeto a ser percorrido
                if indice < len(trajeto) - 1:
                    indice += 1
                    pygame.time.delay(10)
                else:
                    animacao = False
                pygame.display.flip()
            # VERIFICA AS CONDIÇÕES DE UM DETERMINADO VERTICE
            if condicaoTempo[0]<0 and condicaoTempo[1]<0:
                pygame.display.flip()
                screen.blit(game_over, (0, 0))
                pygame.display.flip()
            ######## VERIFICAÇÕES DO VÉRTICE ########
            if(gf.getVertice(i).getECheckPoint()): # SE TEM CHECKPOINT
                if not personagem.temCheckAtivado():
                    desenhar_texto(screen, f"Você ativou o checkpoint do vértice {i}", 400,100)
                    personagem.setLocalizacaoCheckPoint(i)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.time.delay(1000)
            elif gf.getVertice(i).getTemArma(): # SE TEM ARMA
                desenhar_texto(screen, f"VOCÊ ACHOU A ARMA: {item.getNome()}, MAS JA POSSUI UMA ARMA EQUIAPA!", 400,100)
                if not personagem.getTemArma(): 
                    desenhar_texto(screen, f"VOCÊ EQUIPOU A ARMA: {item.getNome()}", 400,100)
                    desenhar_texto(screen, f"RECEBEU: {item.getptAtaque()}PTS DE ATAQUE", 400,80)
                    arma = gf.getVertice(i).getArma()
                    personagem.equiparArma(arma)
            elif gf.getVertice(i).getTemItens() and not personagem.getVida() == 100: # SE TEM ITEM E A VIDA DO PERSONAGEM NÃO ESTÁ CHEIA
                item = gf.getVertice(i).getItem()
                desenhar_texto(screen, f"RECEBEU: {item.getptVida()}PTS DE VIDA E {item.getptAtaque()}PTS DE ATAQUE", 400,80)
                desenhar_texto(screen, f"VOCÊ CONSUMIU O ITEM: {item.getNome()}", 400,100)
                personagem.consumirItem(item)
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.time.delay(1000)
                if gf.getVertice(i).getTemCriaturas() and (gf.getVertice(i)).getCriatura().estaVivo(): # APÓS CONSUMIR ITEM VERIFICA SE TEM CRIATURA
                    criatura = gf.getVertice(i).getCriatura()
                    plotBatalhar(tempo_inicial,personagem,criatura)
            elif gf.getVertice(i).getTemCriaturas() and (gf.getVertice(i)).getCriatura().estaVivo() and i ==14:
                # CASO EM QUE ESTÁ NO VÉRTICE ONDE TEM O TESOURO E TEM ALGUMA CRIATURA
                # NESTE CASO INICIA-SE A LUTA E APÓS ISSO O PERSONAGEM PODE ROUBAR O TESOURO
                criatura = gf.getVertice(i).getCriatura()
                plotBatalhar(tempo_inicial,personagem,criatura)
                estaIndo = False
                plotPrincipal(tempo_inicial)
                desenhar_texto(screen, f"VOCÊ ENCONTROU: R$500.000 DE OURO", 450,100)
                desenhar_texto(screen, f"Pegando ouro...", 400,90)
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.time.delay(1000)
                personagem.carregarTesouro(500000)
            # SE TEM CRIATURA, SE SIM VAI LUTAR (3 ROUND)
            elif gf.getVertice(i).getTemCriaturas() and (gf.getVertice(i)).getCriatura().estaVivo():
                criatura = gf.getVertice(i).getCriatura()
                plotBatalhar(tempo_inicial,personagem,criatura)
            elif i == 14: # SE CHEGOU AO VÉRTICE DO TESOURO
                estaIndo = False
                desenhar_texto(screen, f"VOCÊ ENCONTROU: R$500.000 DE OURO", 450,100)
                desenhar_texto(screen, f"Pegando ouro...", 400,90)
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.time.delay(1000)
                personagem.carregarTesouro(500000)
            elif i == 1 and personagem.getTesouro()>0: # SE QUANDO ESTIVER CARREGANDO O TESOURO E CHEGOU NA ILHA
                screen.fill((0, 0, 0))
                desenhar_texto(screen, f'PARABÉNS, VOCÊ GANHOU E PEGOU R${personagem.getTesouro()} DO TESOURO', 400,100)
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
            
        elif condicaoTempo[0] <0 and condicaoTempo[1] <0: # CONDIÇÃO DO TEMPO
            screen.blit(game_over, (0, 0))
        
        else: # OUTROS CASOS
            screen.blit(game_over, (0, 0))
            
        pygame.time.delay(100)
        pygame.display.flip()
        
    pygame.display.flip()

