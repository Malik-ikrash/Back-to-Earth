import pygame
import os
window = pygame.display.set_mode((1050,750))

laser_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
endpoint_group = pygame.sprite.Group()
staticobject_group = pygame.sprite.Group()
moveobject_group = pygame.sprite.Group()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)




class Player_stats(pygame.sprite.Sprite):
    def __init__(self,x,y,window,health = 100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.window = window
        self.object_laser = pygame.image.load(os.path.join("player_laser.png"))
        self.laser_breaks = pygame.time.get_ticks()
        self.health = health
        self.full_health = health


    def update(self):

        playervel = 5
        cooldown = 500
        time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x - playervel > -50:
            self.rect.x -= playervel
        if key[pygame.K_RIGHT] and (self.rect.x + playervel + self.getobjectwidth() < 1050):
            self.rect.x += playervel
        if key[pygame.K_UP] and self.rect.y + playervel > 30:
            self.rect.y -= playervel   
        if key[pygame.K_DOWN] and (self.rect.y + playervel + self.getobjectheight() + 15 < 750):
            self.rect.y += playervel
        if key[pygame.K_SPACE] and time - self.laser_breaks > cooldown:
            laser = Bullets(self.rect.x+160, self.rect.y+25, self.object_laser)
            laser_group.add(laser)
            self.laser_breaks = time

        self.mask = pygame.mask.from_surface(self.image)

        self.health_bar(self.window) 


    def getobjectwidth(self):
        return self.image.get_width()

    def getobjectheight(self):
        return self.image.get_height()
 

    def health_bar(self,window):
        if pygame.sprite.spritecollide(self,enemy_bullet_group,False,pygame.sprite.collide_mask):
            self.full_health -= 25

        pygame.draw.rect(window, RED, (self.rect.x,(self.rect.bottom + 10),self.rect.width,15))
        if self.full_health > 0:
             pygame.draw.rect(window, GREEN, (self.rect.x,(self.rect.bottom + 10),self.rect.width * (self.full_health/self.health),15))
    

        
          

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


    def update(self):
        self.rect.x += 5
        if self.rect.x > 1100:
            self.kill()

        if pygame.sprite.spritecollide(self,enemy_group,True,pygame.sprite.collide_mask):
            self.kill()

            

class enemy_stats(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.object_laser = pygame.image.load(os.path.join("enemy_laser.png"))
        self.direction = 1
        self.speed = 10
        self.enemy_breaks = pygame.time.get_ticks()


    def update(self):
        time = pygame.time.get_ticks()
        cooldown = 180
        self.rect.y += self.speed
        if self.rect.y + 100 > 750 or self.rect.y < 0:
            self.direction *= -1
        self.speed *= self.direction

        if time - self.enemy_breaks > cooldown:   
           shots = enemy_bullets(self.rect.x, self.rect.y + 20 ,pygame.image.load(os.path.join("enemy_laser.png")))
           enemy_bullet_group.add(shots)
           self.enemy_breaks = time

        self.mask = pygame.mask.from_surface(self.image)


class enemy_bullets(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


    def update(self):
        self.rect.x -= 5
        if self.rect.x < 10:
            self.kill()



 

        



class endpoint(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Endpoint.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]



class stationaryobject(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("stillobject.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


class speedingobject(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("object.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.speed = 10
        self.direction = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.y + 100 > 750 or self.rect.y < 0:
            self.direction *= -1
        self.speed *= self.direction
        

            



end = endpoint(1000,410) # An instance of the endpoint class
endpoint_group.add(end)


