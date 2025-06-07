import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

done= False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (250, 250, 100),
                pygame.Rect(50, 50, 50, 50))

    pygame.display.flip() 