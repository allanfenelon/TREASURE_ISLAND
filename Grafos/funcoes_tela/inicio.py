import sys
import pygame
import random
import os
import random
import pandas as pd

from Arquivos.Classes.Grafo import Grafo
from Arquivos.Classes.Pessoa_ import Pessoa

def inicializarVertices(gf):
    """
    Inicializa os vértices do Grafo com os dados fornecidos por um arquivo CSV.

    Entrada:
        - gf: O Grafo no qual os vértices serão inicializados e atualizados.

    """
    # LEITURA DO CSV VERTICES
    dadosVertice = pd.read_csv("./Arquivos/data/vertices.csv",sep=",")
    for i, row in dadosVertice.iterrows(): # PERCORRE LINHA POR LINHA
        # SALVANDO O DADO DA LINHA I E DA COLUNA X
        vertice = row["vertice"]
        checkpoint = row["checkpoint"]
        temItem = row["temItem"]
        temCriatura = row["temCriatura"]
        nomeCriatura = row["nomeCriatura"]
        ptAtaque = row["ptAtaque"]
        tipoItem = row["tipoItem"]
        temArma = row["temArma"]
        tipoArma = row["tipoArma"]
        nomeItem = row["nomeItem"]
        nomeArma = row["nomeArma"]
        coordX = row['coorX']
        coordY = row['coorY']
        # INSERINDO VERTICE (COMO ESTA INDO LINHA POR LINHA NÃO HÁ PROBLEMAS)
        gf.setVertice(vertice)
        if(gf.getVertice(vertice) != None): # VERIFICA SE O VÉRTICE ESTÁ NO GRAFO
            # ATIVA, SE HOUVER O CHECK POINT
            if checkpoint:
                gf.getVertice(vertice).setAtivarCheckPoint() 
            # INSERINDO ITEM NO VERTICE CASO HAJA
            if temItem and not gf.getVertice(vertice).getTemItens():
                gf.getVertice(vertice).setItem(nomeItem,tipoItem)
            # INSERIDNO CRIATURA CASO HAJA
            if temCriatura and not gf.getVertice(vertice).getTemCriaturas():
                gf.getVertice(vertice).setCriatura(nomeCriatura,ptAtaque)
            # INSERINDO ARMA CASO HAJA
            if temArma and not gf.getVertice(vertice).getTemArma():
                gf.getVertice(vertice).setArma(nomeArma,tipoArma)
            # INSERINDO AS COORDENADAS
            gf.getVertice(vertice).setCoordenadas(coordX,coordY)

            
def inicializarArestas(gf):
    """
    Inicializa as arestas do Grafo com os dados fornecidos por um arquivo CSV.

    Entrada:
        - gf: O Grafo no qual as arestas serão inicializadas e atualizadas.
    """

    # Diretório do script Python
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    # Caminho para o diretório Arquivos
    caminho_arquivos = os.path.join(diretorio_script, "..", "Arquivos")
    arestas_csv = os.path.join(caminho_arquivos, "arestas.csv")
    # LEITURA DO CSV ARESTAS
    dadosArestas = pd.read_csv("./Arquivos/data/arestas.csv",sep=",")
    for i, row in dadosArestas.iterrows(): # PERCORRE LINHA POR LINHA
        origem = row["origem"]
        destino = row["destino"]
        gf.setArestas(origem,destino)

################################ DEFININDO VARIÁVEIS AUXILIARES PARA AS TELAS DO PYGAME

# Definir cores
cor_botao = (0, 150, 0)
cor_texto = (255, 255, 255)
# Define a cor branca
WHITE = (255, 255, 255)
# Define a cor preta para o texto
BLACK = (0, 0, 0)
# Define a cor cinza para o fundo
GRAY = (200, 200, 200)
cor_hover = (0, 255, 0)
def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
fundo = pygame.image.load('./Arquivos/image/island.jpg')  
fundo = pygame.transform.scale(fundo, (800, 600))
personagemIMG = pygame.image.load('./Arquivos/image/people.png')
personagemIMG = pygame.transform.scale(personagemIMG, (40, 50))

####################################

#################################### FUNÇÕES AUXILIARES PARA O PLOT DO PERSONAGEM E SUA MOVIMENTAÇÃO

def plotar_personagem(tela, personagemIMG= personagemIMG, posx=575+3, posy=499+5):
    tela.blit(personagemIMG, (posx, posy))
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
####################################
# FUNÇÃO AUXILIAR PARA PLOTAR TEXTO
def desenhar_texto(tela,texto, x, y):
    # Carrega a fonte padrão do sistema
    fonte = pygame.font.Font(None, 25)
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_retangulo = texto_surface.get_rect()
    texto_retangulo.center = (x, y)
    tela.blit(texto_surface, texto_retangulo)
# FUNÇÃO AUXILIAR PARA PLOTAR BOTÃO
def desenhar_botao(tela,texto, x, y, largura, altura, cor_normal, cor_hover):
        pos_mouse = pygame.mouse.get_pos()

        if x < pos_mouse[0] < x + largura and y < pos_mouse[1] < y + altura:
            pygame.draw.rect(tela, cor_hover, (x, y, largura, altura))
        else:
            pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))

        desenhar_texto(tela,texto, x + largura / 2, y + altura / 2)

def tela_inicial(tela, largura, altura):
    """
    Exibe a tela inicial do jogo com um botão "Iniciar".

    Entrada:
        - tela: A tela do jogo onde a tela inicial será exibida.
        - largura: Largura da tela.
        - altura: Altura da tela.
    """
    # Carregar imagem de fundo
    fundo = pygame.image.load('./Arquivos/image/inicio_bg.jpeg')  # Substitua pelo caminho correto da sua imagem
    fundo = pygame.transform.scale(fundo, (largura, altura))

    def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover):
        pos_mouse = pygame.mouse.get_pos()
        if x < pos_mouse[0] < x + largura and y < pos_mouse[1] < y + altura:
            pygame.draw.rect(tela, cor_hover, (x, y, largura, altura))
        else:
            pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))
        desenhar_texto(tela,texto, x + largura / 2, y + altura / 2)
    inicio = True
    # Loop principal do jogo
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Verificar se houve um clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                inicio = False
        # Desenhar imagem de fundo
        tela.blit(fundo, (0, 0))
        # Desenha o botão "Iniciar"
        desenhar_botao('Iniciar', largura // 2 - 100, altura // 2, 200, 50, cor_botao, (0, 255, 0))
        pygame.display.flip()

