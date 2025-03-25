import pygame
import time
import random

pygame.init()

colour_1 = (255,255,255)
colour_2 = (255,255,102)
colour_3 = (0,0,0)
colour_4 = (213,200,80)
colour_5 = (0,255,0)
colour_6 = (255,0,0)

box_len = 900
box_height = 600

add_caption = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SNAKE GAME")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 15

dispaly_style = pygame.font.SysFont("arial", 30, "bold")
score_font = pygame.font.SysFont("arial", 45, "bold")

def final_score(score):
    value = score_font.render("Enjoy the snake game -------- Your score is :" + str(score), True, colour_2)
    add_caption.blit(value, [box_len / 6, box_height / 3])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(add_caption, colour_5, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    x1 = box_len / 2
    y1 = box_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            add_caption.fill(colour_3)
            final_score(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= box_len or x1 < 0 or y1 >= box_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        add_caption.fill(colour_4)
        pygame.draw.rect(add_caption, colour_6, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        timer.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
