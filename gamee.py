import pygame,random
import sys
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_food(self):
            food_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            pygame.draw.rect(screen,('blue'),food_rect)



pygame.init()
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

food = Food()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((190,210,50))    
    food.draw_food()
    pygame.display.update()
    clock.tick(60)