import pygame, time, random

pygame.init()
screen = pygame.display.set_mode((1000,400))                           
pygame.display.set_caption("LLAMA GAME")
clock = pygame.time.Clock()

quit_game = False
colors = {"green":(188, 227, 199), "dark_green":(0, 102, 51),
          "blue":(32, 32, 200),"black":(0, 0, 0),"white":(255, 255, 255),
          "lightblue":(176, 197, 245)}

kjhfkjdsngb
dba
gbg
dd
b
fsbn
etgr
tb
ntq
ebgheqarjeafdbvakjfdn

            if event.key == pygame.K_ESCAPE:
                quit_game = True
    
    draw_background()

    for items in cacti_list:
        items.draw()
        items.move()
        
    pygame.display.update()
    clock.tick(10)
