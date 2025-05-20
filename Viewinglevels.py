import pygame
import sys
import os
import mysql.connector
from buttonclass import Button
from foundation import basicstate


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class viewlevels_page(basicstate):
    def __init__(self):
        super(viewlevels_page, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 16)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.bigfont = pygame.font.SysFont("comicsans", 30)
        self.signout = None
        self.levelone = None
        self.leveltwo = None
        self.levelthree = None
        self.levelfour = None
        self.levelfive = None
        self.levelsix = None
        self.levelseven = None
        self.leveleight = None

    def handle_inputs(self):

            if self.signout.clicked():
                self.done = True
                self.next_state = "menu"

            if self.levelone.clicked():
                self.done = True
                self.next_state = "gamelevelone"


            if self.leveltwo.clicked():
                self.done = True
                self.next_state = "gameleveltwo"
               

            if self.levelthree.clicked():
               self.done = True
               self.next_state = "gamelevelthree"

            if self.levelfour.clicked():
                self.done = True
                self.next_state = "gamelevelfour"

            if self.levelfive.clicked():
                self.done = True
                self.next_state = "gamelevelfive"

            if self.levelsix.clicked():
                self.done = True
                self.next_state = "gamelevelsix"

            if self.levelseven.clicked():
                self.done = True
                self.next_state = "gamelevelseven"

            if self.leveleight.clicked():
                self.done = True
                self.next_state = "gameleveleight"
        

        


    def get_event(self, event):

        if event.type == pygame.QUIT:
                self.quit = True

        self.handle_inputs()


    def draw(self, window):

        outline = pygame.draw.rect(window, WHITE,[50,50,700,600],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        alllevels = self.bigfont.render("All levels", True, 'black')
        window.blit(gamename, (70,60))
        window.blit(self.logo, (520,50))
        window.blit(alllevels, (320,60))


        self.levelone = Button(window,'',(80,200),130,100,'black',2,10,10)
        levelonetext = self.font.render('Level one', True, 'black')
        window.blit(levelonetext,(110,310))
        self.levelone.drawing()

        self.leveltwo = Button(window,'',(240,200),130,100,'black',2,10,10)
        leveltwotext = self.font.render('Level two', True, 'black')
        window.blit(leveltwotext,(270,310))
        self.leveltwo.drawing()

        
        self.levelthree = Button(window,'',(410,200),130,100,'black',2,10,10)
        levelthreetext = self.font.render('Level three', True, 'black')
        window.blit(levelthreetext,(440,310))
        self.levelthree.drawing()

        self.levelfour = Button(window,'',(570,200),130,100,'black',2,10,10)
        levelfourtext = self.font.render('Level four', True, 'black')
        window.blit(levelfourtext,(600,310))
        self.levelfour.drawing()
    

        self.levelfive = Button(window,'',(80,400),130,100,'black',2,10,10)
        levelfivetext = self.font.render('Level five', True, 'black')
        window.blit(levelfivetext,(110,510))
        self.levelfive.drawing()


        self.levelsix = Button(window,'',(240,400),130,100,'black',2,10,10)
        levelsixtext = self.font.render('Level six', True, 'black')
        window.blit(levelsixtext,(270,510))
        self.levelsix.drawing()
    

        self.levelseven = Button(window,'',(410,400),130,100,'black',2,10,10)
        levelseventext = self.font.render('Level seven', True, 'black')
        window.blit(levelseventext,(440,510))
        self.levelseven.drawing()
      

        self.leveleight = Button(window,'',(570,400),130,100,'black',2,10,10)
        leveleighttext = self.font.render('Level eight', True, 'black')
        window.blit(leveleighttext,(600,510))
        self.leveleight.drawing()



        self.signout = Button(window,'Sign out',(80,570),80,50,'black',2,10,10)
        signouttext = self.font.render('Sign out', True, 'black')
        window.blit(signouttext,(90,580))
        self.signout.drawing()
 


