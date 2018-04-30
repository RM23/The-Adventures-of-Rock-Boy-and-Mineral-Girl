#file to hold class for rocks that need to be identified
import pygame as game
class Rock():
    def __init__(self,ID,screen):
        if (ID == 1):
            self.name = 'citrine'
            self.hardness = 7
            self.streak = 'white'
            self.opacity = 'translucent'
            self.cleavage = 'no'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this variety of quartz is yellow due to iron impurities."

            self.imageFile = 'Quartz.png'
            
        elif (ID == 2):
            self.name = 'copper'
            self.hardness = 3
            self.streak = 'red'
            self.opacity = 'opaque'
            self.cleavage = 'no'
            self.fracture = 'hackly'
            self.tenacity = 'ductile'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this native element made Butte Montana the richest hill on Earth!"

            self.imageFile = 'Copper.png'
            
        elif (ID == 3):
            self.name = 'ulexite'
            self.hardness = 2.5
            self.streak = 'white'
            self.opacity = 'translucent'
            self.cleavage = 'prismatic'
            self.fracture = 'uneven'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this mineral is used in fiber optic cables."

            self.imageFile = 'Borate.png'
            
        elif (ID == 4):
            self.name = 'calcite'
            self.hardness = 3
            self.streak = 'white'
            self.opacity = 'translucent'
            self.cleavage = 'rhombohedral'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 1

            self.knowledge = "this mineral is what creates karst topographies."

            self.imageFile = 'Carbonate.png'
            
        elif (ID == 5):
            self.name = 'dolomite'
            self.hardness = 4
            self.streak = 'white'
            self.opacity = 'opaque'
            self.cleavage = 'rhombohedral'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 2

            self.knowledge = "this mineral is added to soils to buffer the effects of acid rain."

            self.imageFile = 'Carbonate.png'
            
        elif (ID == 6):
            self.name = 'halite'
            self.hardness = 2.5
            self.streak = 'white'
            self.opacity = 'translucent'
            self.cleavage = 'cubic'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "huh! This one tastes like salt!"

            self.imageFile = 'Halide.png'
            
        elif (ID == 7):
            self.name = 'goethite'
            self.hardness = 5
            self.streak = 'yellow'
            self.opacity = 'opaque'
            self.cleavage = 'no'
            self.fracture = 'splintery'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this mineral was named after a famous German polymath."

            self.imageFile = 'IronOxide.png'
            
        elif (ID == 8):
            self.name = 'magnetite'
            self.hardness = 6
            self.streak = 'black'
            self.opacity = 'opaque'
            self.cleavage = 'no'
            self.fracture = 'uneven'
            self.tenacity = 'brittle'
            self.magnetic = 1
            self.acid = 0

            self.knowledge = "this iron-rich mineral makes up most direct-shipping ores."

            self.imageFile = 'IronOxide.png'
            
        elif (ID == 9):
            self.name = 'kaolinite'
            self.hardness = 2
            self.streak = 'white'
            self.opacity = 'opaque'
            self.cleavage = 'basal'
            self.fracture = 'earthy'
            self.tenacity = 'sectile'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this is a clay mineral with a Chinese name."

            self.imageFile = 'Phyllosilicate.png'

        elif (ID == 10):
            self.name = 'talc'
            self.hardness = 1
            self.streak = 'white'
            self.opacity = 'opaque'
            self.cleavage = 'basal'
            self.fracture = 'uneven'
            self.tenacity = 'sectile'
            self.magnetic = 0
            self.acid = 0

            self.knowledge = "this softie is used to make baby powder."

            self.imageFile = 'Phyllosilicate.png'

        self.image = game.image.load(self.imageFile)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
    def blit(self):
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery
        self.screen.blit(self.image,self.rect)
