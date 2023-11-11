import pygame,random
import sys
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.randomize()
    
    def draw_food(self):
        apple_image = pygame.image.load('applee.png')
        apple_image = pygame.transform.scale(apple_image, (cell_size, cell_size))
        food_rect = apple_image.get_rect() 
        food_rect.topleft = (int(self.pos.x * cell_size), int(self.pos.y * cell_size))
        screen.blit(apple_image, food_rect) 

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
            for block in self.body:
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
                pygame.draw.rect(screen,(33,75,1),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()


pygame.init()
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_d:
                main_game.snake.direction = Vector2(1,0)
        

    screen.fill((190,210,50))    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)