import pygame
import sys
from foundation import basicstate
from buttonclass import Button
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class registeredlosinglevelone(basicstate):
    def __init__(self):
        super(registeredlosinglevelone, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.playerscore = "Score:0"
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.Leaderboard = None
        self.Retry = None
        self.alllevels = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelone"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        failed = self.bigfont.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270)) 
        window.blit(gamename, (160,120))
        window.blit(self.logo, (370,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(400,430),220,40,'white',0,50,10)
        self.alllevels.drawing()
 

        self.Leaderboard = Button(window,'Leaderboard',(240,430),150,40,'white',0,20,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(150,430),80,40,'white',0,15,10)
        self.Retry.drawing()
  



