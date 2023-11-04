import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((450,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((190,210,234))
    screen.blit(test_surface,(200,250))        
    pygame.display.update()
    clock.tick(60)