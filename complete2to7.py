import pygame
import sys
from Playeraccounts import sign_in_players
from foundation import basicstate
from buttonclass import Button
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class completing2(basicstate):
    def __init__(self):
        super(completing2, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gamelevelthree"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore2(2000)

        playerscore.addtohighscore()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 2000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()


class completing3(basicstate):
    def __init__(self):
        super(completing3, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gamelevelfour"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore3(3000)

        playerscore.addtohighscore()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 3000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()



class completing4(basicstate):
    def __init__(self):
        super(completing4, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gamelevelfive"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore4(4000)

        playerscore.addtohighscore()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 4000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()


class completing5(basicstate):
    def __init__(self):
        super(completing5, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gamelevelsix"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore5(5000)

        playerscore.addtohighscore()

    def draw(self,window):

        
        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 5000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()

class completing6(basicstate):
    def __init__(self):
        super(completing6, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gamelevelseven"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore6(6000)

        playerscore.addtohighscore()

    def draw(self,window):


        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 6000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()

class completing7(basicstate):
    def __init__(self):
        super(completing7, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
        self.nextlevel = None
        self.alllevels = None
        self.Leaderboard = None
        self.Retry = None

    def handle_input(self):
        
        if self.nextlevel.clicked():
            self.done = True
            self.next_state = "gameleveleight"
        elif self.alllevels.clicked():
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

    def insertscoreintotable(self):
        with open("detailfile.txt","r") as readfile:
            line = readfile.readline()
            items = line.split(",")
            email = items[0]
            password = items[1]

        playerscore = sign_in_players(email,password)
        playerscore.createdbconn()
        playerscore.getkey()
        playerscore.insertscore7(7000)

        playerscore.addtohighscore()

    def draw(self,window):

        outline = pygame.draw.rect(window, WHITE,[150,120,550,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.bigfont.render("Congratulations", True, 'black')
        score = self.bigfont.render("Score: 7000", True, 'black')
        window.blit(congrats, (300,270))
        window.blit(gamename, (160,120))
        window.blit(self.logo, (480,120))
        window.blit(score,(350,350))

        self.nextlevel = Button(window,'Next level',(610,430),90,40,'white',0,10,10)
        self.nextlevel.drawing()
 

        self.alllevels = Button(window,'View all levels',(460,430),140,40,'white',0,15,10)
        self.alllevels.drawing()


        self.Leaderboard = Button(window,'Leaderboard',(340,430),110,40,'white',0,10,10)
        self.Leaderboard.drawing()


        self.Retry = Button(window,'Retry',(270,430),60,40,'white',0,10,10)
        self.Retry.drawing()


        self.Previouslevel = Button(window,'Previous level',(150,430),110,40,'white',0,10,10)
        self.Previouslevel.drawing()

        self.insertscoreintotable()







