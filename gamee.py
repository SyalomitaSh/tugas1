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
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('headatas.png').convert_alpha()
        self.head_down = pygame.image.load('headbawah.png').convert_alpha()
        self.head_right = pygame.image.load('headkanan.png').convert_alpha()
        self.head_left = pygame.image.load('headkiri.png').convert_alpha()

        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))

        self.tail_up = pygame.image.load('tailatas.png').convert_alpha()
        self.tail_down = pygame.image.load('tailbawah.png').convert_alpha()
        self.tail_right = pygame.image.load('tailkanan.png').convert_alpha()
        self.tail_left = pygame.image.load('tailkiri.png').convert_alpha()

        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        self.datar = pygame.image.load('bodyatas.png').convert_alpha()
        self.atas = pygame.image.load('bodymendatar.png').convert_alpha()

        self.belokkananatas = pygame.image.load('belokkananatas.png').convert_alpha()
        self.belokkananbawah = pygame.image.load('belokkananbawah.png').convert_alpha()
        self.belokkiriatas = pygame.image.load('belokkiriatas.png').convert_alpha()
        self.belokkiribawah = pygame.image.load('belokkiribawah.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            else:
                pygame.draw.rect(screen,(33,75,1),block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head =self.head_right
        elif head_relation == Vector2(0,1): self.head =self.head_up
        elif head_relation == Vector2(0,-1): self.head =self.head_down

    def update_tail_graphics(self):
        # 
        if len(self.body) >= 2:
            tail_relation = self.body[-1] - self.body[-2]

        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail =self.tail_right
        elif tail_relation == Vector2(0,1): self.tail =self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail =self.tail_down


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
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over():
        pygame.quit()
        sys.exit() 


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
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(1,0)
        

    screen.fill((190,210,50))    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)