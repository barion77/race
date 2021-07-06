import pygame as pg
import math
import sys
import random

pg.init()
pg.font.init()


all_speed = 6 

# Victory
vin_img = pg.image.load("Pygame\\race\\vin.png")
def vin_text(x, y):
    screen.blit(vin_img, (x, y))

# Text Game Over
game_over_img = pg.image.load("Pygame\\race\\text.png")

def game_over(x, y):
    screen.blit(game_over_img, (x, y))


# Score 
score = 0
font_score = pg.font.SysFont("chiller", 54)
def show_score(x, y):
    score_text = font_score.render("Score: {}".format(score), True, (255, 64, 100))
    screen.blit(score_text, (x, y))

def count_score(file_txt, current_score): 

    file_score = open(file_txt, 'r')
    score_in_file = file_score.read()

    if int(score_in_file) < current_score:
        new_file = open(file_txt, 'w')
        new_file.write(str(current_score))
        new_file.close()
        return True
    else:
        return False 

        
score_font = pg.font.SysFont("chiller", 54) 
def text_score_in_end(x, y):
    score_in = open("Pygame\\race\score.txt", "r")
    last_score = score_in.read()
    score_in_end = score_font.render("You record: {0}".format(last_score), True, (198, 10, 10))
    screen.blit(score_in_end, (x, y)) 

# Screen and Backgraund
size = width, height = 800, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Race")
backgraund = pg.image.load("Pygame\\race\\backgraund.png") 
backgraund_y = 0
backgraund_y2 = - 600
backgraund_y_change = all_speed
backgraund_y_change2 = all_speed

def backgraund_move(y):
    screen.blit(backgraund, (0, y))


# Player
player_img = pg.image.load("Pygame\\race\player.png")
player_x = 350
player_y = 500
player_x_change = 0
player_y_change = 0
speed = 4   


def player(x, y):
    screen.blit(player_img, (x, y))

# Dangerous 
stone_img = pg.image.load("Pygame\\race\\stone.png")
stone_x = random.randint(69, 699)
stone_x2 = random.randint(70, 700) 
stone_y = -(random.randint(31, 129))
stone_y2 = -(random.randint(30, 128))

def stone(x, y):
    screen.blit(stone_img, (x, y))

# Collision
def collide(stone_x, stone_y, player_x, player_y):
    rect = math.sqrt((math.pow(stone_x - player_x, 2) + math.pow(stone_y - player_y, 2)))
    if rect < 64:
        return True
    else:
        return False

running = True 
while running:

    
    screen.fill((0, 0, 0))
    if backgraund_y == 600:
        backgraund_y = 0
        backgraund_move(backgraund_y)
    else:
        backgraund_move(backgraund_y)
        backgraund_y += backgraund_y_change 

    if backgraund_y2 >= 0:
        backgraund_y2 = - 600
        backgraund_move(backgraund_y2)
        
    else:
        backgraund_move(backgraund_y2) 
        backgraund_y2 += backgraund_y_change2
        

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            player_x_change = speed

        if event.key == pg.K_LEFT:
         player_x_change = -speed

    if event.type == pg.KEYUP:
        if event.key == pg.K_RIGHT or pg.K_LEFT:
            player_x_change = 0

    if player_x <= 64:
        player_x = 64
    
    if player_x >= 670:
        player_x = 670 



    stone_y += all_speed
    stone_y2 += all_speed
    if stone_y >= 600:
        stone_y = -32
        stone_y2 = -64
        stone(stone_x, stone_y)
        stone_y = -(random.randint(31, 129))
        stone_y2 = -(random.randint(30, 128))
        stone_x = random.randint(70, 700)  
    else:
        stone(stone_x, stone_y) 
        stone(stone_x2, stone_y2)


    # Collision
    player(player_x, player_y)
    if collide(stone_x, stone_y, player_x, player_y):
        all_speed = 0
        player_x_change = 0
        player_y_change = 0 
        backgraund_y_change = 0
        backgraund_y_change2 = 0
        verify_score = count_score("Pygame\\race\score.txt", score)
        score = -1
        game_over(120, 200)
    else:
        all_speed += 0.01

    player(player_x, player_y)
    if collide(stone_x2, stone_y2, player_x, player_y):
        all_speed = 0
        player_x_change = 0
        player_y_change = 0 
        backgraund_y_change = 0
        backgraund_y_change2 = 0
        verify_score = count_score("Pygame\\race\score.txt", score)
        score = -1
        game_over(120, 200)
    else:
        all_speed += 0.01

    text_score_in_end(48, 10)
    player_y -= player_y_change
    player_x += player_x_change
    player_y_change = 0
    if player_y <= 0:
        all_speed = 0
        speed = 0
        player_x_change = 0
        player_y_change = 0 
        backgraund_y_change = 0
        backgraund_y_change2 = 0
        verify_score = count_score("Pygame\\race\score.txt", score)
        score = -1
        vin_text(220, 200) 
    else:
        player_y_change = 0.01

    # Score 
    score += 1
    show_score(565, 5)
    pg.display.update()