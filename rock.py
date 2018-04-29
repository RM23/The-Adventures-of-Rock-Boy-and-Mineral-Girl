#file to hold class for rocks that need to be identified
import pygame as game
class Rock():
    def __init__(self,ID,screen):
        if (ID == 1):
            self.name = 'citrine'
            self.hardness = 7
            self.streak = 'white'
            self.opacitry = 'translucent'
            self.cleavage = 'none'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Quartz.png'
            
        elif (ID == 2):
            self.name = 'copper'
            self.hardness = 3
            self.streak = 'red'
            self.opacitry = 'opaque'
            self.cleavage = 'none'
            self.fracture = 'hackly'
            self.tenacity = 'ductile'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Copper.png'
            
        elif (ID == 3):
            self.name = 'ulexite'
            self.hardness = 2.5
            self.streak = 'white'
            self.opacitry = 'translucent'
            self.cleavage = 'prismatic'
            self.fracture = 'uneven'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Borate.png'
            
        elif (ID == 4):
            self.name = 'calcite'
            self.hardness = 3
            self.streak = 'white'
            self.opacitry = 'translucent'
            self.cleavage = 'rhombohedral'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 1

            self.imageFile = 'Carbonate.png'
            
        elif (ID == 5):
            self.name = 'dolomite'
            self.hardness = 4
            self.streak = 'white'
            self.opacitry = 'opaque'
            self.cleavage = 'rhombohedral'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 2

            self.imageFile = 'Carbonate.png'
            
        elif (ID == 6):
            self.name = 'halite'
            self.hardness = 2.5
            self.streak = 'white'
            self.opacitry = 'translucent'
            self.cleavage = 'cubic'
            self.fracture = 'conchoidal'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Halide.png'
            
        elif (ID == 7):
            self.name = 'goethite'
            self.hardness = 5
            self.streak = 'yellow'
            self.opacitry = 'opaque'
            self.cleavage = 'none'
            self.fracture = 'splintery'
            self.tenacity = 'brittle'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'IronOxide.png'
            
        elif (ID == 8):
            self.name = 'magnetite'
            self.hardness = 6
            self.streak = 'black'
            self.opacitry = 'opaque'
            self.cleavage = 'none'
            self.fracture = 'uneven'
            self.tenacity = 'brittle'
            self.magnetic = 1
            self.acid = 0

            self.imageFile = 'IronOxide.png'
            
        elif (ID == 9):
            self.name = 'kaolinite'
            self.hardness = 2
            self.streak = 'white'
            self.opacitry = 'opaque'
            self.cleavage = 'basal'
            self.fracture = 'earthy'
            self.tenacity = 'sectile'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Phyllosilicate.png'

        elif (ID == 10):
            self.name = 'talc'
            self.hardness = 1
            self.streak = 'white'
            self.opacitry = 'opaque'
            self.cleavage = 'basal'
            self.fracture = 'uneven'
            self.tenacity = 'sectile'
            self.magnetic = 0
            self.acid = 0

            self.imageFile = 'Phyllosilicate.png'

        self.image = game.image.load(self.imageFile)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
    def blit(self):
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery
        self.screen.blit(self.image,self.rect)
