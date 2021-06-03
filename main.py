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


class Creature():

    def __init__(self, species, x, y):
        self.species = species
        self.x = x
        self.y = y

        SPEED_MAP = {
            "toad": (5),
            "wasp": (round(random.uniform(1.0,3.0), 1)),
            "hornet": (round(random.uniform(0.5,1.5), 1)),
            "bug": (round(random.uniform(0.5,1.5), 1)),
            "fly": (round(random.uniform(1.0,3.0), 1)),
            "snail": (round(random.uniform(0.5,1.0), 1)),
            "earthworm": (round(random.uniform(3.5,4.5), 1)),
            "ladybug": (round(random.uniform(1.0,1.5), 1)),
            "mosquito": (round(random.uniform(0.5,1.5), 1)),
        }
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
        LP_MAP = {
            "toad": (3),
            "wasp": (-1),
            "hornet": (-2),
            "bug": (-1),
            "fly": (0),
            "snail": (0),
            "earthworm": (1),
            "ladybug": (1),
            "mosquito": (0)
        }
        SP_MAP = {
            "toad": (0),
            "wasp": (0),
            "hornet": (0),
            "bug": (0),
            "fly": (2),
            "snail": (1),
            "earthworm": (4),
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


def rand_species(n, w_wasp, w_hornet, w_bug, w_fly, w_snail, w_earthworm, w_ladybug, w_mosquito):

    list_of_creatures = [None, "wasp", 'hornet', 'bug', 'fly', 'snail', 'earthworm', 'ladybug', 'mosquito']

    for i in range(1):
        species = random.choices(list_of_creatures,
                                 weights=[n, w_wasp, w_hornet, w_bug, w_fly, w_snail, w_earthworm, w_ladybug,w_mosquito],
                                 k=1)
    return species


def rand_spawn_place(WIDTH):

    height = -200
    r = abs(height) // 50
    c = WIDTH // 50
    r_list = [i+1 for i in range(r)]
    c_list = [i+1 for i in range(c)]

    rand_c = random.choice(r_list) * 50 - 50
    rand_r = random.choice(c_list) * (-50) - 50
    if rand_c == 0:
        rand_c += 1
    elif rand_r == WIDTH - 50:
        rand_c -= 1

    return rand_r, rand_c



def main():
    run = True
    FPS = 60

    lives = 3
    score = 0
    level = 1

    main_font = pygame.font.SysFont("comicsans", 35)
    lost_font = pygame.font.SysFont("comicsans", 60)

    is_jumping = False
    jump_count = 10

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
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (10, 40))
        WINDOW.blit(score_label, (WIDTH - score_label.get_width() - 10, 10))  # get_width() return the width of surfaces

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
            if lost_count > FPS * 3:
                run = False
            else:
                continue


        for i in range(1):

            if score < 50:
                level = 1
            elif score >= 50 and score < 100:
                level = 2
            elif score >= 100 and score < 150:
                level = 3
            elif score >= 150:
                level = (score + 50) // 50

            if level == 1:
                species = rand_species(2000, 2, 0, 0, 8, 0, 0, 0, 8)
                if species[0] == None:
                    pass
                else:
                    rand_r, rand_c = rand_spawn_place(WIDTH)
                    #creature = Creature(species[0], random.randrange(10, WIDTH - 60), random.randrange(-200, -50))
                    creature = Creature(species[0], rand_c, rand_r)
                    creatures.append(creature)

            elif level == 2:
                rand_r, rand_c = rand_spawn_place(WIDTH)
                species = rand_species(2000, 2, 1, 0, 5, 0, 1, 0, 5)
                if species[0] == None:
                    pass
                else:
                    creature = Creature(species[0], rand_c, rand_r)
                    creatures.append(creature)


            elif level == 3:
                rand_r, rand_c = rand_spawn_place(WIDTH)
                species = rand_species(2000, 3, 1, 2, 4, 1, 1, 1, 4)
                if species[0] == None:
                    pass
                else:
                    creature = Creature(species[0], rand_c, rand_r)
                    creatures.append(creature)


            elif level > 3:

                k = level - 2
                rand_r, rand_c = rand_spawn_place(WIDTH)
                species = rand_species(2000, k*2, k*1, k*1, k*3, k*1, k*1, k*1, k*2)
                if species[0] == None:
                    pass
                else:
                    creature = Creature(species[0], rand_c, rand_r)
                    creatures.append(creature)


            """ 
            species = random.choices(list_of_creatures, weights=[2200,3,1,2,2,1,1,1,2], k=1)
            if species[0] == None:
                pass
            else:
                creature = Creature(species[0], random.randrange(10, WIDTH - 60), random.randrange(-200, -50))
                creatures.append(creature)
            """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Moving when not jumping
        if not(is_jumping):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and toad.x > 0:
                toad.x -= toad.speed
            if keys[pygame.K_RIGHT] and toad.x + toad.get_width() < WIDTH:
                toad.x += toad.speed
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                is_jumping = True

        # Moving when jumping
        elif is_jumping:
            if jump_count >= -10:
                k = 1
                if jump_count < 0:
                    k = -1
                toad.y -= jump_count ** 2 * 0.5 * k
                jump_count -= 1

            else:
                is_jumping = False
                jump_count = 10

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and toad.x > 0:
                toad.x -= toad.speed *2
            if keys[pygame.K_RIGHT] and toad.x + toad.get_width() < WIDTH:
                toad.x += toad.speed *2


        # Moving creatures and removing them whem they hit the ground
        for creature in creatures[:]:

            creature.move()

            # Eating creatures
            if creature.collision(toad):

                if (score + creature.sp) >= 0:
                    score += creature.sp

                if (lives + creature.lp) <= 3:
                    toad.lp += creature.lp
                    lives += creature.lp

                creatures.remove(creature)

            # Creatures hitting the ground
            if creature.y + creature.get_height() > HEIGHT - 80:
                if creature.species == "fly" or creature.species == "mosquito" or creature.species == "ladybug" or creature.species == "snail":
                    lives -= 1
                print(creature.species, creature.x)

                creatures.remove(creature)





main()
