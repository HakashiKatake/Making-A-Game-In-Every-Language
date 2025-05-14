import pygame
from pygame.locals import * 

clock = pygame.time.Clock()
fps = 60



screen_width = 600
screen_height = 800

bg = pygame.image.load('img/bg.png')

def draw_bg():
    screen.blit(bg, (0,0))


screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Pygame Window") 

run = True
while run:


    clock.tick(fps) # 60 FPS
    #draw background
    draw_bg()

    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

pygame.quit()