import pygame
import sys
from foundation import basicstate
from buttonclass import Button
from Playeraccounts import register_player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Registerplayer(basicstate):
    def __init__(self):
        super(Registerplayer,self).__init__()
        self.email_text = ""
        self.password_text = ""
        self.username_text = ""
        self.currentfield = 0
        self.email = None
        self.password = None
        self.username = None
        self.font = pygame.font.SysFont("comicsans",12)
        self.bigfont = pygame.font.SysFont("comicsans",30)
        

    def handle_input(self):

        if self.email.clicked():
            self.currentfield = 0
        elif self.password.clicked():
            self.currentfield = 1
        elif self.username.clicked():
            self.currentfield = 2

        if len(self.email_text) > 0 and len(self.password_text) > 0 and len(self.username_text) > 0:
            if self.reg.clicked(): 
                registeruser = register_player(self.email_text,self.password_text,self.username_text)
                registeruser.createdbconn()
                check_player_details = registeruser.checkdetails()
                if check_player_details == False:
                    pass
                elif check_player_details == True:
                    dfile = open("detailfile.txt", "w")
                    dfile.write(self.email_text+","+self.password_text)
                    dfile.close()
                    foreginkey = registeruser.insertdetails()
                    self.email_text = ""
                    self.password_text = ""
                    self.username_text = ""
                    self.done = True
                    self.next_state = "viewlevels"

            
        


    def get_event(self, event):

            if event.type == pygame.QUIT:
                self.quit = True
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.currentfield == 0:
                        self.email_text = self.email_text[:-1]
                    elif self.currentfield == 1:
                        self.password_text = self.password_text[:-1]
                    else: 
                        self.username_text = self.username_text[:-1]
                    
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
                    else:
                        if event.unicode.isprintable():
                            if len(self.username_text) < 15:
                                if event.unicode == 15:
                                    self.username_text += 0
                                else:            
                                    self.username_text += event.unicode

            self.handle_input()


    def draw(self,window):
        box = pygame.draw.rect(window, WHITE,[250,100,300,450],0,1)
        text = self.bigfont.render('Register','True','black')
        window.blit(text, (340,120))

        self.email = Button(window,'E-mail:',(300,180),200,50,'black',2,0,-20)
        self.email.drawing()
        
        self.password = Button(window,'Password:',(300,270),200,50,'black',2,0,-20)
        self.password.drawing()
        
        self.username = Button(window,'Username:',(300,360),200,50,'black',2,0,-20)
        self.username.drawing()
        
        self.reg = Button(window,'Register',(340,450),120,50,'black',2,15,10)
        self.reg.drawing()

        email_surface = self.font.render(self.email_text, True, BLACK)
        window.blit(email_surface, (310,190))
        

        password_surface = self.font.render(self.password_text, True, BLACK)
        window.blit(password_surface, (310,280))
        

        username_surface = self.font.render(self.username_text, True, BLACK)
        window.blit(username_surface, (310,370))



      

        






   
