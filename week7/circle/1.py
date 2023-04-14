import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
x = 25
y = 25
done = False
clock = pygame.time.Clock()

def right():
    global x
    if x + 25 + 20 <= 510:
        x += 20

def left():
    global x
    if x - 25 - 20 >= 0:
        x -= 20

def down():
    global y
    if y + 25 + 20 <= 510:
        y += 20

def up():
    global y
    if y - 25 - 20 >= 0:
        y -= 20

check = True
while not done:
    
    pygame.display.flip()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            elif event.key == pygame.K_RIGHT:
                right()
            elif event.key == pygame.K_DOWN:
                down()
            elif event.key == pygame.K_UP:
                up()
        clock.tick(60)
        
pygame.quit()