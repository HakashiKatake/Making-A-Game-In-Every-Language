import pygame
from pygame.locals import * 

clock = pygame.time.Clock()
fps = 60



screen_width = 600
screen_height = 800

bg = pygame.image.load('img/bg.png')

def draw_bg():
    screen.blit(bg, (0,0))

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x ,y]


spaceship_group = pygame.sprite.Group()

spaceship = SpaceShip(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)





screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Space Invaders") 

run = True
while run:


    clock.tick(fps) # 60 FPS
    #draw background
    draw_bg()

    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    spaceship_group.draw(screen)

    pygame.display.update()

pygame.quit()