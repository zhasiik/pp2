import pygame, sys
from pygame.locals import *
import random, time
pygame.init()

path = "week8\cer\ile"
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0



#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

BACKGROUND = pygame.image.load(path + "\\Street.png")

FPS = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((400, 600))
DISPLAY.fill(WHITE)
pygame.display.set_caption("mYgAmE")

###
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path + "\\Enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 98))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, SCREEN_WIDTH-60), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            global SCORE
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(60, SCREEN_WIDTH-60), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
###

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path + "\\Player.png")
        self.image = pygame.transform.scale(self.image, (40, 98))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-6, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(6, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
###
        
#Adding class Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path + "\\Coin.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH-50), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH-50), 0)

    def pluspoint(self):
        global COIN
        COIN += 1
        self.rect.top = 0
        self.rect.center = (random.randint(50, SCREEN_WIDTH-50), 0)
        DISPLAY.blit(self.image, self.rect)
###
        
#Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Adding new User event for background music
PLAY_MUSIC = pygame.USEREVENT + 2
pygame.time.set_timer(PLAY_MUSIC, 16000)
pygame.mixer.Sound(path + "\\background.wav").play()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == PLAY_MUSIC:
            pygame.mixer.Sound(path + "\\background.wav").play()

    DISPLAY.blit(BACKGROUND, (0, 0))
    #DISPLAY.fill(WHITE)
    SCORES = font_small.render(str(SCORE), True, BLACK)
    COINS = font_small.render(str(COIN), True, BLUE)
    DISPLAY.blit(SCORES, (10, 10))
    DISPLAY.blit(COINS, (SCREEN_WIDTH - 30, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAY.blit(entity.image, entity.rect)

    #To be run if collision occurs between Player and Coin
    if pygame.sprite.collide_rect(P1, C1):
        
        C1.pluspoint()
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(path + "\\crash.wav").play()
        time.sleep(0.5)
        
        DISPLAY.fill(BLUE)
        DISPLAY.blit(game_over, (30, 250))
        coin_text = font.render(f"Coins: {COIN}", True, BLACK)
        DISPLAY.blit(coin_text, (50, 50))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()
        
    
    pygame.display.update()
    FPS.tick(60)