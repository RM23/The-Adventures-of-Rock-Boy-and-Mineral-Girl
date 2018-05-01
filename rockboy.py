import pygame as game

class RockBoy():
    """class for rock boy, the star of the show!"""

    #constants for character state
    def __init__(self,screen):
        #identify as whom the player is playing
        self.name = "Rock"
        
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        self.stage = "CHARACTER_SELECT"
        self.battleStage = "MENU"

        self.walkCounter = 0
        self.walkFrame = 0

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

        #and the same for the battles
        self.battleImage = game.image.load("RockBattle.png")
        self.battleRect = self.battleImage.get_rect()
        self.battleRect.left = self.screenRect.left
        self.battleRect.bottom = self.screenRect.bottom

        #walking images for animation (couldn't be bothered with spritesheets, hahahahahah)
        self.walkingImages = []
        self.walkingLeftImages = []
        for i in range(0,4):
            self.walkingImages.append(game.image.load(self.name+"Walk"+str(i+1)+".png"))
            self.walkingLeftImages.append(game.image.load(self.name+"WalkLeft"+str(i+1)+".png"))
        self.walkingImage = self.walkingImages[self.walkFrame]
        self.walkingLeftImage = self.walkingLeftImages[self.walkFrame]

        #set hit points and exp
        self.hp = 10
        self.exp = 0
        self.lvl = 1
        self.power = 0
        self.powerCap = 5
        
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

    def moving(self):
        if self.movingRight == True or self.movingLeft == True or self.movingUp == True or self.movingDown == True:
            return True
        else:
            return False

    def walkAnimate(self):
        if self.moving():
            if self.walkCounter >= 25:
                self.walkCounter = 0
                self.walkFrame += 1
                if self.walkFrame > 3:
                    self.walkFrame = 0
                self.walkingImage = self.walkingImages[self.walkFrame]
            else:
                self.walkCounter += 1
            
    def stopMovement(self):
        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

    def powerUp(self,i=1):
        if self.power + i <= self.powerCap:
            self.power += i
        else:
            self.power = self.powerCap

    def powerDown(self,i=2):
        self.power -= i
        
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

    def removeRock(self,rockList):
        for i in rockList:
            colliding = False
            if self.rect.right >= i.rect.left and self.rect.right <= i.rect.right and self.rect.centery >= i.rect.centery - 16 and self.rect.centery <= i.rect.centery + 16:
                colliding = True
            elif self.rect.left >= i.rect.left and self.rect.left <= i.rect.right and self.rect.centery >= i.rect.centery - 16 and self.rect.centery <= i.rect.centery + 16:
                colliding = True
            elif self.rect.bottom >= i.rect.top and self.rect.bottom <= i.rect.bottom and self.rect.centerx >= i.rect.centerx - 16 and self.rect.centerx <= i.rect.centerx + 16:
                colliding = True
            elif self.rect.top >= i.rect.top and self.rect.top <= i.rect.bottom and self.rect.centerx >= i.rect.centerx - 16 and self.rect.centerx <= i.rect.centerx + 16:
                colliding = True
            if colliding == True:
                i.rect.left = 3000
                i.rect.top = 3000
                break
            
    def setImage(self,fileName,selectName):
        self.image = game.image.load(fileName)
        self.rect = self.image.get_rect()
        self.rect.left = self.screenRect.left
        self.rect.bottom = self.screenRect.bottom

        self.selectImage = game.image.load(selectName)
        self.selectRect = self.selectImage.get_rect()
        self.selectRect.left = self.screenRect.centerx
        self.selectRect.bottom = self.screenRect.centery

        for i in range(0,4):
            self.walkingImages[i] = game.image.load(self.name+"Walk"+str(i+1)+".png")
            self.walkingLeftImages[i] = game.image.load(self.name+"WalkLeft"+str(i+1)+".png")
        self.walkingImage = self.walkingImages[self.walkFrame]
        self.walkingLeftImage = self.walkingLeftImages[self.walkFrame]

    def setBattleImage(self,fileName):
        self.battleImage = game.image.load(self.name+fileName)
        
    def blit(self):
        """Draw rock at current location"""
        self.screen.blit(self.image,self.rect)

    def selectBlit(self):
        """Blit used for the select screen only"""
        self.screen.blit(self.selectImage,self.selectRect)

    def battleBlit(self):
        """Blit used during battles"""
        self.screen.blit(self.battleImage,self.battleRect)

    def walkBlit(self):
        """Blit current walking frame"""
        if self.movingLeft == False:
            self.screen.blit(self.walkingImages[self.walkFrame],self.rect)
        elif self.movingLeft == True:
            self.screen.blit(self.walkingLeftImages[self.walkFrame],self.rect)
