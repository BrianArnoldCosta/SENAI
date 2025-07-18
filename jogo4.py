import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
         
        screen.fill((255, 255, 255))

        screen.blit(get_image('mdadsa.jpg'), (0, 0))

        #Atualiza a tela com as alterações feitas
        pygame.display.flip()
        clock.tick(60)