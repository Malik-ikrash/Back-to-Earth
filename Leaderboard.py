import pygame
import sys
from buttonclass import Button
from foundation import basicstate
from Playeraccounts import making_leaderboard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

class leaderboard(basicstate):
    def __init__(self):
        super(leaderboard, self).__init__()
        self.bigfont = pygame.font.SysFont("comicsans", 30)
        self.font = pygame.font.SysFont("comicsans", 16)
        self.viewalllevels = None
        self.counter = 0
        self.x = 270
        self.y = 100
        self.printed = False



    def handle_inputs(self):

        if self.viewalllevels.clicked():
                self.counter = 0
                self.printed = False
                self.y = 100
                self.done = True
                self.next_state = "viewlevels"




    def get_event(self,event):
        if event.type == pygame.QUIT:
            self.quit = True

        self.handle_inputs()



    def draw(self,window):
        
        if self.printed is False:
            outline = pygame.draw.rect(window, WHITE,[250,50,300,600],0)
            leaderboard = self.bigfont.render('Leaderboard','True','black')
            window.blit(leaderboard, (320,50))
            name = [""] * 10 
            score = [""] * 10 
            self.board = making_leaderboard()
            self.board.createdbconn()
            self.board.sort_scores()
            with open("highscore.txt","r") as readfile:
                line = readfile.readline().rstrip("\n")
                while line:
                    items = line.split(",")
                    name[self.counter] = items[0]
                    score[self.counter] = items[1]
                    line = readfile.readline().rstrip("\n")
                    text = self.font.render(f"{self.counter+1}.{name[self.counter]} -  {score[self.counter]} Totalscore", True, BLACK)
                    window.blit(text,(self.x , self.y))
                    self.y += 50
                    self.counter += 1

            self.printed = True


        self.viewalllevels = Button(window,'View all levels',(340,600),130,40,'black',1,10,10)
        self.viewalllevels.drawing()



