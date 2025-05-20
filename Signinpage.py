import pygame
import sys
from buttonclass import Button
from foundation import basicstate
from Playeraccounts import sign_in_players

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Signinplayer(basicstate):
    def __init__(self):
        super(Signinplayer,self).__init__()
        self.email_text = ""
        self.password_text = ""
        self.currentfield = 0
        self.email = None
        self.password = None
        self.font = pygame.font.SysFont("comicsans",12)
        self.bigfont = pygame.font.SysFont("comicsans",30)


    def handle_input(self):
        

            if self.email.clicked():
                self.currentfield = 0
            elif self.password.clicked():
                self.currentfield = 1


            if len(self.email_text) > 0 and len(self.password_text) > 0:
                if self.sign_in.clicked():
                    sign_in_user = sign_in_players(self.email_text,self.password_text)
                    sign_in_user.createdbconn()
                    signed_in_player = sign_in_user.checkdetails()
                    if signed_in_player:
                        dfile = open("detailfile.txt", "w")
                        dfile.write(self.email_text + "," +self.password_text)
                        dfile.close()
                        self.done = True
                        self.email_text = ""
                        self.password_text = ""
                        self.next_state = "viewlevels"
                    else:
                        print("failed")



    def get_event(self,event):

            if event.type == pygame.QUIT:
                self.quit = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.currentfield == 0:
                        self.email_text = self.email_text[:-1]
                    elif self.currentfield == 1:
                        self.password_text = self.password_text[:-1]   
                else:
                    if self.currentfield == 0:
                        if event.unicode.isprintable():
                            if len(self.email_text) < 20:
                                if event.unicode == 20:
                                    self.email_text += 0
                                else:
                                    self.email_text += event.unicode
                    elif self.currentfield == 1:
                        if event.unicode.isprintable():
                            if len(self.password_text) < 20:
                                if event.unicode == 20:
                                    self.password_text += 0
                                else:
                                    self.password_text += event.unicode

            self.handle_input() 


    def draw(self,window):
        box = pygame.draw.rect(window, WHITE,[250,100,300,370],0,1)
        text = self.bigfont.render('Sign in','True','black')
        window.blit(text, (340,120))

        self.email = Button(window,'E-mail:',(300,200),200,50,'black',2,0,-20)
        self.email.drawing()
        
        self.password = Button(window,'Password:',(300,280),200,50,'black',2,0,-20)
        self.password.drawing()
        
        self.sign_in = Button(window,'Sign in',(340,370),120,50,'black',2,15,10)
        self.sign_in.drawing()


        email_surface = self.font.render(self.email_text, True, BLACK)
        window.blit(email_surface, (310,210))

        password_surface = self.font.render(self.password_text, True, BLACK)
        window.blit(password_surface, (310,290))







