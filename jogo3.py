import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Círculo que reaparece nas bordas")

done = False
cor = True
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
raio = 40

fps = pygame.time.Clock()

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            cor = not cor

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    # Se sair pela esquerda, aparece na direita
    if x + raio < 0:
        x = SCREEN_WIDTH + raio
    # Se sair pela direita, aparece na esquerda
    elif x - raio > SCREEN_WIDTH:
        x = -raio

    # Se sair por cima, aparece embaixo
    if y + raio < 0:
        y = SCREEN_HEIGHT + raio
    # Se sair por baixo, aparece em cima
    elif y - raio > SCREEN_HEIGHT:
        y = -raio

    screen.fill((255, 255, 255))

    color = (255, 0, 0) if cor else (255, 100, 100)
    pygame.draw.circle(screen, color, (x, y), raio)

    pygame.display.flip() 
    fps.tick(200)
