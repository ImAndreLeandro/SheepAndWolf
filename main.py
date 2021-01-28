import pygame
import time
import math

pygame.init()   
res_x = 1280
res_y = 720
screen = pygame.display.set_mode((res_x,res_y))

background_phase = 0
turn = 0
lobo_selected = 0

pygame.display.set_caption("Sheef & Wolf")
bg_img = pygame.image.load('background1_0.png')
bt_play = pygame.image.load('play.png')
bt_exit = pygame.image.load('exit.png')
bg_img2 = pygame.image.load('background2_0.png')
player_icon = pygame.image.load('player.png')
wolf_icon = pygame.image.load('wolf.png')
player_select = pygame.image.load('block_player.png')
wolf_select = pygame.image.load('block_wolf.png')
wolf_choose = pygame.image.load('select_wolf.png')
bg_img3 = pygame.image.load('background3_0.png')
sheep_lost = pygame.image.load('sheep_lost.png')
wolves_lost = pygame.image.load('wolves_lost.png')

block_size = (70, 66)
player_x = 4
player_y = 7
wolf1_x = 1
wolf1_y = 0
wolf2_x = 3
wolf2_y = 0
wolf3_x = 5
wolf3_y = 0
wolf4_x = 7
wolf4_y = 0

screen.fill((0, 0, 0))
        
screen.blit(bg_img, (0,0))
screen.blit(bt_play, (492,529))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (background_phase == 1):
            if(player_x == 0):
                if(wolf1_x == player_x + 1 and wolf1_y == player_y - 1 or wolf2_x == player_x + 1 and wolf2_y == player_y - 1 or wolf3_x == player_x + 1 and wolf3_y == player_y - 1 or wolf4_x == player_x + 1 and wolf4_y == player_y - 1):
                    if(wolf1_x == player_x + 1 and wolf1_y == player_y + 1 or wolf2_x == player_x + 1 and wolf2_y == player_y + 1 or wolf3_x == player_x + 1 and wolf3_y == player_y + 1 or wolf4_x == player_x + 1 and wolf4_y == player_y + 1):
                        background_phase = 2
            elif (player_x == 7):
                if (wolf1_x == player_x - 1 and wolf1_y == player_y - 1 or wolf2_x == player_x - 1 and wolf2_y == player_y - 1 or wolf3_x == player_x - 1 and wolf3_y == player_y - 1 or wolf4_x == player_x - 1 and wolf4_y == player_y - 1):
                    if (wolf1_x == player_x - 1 and wolf1_y == player_y + 1 or wolf2_x == player_x - 1 and wolf2_y == player_y + 1 or wolf3_x == player_x - 1 and wolf3_y == player_y + 1 or wolf4_x == player_x - 1 and wolf4_y == player_y + 1):
                        background_phase = 2
            elif (wolf1_x == player_x - 1 and wolf1_y == player_y - 1 or wolf2_x == player_x - 1 and wolf2_y == player_y - 1 or wolf3_x == player_x - 1 and wolf3_y == player_y - 1 or wolf4_x == player_x - 1 and wolf4_y == player_y - 1):
                if(wolf1_x == player_x + 1 and wolf1_y == player_y - 1 or wolf2_x == player_x + 1 and wolf2_y == player_y - 1 or wolf3_x == player_x + 1 and wolf3_y == player_y - 1 or wolf4_x == player_x + 1 and wolf4_y == player_y - 1):
                    if(wolf1_x == player_x + 1 and wolf1_y == player_y + 1 or wolf2_x == player_x + 1 and wolf2_y == player_y + 1 or wolf3_x == player_x + 1 and wolf3_y == player_y + 1 or wolf4_x == player_x + 1 and wolf4_y == player_y + 1):
                        if (wolf1_x == player_x - 1 and wolf1_y == player_y + 1 or wolf2_x == player_x - 1 and wolf2_y == player_y + 1 or wolf3_x == player_x - 1 and wolf3_y == player_y + 1 or wolf4_x == player_x - 1 and wolf4_y == player_y + 1):
                            background_phase = 2
                            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (turn == 0):
                    if (mouse[0] >= (392 + ((player_x - 1)*62)) and mouse[0] <= (392 + 62 + ((player_x - 1)*62)) and mouse[1] >= (195 + ((player_y - 1)*62)) and mouse[1] <= (195 + 62 + ((player_y - 1)*62))):
                        if(player_x != 0):
                            player_x = player_x - 1
                            player_y = player_y - 1
                            turn = 1
                    if (mouse[0] >= (392 + ((player_x + 1)*62)) and mouse[0] <= (392 + 62 + ((player_x + 1)*62)) and mouse[1] >= (195 + ((player_y - 1)*62)) and mouse[1] <= (195 + 62 + ((player_y - 1)*62))):
                        if(player_x != 7):
                            player_x = player_x + 1
                            player_y = player_y - 1
                            turn = 1
                        
                if (turn == 1):
                    if(player_x == 0):
                        if(wolf1_x == player_x + 1 and wolf1_y == player_y - 1 or wolf2_x == player_x + 1 and wolf2_y == player_y - 1 or wolf3_x == player_x + 1 and wolf3_y == player_y - 1 or wolf4_x == player_x + 1 and wolf4_y == player_y - 1):
                            if(wolf1_x == player_x + 1 and wolf1_y == player_y + 1 or wolf2_x == player_x + 1 and wolf2_y == player_y + 1 or wolf3_x == player_x + 1 and wolf3_y == player_y + 1 or wolf4_x == player_x + 1 and wolf4_y == player_y + 1):
                                background_phase = 2
                    elif (player_x == 7):
                        if (wolf1_x == player_x - 1 and wolf1_y == player_y - 1 or wolf2_x == player_x - 1 and wolf2_y == player_y - 1 or wolf3_x == player_x - 1 and wolf3_y == player_y - 1 or wolf4_x == player_x - 1 and wolf4_y == player_y - 1):
                            if (wolf1_x == player_x - 1 and wolf1_y == player_y + 1 or wolf2_x == player_x - 1 and wolf2_y == player_y + 1 or wolf3_x == player_x - 1 and wolf3_y == player_y + 1 or wolf4_x == player_x - 1 and wolf4_y == player_y + 1):
                                background_phase = 2
                    elif (wolf1_x == player_x - 1 and wolf1_y == player_y - 1 or wolf2_x == player_x - 1 and wolf2_y == player_y - 1 or wolf3_x == player_x - 1 and wolf3_y == player_y - 1 or wolf4_x == player_x - 1 and wolf4_y == player_y - 1):
                        if(wolf1_x == player_x + 1 and wolf1_y == player_y - 1 or wolf2_x == player_x + 1 and wolf2_y == player_y - 1 or wolf3_x == player_x + 1 and wolf3_y == player_y - 1 or wolf4_x == player_x + 1 and wolf4_y == player_y - 1):
                            if(wolf1_x == player_x + 1 and wolf1_y == player_y + 1 or wolf2_x == player_x + 1 and wolf2_y == player_y + 1 or wolf3_x == player_x + 1 and wolf3_y == player_y + 1 or wolf4_x == player_x + 1 and wolf4_y == player_y + 1):
                                if (wolf1_x == player_x - 1 and wolf1_y == player_y + 1 or wolf2_x == player_x - 1 and wolf2_y == player_y + 1 or wolf3_x == player_x - 1 and wolf3_y == player_y + 1 or wolf4_x == player_x - 1 and wolf4_y == player_y + 1):
                                    background_phase = 2
                                    
                    if (player_y == 0):
                        background_phase = 3
                    
                    if (mouse[0] >= (392 + (wolf1_x*62)) and mouse[0] <= (392 + 62 + (wolf1_x*62)) and mouse[1] >= (195 + (wolf1_y*62)) and mouse[1] <= (195 + 62 + (wolf1_y*62))):
                        lobo_selected = 1
                        turn = 2
                    if (mouse[0] >= (392 + (wolf2_x*62)) and mouse[0] <= (392 + 62 + (wolf2_x*62)) and mouse[1] >= (195 + (wolf2_y*62)) and mouse[1] <= (195 + 62 + (wolf2_y*62))):
                        lobo_selected = 2
                        turn = 2
                    if (mouse[0] >= (392 + (wolf3_x*62)) and mouse[0] <= (392 + 62 + (wolf3_x*62)) and mouse[1] >= (195 + (wolf3_y*62)) and mouse[1] <= (195 + 62 + (wolf3_y*62))):
                        lobo_selected = 3
                        turn = 2
                    if (mouse[0] >= (392 + (wolf4_x*62)) and mouse[0] <= (392 + 62 + (wolf4_x*62)) and mouse[1] >= (195 + (wolf4_y*62)) and mouse[1] <= (195 + 62 + (wolf4_y*62))):
                        lobo_selected = 4
                        turn = 2
                        
                if (turn == 2):
                    if (mouse[0] >= (392 + ((wolf1_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf1_x - 1)*62)) and mouse[1] >= (195 + ((wolf1_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf1_y + 1)*62))):
                        if (lobo_selected == 1 and wolf1_x != 0):
                            turn = 0
                            wolf1_x = wolf1_x - 1
                            wolf1_y = wolf1_y + 1
                    if (mouse[0] >= (392 + ((wolf1_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf1_x + 1)*62)) and mouse[1] >= (195 + ((wolf1_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf1_y + 1)*62))):
                        if (lobo_selected == 1 and wolf1_x != 7):
                            turn = 0
                            wolf1_x = wolf1_x + 1
                            wolf1_y = wolf1_y + 1
                    if (mouse[0] >= (392 + ((wolf2_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf2_x - 1)*62)) and mouse[1] >= (195 + ((wolf2_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf2_y + 1)*62))):
                        if (lobo_selected == 2 and wolf2_x != 0):
                            turn = 0
                            wolf2_x = wolf2_x - 1
                            wolf2_y = wolf2_y + 1
                    if (mouse[0] >= (392 + ((wolf2_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf2_x + 1)*62)) and mouse[1] >= (195 + ((wolf2_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf2_y + 1)*62))):
                        if (lobo_selected == 2 and wolf2_x != 7):
                            turn = 0
                            wolf2_x = wolf2_x + 1
                            wolf2_y = wolf2_y + 1
                    if (mouse[0] >= (392 + ((wolf3_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf3_x - 1)*62)) and mouse[1] >= (195 + ((wolf3_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf3_y + 1)*62))):
                        if (lobo_selected == 3 and wolf3_x != 0):
                            turn = 0
                            wolf3_x = wolf3_x - 1
                            wolf3_y = wolf3_y + 1
                    if (mouse[0] >= (392 + ((wolf3_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf3_x + 1)*62)) and mouse[1] >= (195 + ((wolf3_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf3_y + 1)*62))):
                        if (lobo_selected == 3 and wolf3_x != 7):
                            turn = 0
                            wolf3_x = wolf3_x + 1
                            wolf3_y = wolf3_y + 1
                    if (mouse[0] >= (392 + ((wolf4_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf4_x - 1)*62)) and mouse[1] >= (195 + ((wolf4_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf4_y + 1)*62))):
                        if (lobo_selected == 4 and wolf4_x != 0):
                            turn = 0
                            wolf4_x = wolf4_x - 1
                            wolf4_y = wolf4_y + 1
                    if (mouse[0] >= (392 + ((wolf4_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf4_x + 1)*62)) and mouse[1] >= (195 + ((wolf4_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf4_y + 1)*62))):
                        if (lobo_selected == 4 and wolf4_x != 7):
                            turn = 0
                            wolf4_x = wolf4_x + 1
                            wolf4_y = wolf4_y + 1
                    
                    
        
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if(mouse[0] >= 492 and mouse[0] <= 789 and mouse[1] >= 529 and mouse[1] <= 644):
                    background_phase = 1
                    turn = 0
                    lobo_selected = 0
                    player_x = 4
                    player_y = 7
                    wolf1_x = 1
                    wolf1_y = 0
                    wolf2_x = 3
                    wolf2_y = 0
                    wolf3_x = 5
                    wolf3_y = 0
                    wolf4_x = 7
                    wolf4_y = 0
                if(mouse[0] >= 554 and mouse[0] <= 727 and mouse[1] >= 645 and mouse[1] <= 720):
                    running = False
    

    screen.fill((0, 0, 0))
            
    if (background_phase == 1):
        screen.blit(bg_img2, (0,0))
        
        if (turn == 0):
            if(player_x != 0):
                if(not(wolf1_x == player_x - 1 and wolf1_y == player_y - 1 or wolf2_x == player_x - 1 and wolf2_y == player_y - 1 or wolf3_x == player_x - 1 and wolf3_y == player_y - 1 or wolf4_x == player_x - 1 and wolf4_y == player_y - 1)):
                    screen.blit(player_select, (392 + ((player_x - 1)*62), 195 + ((player_y - 1)*62)))
            if(player_x != 7):
                if(not(wolf1_x == player_x + 1 and wolf1_y == player_y - 1 or wolf2_x == player_x + 1 and wolf2_y == player_y - 1 or wolf3_x == player_x + 1 and wolf3_y == player_y - 1 or wolf4_x == player_x + 1 and wolf4_y == player_y - 1)):
                    screen.blit(player_select, (392 + ((player_x + 1)*62), 195 + ((player_y - 1)*62)))
        
        if (turn == 1):
            screen.blit(wolf_choose, (392 + (wolf1_x*62), 195 + (wolf1_y*62)))
            screen.blit(wolf_choose, (392 + (wolf2_x*62), 195 + (wolf2_y*62)))
            screen.blit(wolf_choose, (392 + (wolf3_x*62), 195 + (wolf3_y*62)))
            screen.blit(wolf_choose, (392 + (wolf4_x*62), 195 + (wolf4_y*62)))
            
        if (turn == 2):
            if (lobo_selected == 1):
                if(wolf1_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf1_x - 1)*62), 195 + ((wolf1_y + 1)*62)))
                if(wolf1_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf1_x + 1)*62), 195 + ((wolf1_y + 1)*62)))
            if (lobo_selected == 2):
                if(wolf2_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf2_x - 1)*62), 195 + ((wolf2_y + 1)*62)))
                if(wolf2_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf2_x + 1)*62), 195 + ((wolf2_y + 1)*62)))
            if (lobo_selected == 3):
                if(wolf3_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf3_x - 1)*62), 195 + ((wolf3_y + 1)*62)))
                if(wolf3_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf3_x + 1)*62), 195 + ((wolf3_y + 1)*62)))
            if (lobo_selected == 4):
                if(wolf4_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf4_x - 1)*62), 195 + ((wolf4_y + 1)*62)))
                if(wolf4_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf4_x + 1)*62), 195 + ((wolf4_y + 1)*62)))
        
        screen.blit(player_icon, (392 + (player_x*62), 195 + (player_y*62)))
        
        screen.blit(wolf_icon, (392 + (wolf1_x*62), 195 + (wolf1_y*62)))
        screen.blit(wolf_icon, (392 + (wolf2_x*62), 195 + (wolf2_y*62)))
        screen.blit(wolf_icon, (392 + (wolf3_x*62), 195 + (wolf3_y*62)))
        screen.blit(wolf_icon, (392 + (wolf4_x*62), 195 + (wolf4_y*62)))
    
    elif (background_phase == 2):
        screen.blit(bg_img3, (0,0))
        screen.blit(sheep_lost, (243, 245))
        screen.blit(bt_play, (496,538))
        screen.blit(bt_exit, (554,650))
    elif (background_phase == 3):
        screen.blit(bg_img3, (0,0))
        screen.blit(wolves_lost, (243, 245))
        screen.blit(bt_play, (496,538))
        screen.blit(bt_exit, (554,650))
    else:
        screen.blit(bg_img, (0,0))
        screen.blit(bt_play, (496,538))
        screen.blit(bt_exit, (554,650))
    pygame.display.update()
    
