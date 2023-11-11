import pygame,random
import sys
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)
    
    def draw_food(self):
        apple_image = pygame.image.load('applee.png')
        apple_image = pygame.transform.scale(apple_image, (cell_size, cell_size))
        food_rect = apple_image.get_rect() 
        food_rect.topleft = (int(self.pos.x * cell_size), int(self.pos.y * cell_size))
        screen.blit(apple_image, food_rect) 


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
            for block in self.body:
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
                pygame.draw.rect(screen,(33,75,1),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

pygame.init()
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

food = Food()
snake = Snake() 

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_a:
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_d:
                snake.direction = Vector2(1,0)
        

    screen.fill((190,210,50))    
    food.draw_food()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)