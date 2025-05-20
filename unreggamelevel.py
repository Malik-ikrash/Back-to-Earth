import pygame
import sys
import os
from foundation import basicstate
from spriteclasses import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class unreglevel(basicstate):
    def __init__(self):
        super(unreglevel, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel = True
        self.hits = 0

        



    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.done = True
                self.next_state = "unregfinishlevelone"
                laser_group.empty()
                enemy_bullet_group.empty()
                player = Player_stats(30,330,window)
                player_group.add(player)
                first_enemy = enemy_stats(750,100)
                enemy_group.add(first_enemy)



    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.done = True
            self.next_state = "unregfaillevelone"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()
            player = Player_stats(30,330,window)
            first_enemy = enemy_stats(750,100)
            player_group.add(player)
            enemy_group.add(first_enemy)
            
            
            

    def gamelevel(self,window):

        laser_group.draw(window)
        endpoint_group.draw(window)
        enemy_group.draw(window)
        enemy_bullet_group.draw(window)
        player_group.draw(window)
            
        enemy_group.update()
        enemy_bullet_group.update()
        laser_group.update()
        player_group.update()
     

            
        self.checkendoflevel(window)
        self.playerfail()
        



    
    

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True


    def updating_window(self,window):    
        WIDTH = 90
        HEIGHT = 87
        MARGIN = 5
        grid = []
        
        window.fill(BLACK)
        for row in range(8):   #My standard algorithm(2D array of objects)
            grid.append([])
            for column in range(11):
                grid[row].append(0)
       

 
        for row in range(8):
            for column in range(11):
                color = WHITE
                pygame.draw.rect(window,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
 

    def draw(self,window):

        if self.startlevel: 
            player = Player_stats(30,330,window)
            first_enemy = enemy_stats(750,100)
            player_group.add(player)
            enemy_group.add(first_enemy)
            self.startlevel = False
            
        
        self.updating_window(window)
        self.gamelevel(window)















    
