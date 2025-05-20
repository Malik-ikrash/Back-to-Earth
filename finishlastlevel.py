import pygame
import sys
from foundation import basicstate
from buttonclass import Button
from Playeraccounts import sign_in_players
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class completinglastlevel(basicstate):
    def __init__(self):
        super(completinglastlevel, self).__init__()
        self.font = pygame.font.SysFont("comicsans", 12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        self.logo = pygame.image.load(os.path.join("logo.png"))
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
            self.next_state = "gameleveleight"
        elif self.Previouslevel.clicked():
            self.done = True
            self.next_state = "gamelevelseven"

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
        playerscore.insertscore8(8000)
        
        playerscore.addtohighscore()

    def draw(self,window):


        outline = pygame.draw.rect(window, WHITE,[150,120,470,300],0)
        gamename = self.bigfont.render('Back to Earth','True','black')
        congrats = self.font.render("Congratulations you completed the game", True, 'black')
        score = self.bigfont.render("Score: 8000", True, 'black')
        window.blit(congrats, (210,270))
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

        self.insertscoreintotable()






