# import pygame
# import random

# # Inicializar
# pygame.init()
# LARGURA, ALTURA = 800, 400
# tela = pygame.display.set_mode((LARGURA, ALTURA))
# pygame.display.set_caption("Dino Runner")
# relogio = pygame.time.Clock()

# # Cores
# PRETO = (0, 0, 0)
# BRANCO = (255, 255, 255)
# VERDE = (0, 255, 0)

# # Dino
# dino = pygame.Rect(50, 300, 50, 50)      
# gravidade = 0
# pulo = False

# # Obstáculos
# obstaculos = []
# tempo_obstaculo = 0

# # Loop principal
# rodando = True
# while rodando:
#     relogio.tick(60)
#     tela.fill(BRANCO)

#     # Eventos
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False

#     # Pulo
#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_SPACE] and not pulo:
#         gravidade = -15
#         pulo = True

#     gravidade += 1
#     dino.y += gravidade
#     if dino.y >= 300:
#         dino.y = 300
#         pulo = False

#     # Obstáculos
#     tempo_obstaculo += 1
#     if tempo_obstaculo > 90:
#         obstaculo = pygame.Rect(800, 320, 40, 40)
#         obstaculos.append(obstaculo)
#         tempo_obstaculo = 0

#     for obs in obstaculos[:]:
#         obs.x -= 10
#         if obs.x < -50:
#             obstaculos.remove(obs)
#         if dino.colliderect(obs):
#             print("Game Over")
#             rodando = False

#     # Desenhar
#     pygame.draw.rect(tela, VERDE, dino)
#     for obs in obstaculos:
#         pygame.draw.rect(tela, PRETO, obs)

#     pygame.display.flip()

# pygame.quit()




import pygame
import time
import random


codigo_secreto = 12345678


# Inicialização do pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensões da tela
largura = 600
altura = 400

# Tamanho do bloco da cobra e velocidade
tamanho_bloco = 20
velocidade = 10

# Fonte
fonte = pygame.font.SysFont("bahnschrift", 25)
placar_fonte = pygame.font.SysFont("comicsansms", 35)

# Cria a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Função do placar
def mostrar_pontuacao(pontos):
    valor = placar_fonte.render(f"Pontuação: {pontos}", True, amarelo)
    tela.blit(valor, [10, 10])

# Função da cobra
def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], tamanho_bloco, tamanho_bloco])

# Mensagem final
def mensagem_final(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

# Loop principal
def gameLoop():
    fim_de_jogo = False
    game_over = False

    x = largura / 2
    y = altura / 2
    x_mudanca = 0
    y_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not fim_de_jogo:

        while game_over:
            tela.fill(azul)
            mensagem_final("Você perdeu! Pressione C para jogar novamente ou Q para sair", vermelho)
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_de_jogo = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True

        x += x_mudanca
        y += y_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        corpo_cobra = []
        corpo_cobra.append(x)
        corpo_cobra.append(y)
        lista_cobra.append(corpo_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for bloco in lista_cobra[:-1]:
            if bloco == corpo_cobra:
                game_over = True

        desenhar_cobra(tamanho_bloco, lista_cobra)
        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

# Executa o jogo
gameLoop()