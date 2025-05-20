import pygame
import sys
import os
from foundation import basicstate
from spriteclasses import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



class levelone(basicstate):  # Game level one 
    def __init__(self):   #constructor function 
        super(levelone, self).__init__()    
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel1 = True
        self.hits = 0    #Attribute to keep track of the number of times the player has been hit

    def checkendoflevel(self,window): #Checks if all the enemies are dead and the player has reached the endpoint
        
        if len(enemy_group) == 0: # checks if the enemy is dead  
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask): #Checks to see if the player has reached the endpoint
                self.startlevel1 = True
                self.done = True
                self.next_state = "regcompletelevelone"
                laser_group.empty()        
                enemy_bullet_group.empty()     #Empties both the laser_group and enemy_bullet_group 




    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel1 = True
            self.done = True
            self.next_state = "regfaillevelone"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()
            
            
            

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
        for row in range(8):   #My data structure(2D array of objects)
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

        if self.startlevel1: 
            player = Player_stats(30,330,window)
            first_enemy = enemy_stats(750,100)
            player_group.add(player)
            enemy_group.add(first_enemy)
            self.startlevel1 = False

        self.updating_window(window)
        self.gamelevel(window)


class leveltwo(basicstate):   # Game level two 
    def __init__(self):
        super(leveltwo, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel2 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel2 = True
                self.done = True
                self.next_state = "completelevel2"
                laser_group.empty()
                enemy_bullet_group.empty()



    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel2 = True
            self.done = True
            self.next_state = "regfaillevel2"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()

                      

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
        for row in range(8):   #My data structure(2D array of objects)
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

        if self.startlevel2:
            player = Player_stats(30,330,window)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            player_group.add(player)
            enemy_group.add(first_enemy,second_enemy)
            self.startlevel2 = False
            

        self.updating_window(window)
        self.gamelevel(window)




class levelthree(basicstate):  # Game level three
    def __init__(self):
        super(levelthree, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel3 = True        
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel3 = True
                self.done = True
                self.next_state = "completelevel3"
                laser_group.empty()
                enemy_bullet_group.empty()




    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel3 = True
            self.done = True
            self.next_state = "regfaillevel3"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()

                      

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
        for row in range(8):   #My data structure(2D array of objects)
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

        if self.startlevel3:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            third_enemy = enemy_stats(650,650)
            enemy_group.add(first_enemy,second_enemy,third_enemy)
            self.startlevel3 = False
            

        self.updating_window(window)
        self.gamelevel(window)


class levelfour(basicstate): # Game level four 
    def __init__(self):
        super(levelfour, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel4 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel4 = True
                self.done = True
                self.next_state = "completelevel4"
                laser_group.empty()
                enemy_bullet_group.empty()



    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel4 = True
            self.done = True
            self.next_state = "regfaillevel4"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()

                      

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
        for row in range(8):  #My data structure(2D array of objects)
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

        if self.startlevel4:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            third_enemy = enemy_stats(650,650)
            fourth_enemy = enemy_stats(550,250)
            fifth_enemy = enemy_stats(920,630)
            enemy_group.add(first_enemy,second_enemy,third_enemy,fourth_enemy,fifth_enemy)
            self.startlevel4 = False
            

        self.updating_window(window)
        self.gamelevel(window)


class levelfive(basicstate): # Game level five 
    def __init__(self):
        super(levelfive, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel5 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel5 = True
                self.done = True
                self.next_state = "completelevel5"
                laser_group.empty()
                enemy_bullet_group.empty()


        if pygame.sprite.groupcollide(staticobject_group,player_group,True,True,pygame.sprite.collide_mask):
                self.startlevel5 = True
                self.done = True
                self.next_state = "regfaillevel5"
                laser_group.empty()
                enemy_group.empty()
                enemy_bullet_group.empty()
            


    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel5 = True
            self.done = True
            self.next_state = "regfaillevel5"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()

                      

    def gamelevel(self,window):

        laser_group.draw(window)
        endpoint_group.draw(window)
        enemy_group.draw(window)
        enemy_bullet_group.draw(window)
        player_group.draw(window)
        staticobject_group.draw(window)
            
        enemy_group.update()
        enemy_bullet_group.update()
        laser_group.update()
        player_group.update()
        staticobject_group.update()
                 
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
        for row in range(8):  #My data structure(2D array of objects)
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

        if self.startlevel5:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            fifth_enemy = enemy_stats(920,630)
            enemy_group.add(first_enemy,second_enemy,fifth_enemy)
            one_still = stationaryobject(240,140)
            second_still = stationaryobject(335,600)
            staticobject_group.add(one_still,second_still)
            self.startlevel5 = False
            

        self.updating_window(window)
        self.gamelevel(window)

class levelsix(basicstate): # Game level six
    def __init__(self):
        super(levelsix, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel6 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel6 = True
                self.done = True
                self.next_state = "completelevel6"
                laser_group.empty()
                enemy_bullet_group.empty()


        if pygame.sprite.groupcollide(staticobject_group,player_group,True,True,pygame.sprite.collide_mask):
                self.startlevel6 = True
                self.done = True
                self.next_state = "regfaillevel6"
                laser_group.empty()
                enemy_group.empty()
                enemy_bullet_group.empty()

                

    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel6 = True
            self.done = True
            self.next_state = "regfaillevel6"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()

                      

    def gamelevel(self,window):

        laser_group.draw(window)
        endpoint_group.draw(window)
        enemy_group.draw(window)
        enemy_bullet_group.draw(window)
        player_group.draw(window)
        staticobject_group.draw(window)
            
        enemy_group.update()
        enemy_bullet_group.update()
        laser_group.update()
        player_group.update()
        staticobject_group.update()
                 
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
        for row in range(8):  #My data structure(2D array of objects)
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

        if self.startlevel6:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            third_enemy = enemy_stats(650,650)
            fifth_enemy = enemy_stats(920,630)
            enemy_group.add(first_enemy,second_enemy,third_enemy,fifth_enemy)
            one_still = stationaryobject(240,140)
            second_still = stationaryobject(335,600)
            third_still = stationaryobject(430,325)
            staticobject_group.add(one_still,second_still,third_still)
            self.startlevel6 = False
            

        self.updating_window(window)
        self.gamelevel(window)

class levelseven(basicstate): # Game level seven 
    def __init__(self):
        super(levelseven, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel7 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel7 = True
                self.done = True
                self.next_state = "completelevel7"
                laser_group.empty()
                enemy_bullet_group.empty()
                moveobject_group.empty()

                

        if pygame.sprite.groupcollide(moveobject_group,player_group,True,True,pygame.sprite.collide_mask):
                self.startlevel7 = True
                self.done = True
                self.next_state = "regfaillevel7"
                laser_group.empty()
                enemy_group.empty()
                enemy_bullet_group.empty()
                moveobject_group.empty()


    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel7 = True
            self.done = True
            self.next_state = "regfaillevel7"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()
            moveobject_group.empty()


                      

    def gamelevel(self,window):

        laser_group.draw(window)
        endpoint_group.draw(window)
        enemy_group.draw(window)
        enemy_bullet_group.draw(window)
        player_group.draw(window)
        moveobject_group.draw(window)
            
        enemy_group.update()
        enemy_bullet_group.update()
        laser_group.update()
        player_group.update()
        moveobject_group.update()
                 
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
        for row in range(8):   #My data structure(2D array of objects)
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
        if self.startlevel7:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            third_enemy = enemy_stats(650,650)
            fifth_enemy = enemy_stats(920,630)
            fourth_enemy = enemy_stats(550,250)
            enemy_group.add(first_enemy,second_enemy,third_enemy,fourth_enemy,fifth_enemy)
            one_move = speedingobject(235,250)
            second_move = speedingobject(430,500)
            moveobject_group.add(one_move,second_move)
            self.startlevel7 = False
            

        self.updating_window(window)
        self.gamelevel(window)

class leveleight(basicstate): # Game level eight
    def __init__(self):
        super(leveleight, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.startlevel8 = True
        self.hits = 0

    def checkendoflevel(self,window):
        if len(enemy_group) == 0:        
            if pygame.sprite.groupcollide(endpoint_group,player_group,False,True,pygame.sprite.collide_mask):
                self.startlevel8 = True
                self.done = True
                self.next_state = "completelastlevel"
                laser_group.empty()
                enemy_bullet_group.empty()
                moveobject_group.empty()


        if pygame.sprite.groupcollide(moveobject_group,player_group,True,True,pygame.sprite.collide_mask):
                self.startlevel8 = True
                self.done = True
                self.next_state = "regfaillevel8"
                laser_group.empty()
                enemy_group.empty()
                enemy_bullet_group.empty()
                moveobject_group.empty()

    def playerfail(self):

        if pygame.sprite.groupcollide(enemy_bullet_group,player_group,True,False,pygame.sprite.collide_mask):
            self.hits += 1

        if self.hits == 4:
            self.startlevel8 = True
            self.done = True
            self.next_state = "regfaillevel8"
            self.hits = 0
            laser_group.empty()
            player_group.empty()
            enemy_bullet_group.empty()
            enemy_group.empty()
            moveobject_group.empty()


    def gamelevel(self,window):

        laser_group.draw(window)
        endpoint_group.draw(window)
        enemy_group.draw(window)
        enemy_bullet_group.draw(window)
        player_group.draw(window)
        moveobject_group.draw(window)
            
        enemy_group.update()
        enemy_bullet_group.update()
        laser_group.update()
        player_group.update()
        moveobject_group.update()
                 
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
        for row in range(8):   #My data structure(2D array of objects)
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

        if self.startlevel8:
            player = Player_stats(30,330,window)
            player_group.add(player)
            first_enemy = enemy_stats(750,100)
            second_enemy = enemy_stats(850,300)
            third_enemy = enemy_stats(650,650)
            fourth_enemy = enemy_stats(550,250)
            fifth_enemy = enemy_stats(920,630)
            sixth_enemy = enemy_stats(350,450)
            enemy_group.add(first_enemy, second_enemy,third_enemy,fourth_enemy,fifth_enemy,sixth_enemy)
            one_move = speedingobject(235,250)
            second_move = speedingobject(430,500)
            third_move = speedingobject(525,400)
            moveobject_group.add(one_move,second_move,third_move)
            self.startlevel8 = False
            

        self.updating_window(window)
        self.gamelevel(window)

