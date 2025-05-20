import pygame
import sys
from Game import State
from Gamemenu import Menu
from Registerpage import Registerplayer
from Signinpage import Signinplayer
from Viewinglevels import viewlevels_page
from Leaderboard import leaderboard
from gamelevels import *
from unreggamelevel import unreglevel
from complete2to7 import *
from unregisteredcompletelevel import unregisteredcompletelevelone
from registeredfailexceptlevelone import *
from registeredlosinglevelone import registeredlosinglevelone
from unregisteredfaillevel import unregisteredlosinglevelone
from finishlastlevel import completinglastlevel
from registeredfinishlevelone import  registeredcompletinglevelone



pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1050,750))
state_dict = {
    "menu": Menu(),
    "register": Registerplayer(),
    "signin": Signinplayer(),
    "viewlevels": viewlevels_page(),
    "leaderboard":leaderboard(),
    "gamelevelone": levelone(),
    "gameleveltwo": leveltwo(),
    "gamelevelthree": levelthree(),
    "gamelevelfour": levelfour(),
    "gamelevelfive": levelfive(),
    "gamelevelsix": levelsix(),
    "gamelevelseven": levelseven(),
    "gameleveleight": leveleight(),
    "unreggamelevel": unreglevel(),
    "completelevel2": completing2(),
    "completelevel3": completing3(),
    "completelevel4": completing4(),
    "completelevel5": completing5(),
    "completelevel6": completing6(),
    "completelevel7": completing7(),
    "unregfinishlevelone": unregisteredcompletelevelone(),
    "regfaillevel2": registeredlosinglevel2(),
    "regfaillevel3": registeredlosinglevel3(),
    "regfaillevel4": registeredlosinglevel4(),
    "regfaillevel5": registeredlosinglevel5(),
    "regfaillevel6": registeredlosinglevel6(),
    "regfaillevel7": registeredlosinglevel7(),
    "regfaillevel8": registeredlosinglevel8(),
    "regfaillevelone": registeredlosinglevelone(),
    "unregfaillevelone": unregisteredlosinglevelone(),
    "completelastlevel": completinglastlevel(),
    "regcompletelevelone": registeredcompletinglevelone()

}



backtoearth = State(window, state_dict, "menu")
backtoearth.run()

pygame.quit()
sys.exit()
 
