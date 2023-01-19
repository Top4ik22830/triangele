import pygame, sys
from pygame.locals import QUIT

pygame.init()
WINDOW = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Название игры")
WINDOW.fill((123,123,2))

player = pygame.Rect(100,100, 50, 50)
pygame.draw.rect(WINDOW, (13, 245, 25), player)
FPS = pygame.time.Clock()
step = 5


while True:
    WINDOW.fill((123,123,2))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 1
    elif keys[pygame.K_RIGHT]:
        player.x += 1
    if keys[pygame.K_DOWN]:
        player.y += 1
    elif keys[pygame.K_UP]:
        player.y -= 1



    pygame.draw.rect(WINDOW, (13,245, 25), player)
    pygame.display.update()
    FPS.tick(40)
