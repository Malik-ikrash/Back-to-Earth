import pygame
import sys
import os
from foundation import basicstate
from buttonclass import Button 



BLACK = (0, 0, 0)  
WHITE = (255, 255, 255) 

pygame.init()

class Menu(basicstate):
    def __init__(self):
        super(Menu, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.register = None
        self.signin = None
        self.quitgame = None
        self.guest = None


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif self.register.clicked():
            self.done = True 
            self.next_state = "register"
        elif self.signin.clicked():
            self.done = True
            self.next_state = "signin"
        elif self.guest.clicked():
            self.done = True
            self.next_state = "unreggamelevel"
        elif self.quitgame.clicked():
            self.quit = True



        

    def draw(self, window):
        window = window
        window.fill(pygame.Color("black"))
        outline = pygame.draw.rect(window, WHITE,[200,120,400,300],0)
        gamename = self.font.render('Back to Earth','True','black')
        window.blit(gamename, (300,180))
        window.blit(self.logo, (300,270))

        self.register = Button(window,'Register',(200,430),90,40,'white',0,15,10)
        self.register.drawing()
        self.signin = Button(window,'Sign in',(300,430),80,40,'white',0,15,10)
        self.signin.drawing()
        self.guest = Button(window,'Play as a guest',(390,430),120,40,'white',0,10,10)
        self.guest.drawing()
        self.quitgame = Button(window,'Quit',(520,430),80,40,'white',0,15,10)
        self.quitgame.drawing()





        
        
        





