import pygame
import sys


class Button:
    def __init__(self,window,text,pos,height,width,colour,border,x,y):
        self.text = text
        self.pos = pos
        self.colour = colour
        self.border = border
        self.x = x
        self.y = y
        self.button = pygame.rect.Rect((self.pos[0],self.pos[1]),(height,width))
        self.window = window
        self.font = pygame.font.SysFont("comicsans", 16)

    def drawing(self):
        switch = pygame.draw.rect(self.window,self.colour, self.button,self.border)
        text = self.font.render(self.text,'True','black')
        self.window.blit(text,(self.pos[0] + self.x, self.pos[1] + self.y))

    def clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
            
        return False
