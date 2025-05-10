import pygame
import random

# Inicializar
pygame.init()
LARGURA, ALTURA = 800, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dino Runner")
relogio = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Dino
dino = pygame.Rect(50, 300, 50, 50)
gravidade = 0
pulo = False

# Obstáculos
obstaculos = []
tempo_obstaculo = 0

# Loop principal
rodando = True
while rodando:
    relogio.tick(60)
    tela.fill(BRANCO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Pulo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE] and not pulo:
        gravidade = -15
        pulo = True

    gravidade += 1
    dino.y += gravidade
    if dino.y >= 300:
        dino.y = 300
        pulo = False

    # Obstáculos
    tempo_obstaculo += 1
    if tempo_obstaculo > 90:
        obstaculo = pygame.Rect(800, 320, 40, 40)
        obstaculos.append(obstaculo)
        tempo_obstaculo = 0

    for obs in obstaculos[:]:
        obs.x -= 10
        if obs.x < -50:
            obstaculos.remove(obs)
        if dino.colliderect(obs):
            print("Game Over")
            rodando = False

    # Desenhar
    pygame.draw.rect(tela, VERDE, dino)
    for obs in obstaculos:
        pygame.draw.rect(tela, PRETO, obs)

    pygame.display.flip()

pygame.quit()

