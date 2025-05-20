import pygame
import sys
from foundation import basicstate
from buttonclass import Button
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class unregisteredlosinglevelone(basicstate):
    def __init__(self):
        super(unregisteredlosinglevelone, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.playerscore = "Score:0"
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.Register = None
        self.Retry = None

    def handle_input(self):

        if self.Register.clicked():
            self.done = True
            self.next_state = "register"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "unreggamelevel"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[200,120,400,250],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        failed = self.bigfont.render("Level failed", True, 'black')
        score = self.bigfont.render(self.playerscore, True, 'black')
        window.blit(failed, (300,240))
        window.blit(gamename, (200,120))
        window.blit(self.logo, (399,120))
        window.blit(score,(350,290))

        self.Register = Button(window,'Register to unlock more levels later on',(290,380),310,40,'white',0,10,10)
        self.Register.drawing()
   

        self.Retry = Button(window,'Retry',(200,380),80,40,'white',0,15,10)
        self.Retry.drawing()
  




