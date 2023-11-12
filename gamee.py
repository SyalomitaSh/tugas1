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

        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()

        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))

        self.tail_up = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_left.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_right.png').convert_alpha()

        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        self.body_datar = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_atas = pygame.image.load('body_horizontal.png').convert_alpha()

        self.body_datar = pygame.transform.scale(self.body_datar, (cell_size, cell_size))
        self.body_atas = pygame.transform.scale(self.body_atas, (cell_size, cell_size))

        self.belokkananatas = pygame.image.load('body_tr.png').convert_alpha()
        self.belokkananbawah = pygame.image.load('body_tl.png').convert_alpha()
        self.belokkiriatas = pygame.image.load('body_br.png').convert_alpha()
        self.belokkiribawah = pygame.image.load('body_bl.png').convert_alpha()

        self.belokkananatas = pygame.transform.scale(self.belokkananatas, (cell_size, cell_size))
        self.belokkananbawah = pygame.transform.scale(self.belokkananbawah, (cell_size, cell_size))
        self.belokkiriatas = pygame.transform.scale(self.belokkiriatas, (cell_size, cell_size))
        self.belokkiribawah = pygame.transform.scale(self.belokkiribawah, (cell_size, cell_size))


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
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_datar, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_atas, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.belokkananbawah, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.belokkiribawah, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.belokkananatas, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.belokkiriatas, block_rect)



    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head =self.head_right
        elif head_relation == Vector2(0,1): self.head =self.head_up
        elif head_relation == Vector2(0,-1): self.head =self.head_down

    def update_tail_graphics(self):
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
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

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

    def game_over(self):
        pygame.quit()
        sys.exit() 

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen,grass_color,grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3 )
        score_surface = game_font.render(score_text, True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface, score_rect)


    

pygame.init()
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Arial", 25)


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