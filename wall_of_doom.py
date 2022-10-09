import pygame
import random
from pygame.locals import *
pygame.init()

pygame.font.init()


running = True
screen = pygame.display.set_mode((1000, 1000))

player_x = 100
player_y = 500
derection = 2
smallfont = pygame.font.Font(None, 40)
wall_of_doom = pygame.image.load("wall.png")
wall_of_doom = pygame.transform.scale(wall_of_doom,(100,1000))
fire = pygame.image.load("fire.png")
wall_of_doom = pygame.transform.flip(wall_of_doom, True, False)
backround = pygame.image.load("nether.png")
backround = pygame.transform.scale(backround,(1000,1000))
player = pygame.image.load("player_2.png")
bullet = pygame.image.load("bullet.png")
fighter = pygame.image.load("enemy.png")
player = pygame.transform.scale(player,(100,100))
flag = False
fire_on_screen = []
bullet_on_screen = []
player_hitbox = (player_x, player_y, 90, 90)
player_rect = pygame.Rect(player_hitbox)
clock = pygame.time.Clock()
can_fire = True
you_die = False
class enemy:
    def __init__(self, x, y, pic, can_kill):
        self.x = x
        self.y = y
        self.pic = pic
        self.speed = random.randint(3, 7)
        self.pic = pygame.transform.scale(self.pic,(100,100))
        self.hitbox = (self.x, self.y, 95, 100)
        self.hitbox_rect = pygame.Rect(self.hitbox)
        self.can_kill = can_kill
    def display(self):
        self.hitbox = (self.x, self.y, 95, 100)
        self.hitbox_rect = pygame.Rect(self.hitbox)
        screen.blit(self.pic, (self.x, self.y))
        #pygame.draw.rect(screen, (0, 0, 0), self.hitbox_rect, 2)
    def move(self):
        self.x-=self.speed
    def get_hitbox_rect(self):
        return self.hitbox_rect
    def get_can_kill(self):
        return self.can_kill
class bulit:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.pic = pic
        self.pic = pygame.transform.scale(self.pic, (30, 30))
        self.hitbox = (self.x, self.y, 40, 40)
        self.hitbox_rect = pygame.Rect(self.hitbox)
    def get_hitbox(self):
        return self.hitbox_rect
    def display(self):
        self.hitbox = (self.x, self.y, 40, 40)
        self.hitbox_rect = pygame.Rect(self.hitbox)
        screen.blit(self.pic, (self.x, self.y))
        #pygame.draw.rect(screen, (0, 0, 0), self.hitbox_rect, 2)
    def move_bullet(self):
        self.x+=8
test_bulit = bulit(500, 500, bullet)
bullet_on_screen.append(test_bulit)
def collide():
    for i in bullet_on_screen:
        for x in fire_on_screen:
            if x.get_hitbox_rect().colliderect(i.get_hitbox())  and x.get_can_kill() == True:

                fire_on_screen.remove(x)
                bullet_on_screen.remove(i)
            if player_rect.colliderect(x.get_hitbox_rect()):
                return False
def you_died():
    death = smallfont.render("you died", False, "black")
    death_2 = smallfont.render("press space to restart", False, "black")
    screen.blit(death, [500, 500])
    screen.blit(death_2, [500, 400])
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    
    screen.blit(backround, (0, 0))
    screen.blit(wall_of_doom, (0, 0))
    screen.blit(player, (player_x, player_y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and flag == False and you_die == False:
        derection+=1
        starttime = pygame.time.get_ticks()
        flag = True
    if keys[pygame.K_s] and flag == False and you_die == False:
        derection-=1
        starttime = pygame.time.get_ticks()
        flag = True
    if keys[pygame.K_SPACE] and can_fire == True and you_die == False:
        bullet_on_screen.append(bulit(player_x, player_y, bullet))
        can_fire = False
        time_since_bullet = pygame.time.get_ticks()
    if derection >=3:
        derection = 3


    if derection == 1:
        player_y = 700

    elif derection == 2 :
        player_y = 500



    elif derection == 3 :

        player_y = 300
    if flag == True and pygame.time.get_ticks() - starttime >= 200  and you_die == False:
        flag = False
    if can_fire == False and pygame.time.get_ticks() - time_since_bullet >=250  and you_die == False:
        can_fire = True
    if_enemy_spwan = random.randint(1, 80)
    if if_enemy_spwan == 1  and you_die == False:
        the_y = random.randint(1, 3)
        the_true_y = None
        if the_y == 1:
            the_true_y = 700
        if the_y == 2:
            the_true_y = 500
        if the_y == 3:
            the_true_y = 300
        can_be_killed = random.randint(1, 3)
        if can_be_killed == 1 or 3:
            fire_on_screen.append(enemy(900, the_true_y, fire, False))
        if can_be_killed == 2:
            fire_on_screen.append(enemy(900, the_true_y, fighter, True))
    player_hitbox = (player_x, player_y, 90, 90)
    player_rect = pygame.Rect(player_hitbox)
    #pygame.draw.rect(screen, (0, 0, 0), player_rect, 2)

    
    for i in fire_on_screen:
        i.display()
        i.move()



    for i in bullet_on_screen:
        i.display()
        i.move_bullet()

    if collide() == False:
        you_die = True
    if you_die == True:
        keys = pygame.key.get_pressed()
        you_died()
        if keys[pygame.K_SPACE]:
            you_die = False
            bullet_on_screen = []
            fire_on_screen = []
    pygame.display.update()
pygame.quit()