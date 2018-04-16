import pygame as game

class RockBoy():
    """class for rock boy, the star of the show!"""

    #constants for character state
    def __init__(self,screen):
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        self.stage = "CHARACTER_SELECT"

        #load rock image and get its rect
        self.image = game.image.load("RockBoy.png")
        self.rect = self.image.get_rect()
        self.rect.left = self.screenRect.left
        self.rect.bottom = self.screenRect.bottom
        
        #do the same for the select image
        self.selectImage = game.image.load("RockSelect.png")
        self.selectRect = self.selectImage.get_rect()
        self.selectRect.left = self.screenRect.centerx
        self.selectRect.bottom = self.screenRect.centery
        
        #flags for continuous movement
        self.movingRight = False
        self.movingLeft = False
        self.movingDown = False
        self.movingUp = False

        #variable for state of character

        #variable for movement speed
        self.speed = 1

    def checkCollision(self,tiles):
        colliding = False
        for i in tiles:
            if self.rect.right > i.rect.left and self.rect.right < i.rect.right and self.rect.centery >= i.rect.centery - 16 and self.rect.centery <= i.rect.centery + 16:
                movingRight = False
                self.rect.right = i.rect.left
                colliding = True
            elif self.rect.left > i.rect.left and self.rect.left < i.rect.right and self.rect.centery >= i.rect.centery - 16 and self.rect.centery <= i.rect.centery + 16:
                movingLeft = False
                self.rect.left = i.rect.right
                colliding = True
            elif self.rect.bottom > i.rect.top and self.rect.bottom < i.rect.bottom and self.rect.centerx >= i.rect.centerx - 16 and self.rect.centerx <= i.rect.centerx + 16:
                movingDown = False
                self.rect.bottom = i.rect.top
                colliding = True
            elif self.rect.top > i.rect.top and self.rect.top < i.rect.bottom and self.rect.centerx >= i.rect.centerx - 16 and self.rect.centerx <= i.rect.centerx + 16:
                movingUp = False
                self.rect.top = i.rect.bottom
                colliding = True
        if colliding == True:
            return True
        else:
            return False
        
    def updatePos(self):
        """Update character's position based on movement flag"""
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.rect.centerx += self.speed
        elif self.movingLeft and self.rect.left > self.screenRect.left:
            self.rect.centerx -= self.speed
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.rect.centery += self.speed
        elif self.movingUp and self.rect.top > self.screenRect.top:
            self.rect.centery -= self.speed
            
    def setImage(self,fileName,selectName):
        self.image = game.image.load(fileName)
        self.rect = self.image.get_rect()
        self.rect.left = self.screenRect.left
        self.rect.bottom = self.screenRect.bottom

        self.selectImage = game.image.load(selectName)
        self.selectRect = self.selectImage.get_rect()
        self.selectRect.left = self.screenRect.centerx
        self.selectRect.bottom = self.screenRect.centery
        
    def blit(self):
        """Draw rock at current location"""
        self.screen.blit(self.image,self.rect)

    def selectBlit(self):
        """Blit used for the select screen only"""
        self.screen.blit(self.selectImage,self.selectRect)
