import pygame
import sys

pygame.init()

class basicstate(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None 
        self.window_rect = pygame.display.get_surface().get_rect()
                           

    def get_event(self,event):
        pass

    def update(self, time):
        pass

    def draw(self,surface):
        pass


  
        
