import pygame
import random
import os
import time

pygame.font.init()  # initializing font class

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('pictures', 'background_sized.png')),
                                    (WIDTH, HEIGHT))
LOGO = pygame.image.load(os.path.join("pictures", "logo.png"))

# Animals
TOAD = pygame.image.load(os.path.join("pictures", "toad.png"))
WASP = pygame.image.load(os.path.join("pictures", "wasp.png"))
HORNET = pygame.image.load(os.path.join("pictures", "hornet.png"))
BUG = pygame.image.load(os.path.join("pictures", "bug.png"))
FLY = pygame.image.load(os.path.join("pictures", "fly.png"))
SNAIL = pygame.image.load(os.path.join("pictures", "snail.png"))
EARTHWORM = pygame.image.load(os.path.join("pictures", "earthworm.png"))
LADYBUG = pygame.image.load(os.path.join("pictures", "ladybug.png"))
MOSQUITO = pygame.image.load(os.path.join("pictures", "mosquito.png"))

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


class Creature():
    def __init__(self, species, x, y):
        self.species = species
        self.x = x
        self.y = y

        IMG_MAP = {
            "toad": (TOAD),
            "wasp": (WASP),
            "hornet": (HORNET),
            "bug": (BUG),
            "fly": (FLY),
            "snail": (SNAIL),
            "earthworm": (EARTHWORM),
            "ladybug": (LADYBUG),
            "mosquito": (MOSQUITO)
        }
        SPEED_MAP = {
            "toad": (5),
            "wasp": (2),
            "hornet": (1),
            "bug": (2),
            "fly": (2),
            "snail": (1),
            "earthworm": (2),
            "ladybug": (1),
            "mosquito": (1)
        }
        LP_MAP = {
            "toad": (3),
            "wasp": (-1),
            "hornet": (-2),
            "bug": (-1),
            "fly": (0),
            "snail": (0),
            "earthworm": (1),
            "ladybug": (0),
            "mosquito": (0)
        }
        SP_MAP = {
            "toad": (0),
            "wasp": (-2),
            "hornet": (-4),
            "bug": (-2),
            "fly": (1),
            "snail": (1),
            "earthworm": (2),
            "ladybug": (1),
            "mosquito": (1)
        }

        self.speed = SPEED_MAP[species]

        self.lp = LP_MAP[species]
        self.sp = SP_MAP[species]
        self.creature_img = IMG_MAP[species]
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.cool_down_counter = 0
        self.max_lp = 3


    def move(self):

        if (self.species == "wasp") or (self.species == "fly") or (self.species == "mosquito"):

            if self.x <= 0:
                self.speed *= -1

            if self.x >= WIDTH - 50:
                self.speed *= -1

            self.y += abs(self.speed)/2
            self.x += self.speed

        elif (self.species == "bug") or (self.species == "snail") or (self.species == "ladybug"):

            if self.x <= 0:
                self.y += 120
                self.speed *= -1

            if self.x >= WIDTH - 50:
                self.y += 80
                self.speed *= -1

            self.x += self.speed

        else:
            self.y += self.speed

    def draw(self):
        WINDOW.blit(self.creature_img, (self.x, self.y))

    def get_width(self):
        return self.creature_img.get_width()

    def get_height(self):
        return self.creature_img.get_height()

    def collision(self, obj):
        return collide(obj, self)




def collide(obj1, obj2):
    """ return a tuple with values of overlap of two objects

    :param obj1: (class Creature object) first object to check collision for
    :param obj2: (class Creature object) second object
    :return: values of overlap
    """

    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)

    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60

    lives = 3
    score = 0
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 60)

    list_of_creatures = [None,"wasp",'hornet', 'bug', 'fly', 'snail', 'earthworm', 'ladybug', 'mosquito']
    creatures = []

    toad = Creature('toad',500,630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():

        # Background
        WINDOW.blit(BACKGROUND, (0, 0))

        # Labels in the corners
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))  # get_width() return the width of surfaces

        # Creatures
        for creature in creatures:
            creature.draw()

        toad.draw()

        if lost:
            lost_label = lost_font.render("You lost!",1,(255,255,255))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 400))



        pygame.display.update()


    while run:

        clock.tick(FPS)
        redraw_window()


        if lives <= 0 or toad.lp <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 4:
                run = False
            else:
                continue


        for i in range(1):
            species = random.choices(list_of_creatures, weights=[2000,4,1,2,2,1,1,1,2], k=1)
            if species[0] == None:
                pass
            else:
                creature = Creature(species[0], random.randrange(10, WIDTH - 60), random.randrange(-500, -50))
                creatures.append(creature)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and toad.x > 0:
            toad.x -= toad.speed
        if keys[pygame.K_RIGHT] and toad.x + toad.get_width() < WIDTH:
            toad.x += toad.speed


        # Moving creatures and removing them whem they hit the ground
        for creature in creatures[:]:
            creature.move()

            if creature.collision(toad):

                if (score + creature.sp) >= 0:
                    score += creature.sp

                if (lives + creature.lp) <= 3:
                    toad.lp += creature.lp
                    lives += creature.lp


                creatures.remove(creature)


            if creature.y + creature.get_height() > HEIGHT - 80:
                if creature.species == "fly" or creature.species == "mosquito" or creature.species == "ladybug" or creature.species == "snail" or creature.species == "earthworm":
                    lives -= 1
                creatures.remove(creature)





main()
