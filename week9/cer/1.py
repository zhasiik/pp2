import pygame, random, sys, time

pygame.init()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
#gameover = pygame.image.load("images//GameOver.jpg")

FPS = 60 #кадров в секунду
FramePerSecond = pygame.time.Clock()

screen_widht = 400
screen_height = 600
speed = 5
score = 0
coin = 0

#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("week9\cer\images//road.png")

screen = pygame.display.set_mode((400,600))
screen.fill(white)
pygame.display.set_caption('RACER')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("week9\cer\images//Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_widht - 40), 0)
        
    def move(self):
        global score
        self.rect.move_ip(0,speed + 2)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            
    #def draw(self,surface):
     #   surface.blit(self.image, self.rect)
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("week9\cer\images//player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed[pygame.K_DOWN]:
            self.rect.move_ip(0, +5)
        if self.rect.left >0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_widht:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(+5, 0)  
                
    def draw(self,surface):
        surface.blit(self.image,self.rect) 

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('week9\cer\images//1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, screen_widht - 30), 0)     
    
    def move(self):
        self.rect.move_ip(0, speed - 1)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, screen_widht - 30), 0)
            
class Bonus(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('week9\cer\images//metal.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, screen_widht - 30), 0)
        self.ayou = 0
        
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.image = pygame.image.load("week9\cer\images//metal.png")
            self.ayou = 0
        
P1 = Player()
E = Enemy()
C = Coin()
B = Bonus()

enemies = pygame.sprite.Group()
enemies.add(E)
bonus = pygame.sprite.Group()
bonus.add(B)
coins = pygame.sprite.Group()
coins.add(C)
all_sprites = pygame.sprite.Group()
new_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E)
all_sprites.add(C)
new_sprites.add(B)


inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

show_bonus = False 
bonus_timer = 0
bbc = 0
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #P1.update()
    #E.move()
    #P1.draw(screen)
    #E.draw(screen)
    
    #screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    scores = font_small.render(str('SCORE'), True, black)
    screen.blit(scores, (10,10))
    COINS = font_small.render(str(coin), True, black)
    screen.blit(COINS, (130, 10))
    
    for entity in all_sprites: #moves all sprites
        screen.blit(entity.image, entity.rect)
        entity.move()
        
    if B.ayou >= 10:
        for things in new_sprites:
            screen.blit(things.image, things.rect)
            things.move()
        
    if pygame.sprite.spritecollideany(P1, enemies): #столкновение Р1 и Е
        #pygame.image.load("images//GameOver.jpg")
        screen.fill(red)
        pygame.mixer.Sound('week9\cer\mp3//crash.wav').play()
        time.sleep(0.5)
        
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
           entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound("week9\cer\mp3//coin.mp3").play()
        coin += 1 
        C.rect.top = 600
        B.ayou += 1
        
    if pygame.sprite.spritecollideany(P1, bonus):
        B.ayou = 0
        show_bonus = Truebonus_timer = pygame.time.get_t1icks()
        pygame.mixer.Sound("week9\cer\mp3//coin.mp3").play()
        coin += 3
        B.rect.top = 600
    
    if show_bonus:
        bonuss = font_small.render("+3$", True, red)
        screen.blit(bonuss, (130, 50))
        if pygame.time.get_ticks() - bonus_timer >=20000:
            show_bonus = False
        
       
    pygame.display.update()
    pygame.display.flip()
    FramePerSecond.tick(FPS)