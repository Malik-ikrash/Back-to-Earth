import pygame
import sys
import os
from foundation import basicstate
from buttonclass import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

 

class registeredlosinglevel2(basicstate):
    def __init__(self):
        super(registeredlosinglevel2, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.Leaderboard = None 
        self.alllevels = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gameleveltwo"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelone"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel3(basicstate):
    def __init__(self):
        super(registeredlosinglevel3, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelthree"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gameleveltwo"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()



class registeredlosinglevel4(basicstate):
    def __init__(self):
        super(registeredlosinglevel4, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelfour"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelthree"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel5(basicstate):
    def __init__(self):
        super(registeredlosinglevel5, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelfive"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelfour"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel6(basicstate):
    def __init__(self):
        super(registeredlosinglevel6, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelsix"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelfive"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel6(basicstate):
    def __init__(self):
        super(registeredlosinglevel6, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Retry = None
        self.Previouslevel = None
        self.Leaderboard = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelsix"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelfive"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel7(basicstate):
    def __init__(self):
        super(registeredlosinglevel7, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None
        self.Previouslevel = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gamelevelseven"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelsix"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()


class registeredlosinglevel8(basicstate):
    def __init__(self):
        super(registeredlosinglevel8, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.playerscore = "Score:0"
        self.alllevels = None
        self.Retry = None
        self.Previouslevel = None
        self.Leaderboard = None

    def handle_input(self):

        if self.alllevels.clicked():
            self.done = True
            self.next_state = "viewlevels"
        elif self.Leaderboard.clicked():
            self.done = True
            self.next_state = "leaderboard"
        elif self.Retry.clicked():
            self.done = True
            self.next_state = "gameleveleight"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelseven"

    def get_event(self,event):

        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_input()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        gamename = self.font.render('Back to Earth','True','black')
        failed = self.font.render("Level failed", True, 'black')
        score = self.font.render(self.playerscore, True, 'black')
        window.blit(failed, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (400,120))
        window.blit(score,(330,340))

        self.alllevels = Button(window,'View all levels',(480,430),140,40,'white',0,15,10)
        self.alllevels.drawing()
  

        self.Leaderboard = Button(window,'Leaderboard',(360,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()
 

        self.Retry = Button(window,'Retry',(290,430),60,40,'white',0,10,10)
        self.Retry.drawing()
  

        self.Previouslevel = Button(window,'Previous level',(150,430),130,40,'white',0,10,10)
        self.Previouslevel.drawing()
