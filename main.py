import pygame
import random
import os
import time
pygame.font.init()  #initializing font class

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('pictures','background_sized.png')), (WIDTH,HEIGHT))
LOGO = pygame.image.load(os.path.join("pictures","logo.png"))

# Animals
TOAD = pygame.image.load(os.path.join("pictures","toad.png"))
WASP = pygame.image.load(os.path.join("pictures","wasp.png"))

# Game name and logo
pygame.display.set_caption("Toad Game")
pygame.display.set_icon(LOGO)

""" 
class Toad():
    def __init__(self, x, y, score=0):
        self.x = x
        self.y = y
        self.score = score
        self.toad_img = pygame.image.load( (os.path.join("pictures","toad.png")) )
        
        def draw(self, placement):
            pygame.draw()
"""
class Enemy():
    def __init__(self, x, y, speed, lp=-1, sp=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.lp = lp
        self.sp = sp
        self.creature_img = None
        self.cool_down_counter = 0

    def draw(self, placement):
        WINDOW.blit(self.creature_img, (self.x, self.y))

    def get_width(self):
        return self.creature_img.get_width()

    def get_height(self):
        return self.creature_img.get_height()


class Toad(Enemy):
    def __init__(self, x, y, speed, lp=3, sp=0):
        super().__init__(x,y,speed, lp, sp)
        self.creature_img = TOAD
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.max_lp = lp



"""
class Toad:
    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        
"""



def main():

    run = True
    FPS = 60

    lives = 3
    score = 0

    main_font= pygame.font.SysFont("comicsans", 40)

    wasp_velocity = 4

    toad = Toad(500,630, 5)


    clock = pygame.time.Clock()

    def redraw_window():

        WINDOW.blit(BACKGROUND, (0,0))


        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Score: {score}", 1 , (255,255,255))

        WINDOW.blit(lives_label, (10,10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))   # get_width() return the width of surfaces

        toad.draw(WINDOW)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and toad.x > 0:
            toad.x -= toad.speed
        if keys[pygame.K_RIGHT] and toad.x + toad.get_width() < WIDTH:
            toad.x += toad.speed




main()
