
import math
import pygame

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

radius = 5
last_pos = (0, 0)
first_pos = (0, 0)
draw_on = False
color = BLACK
last_color = BLACK
mode = "draw"
firsttap = False


###
def main():
    global BLUE, GREEN, RED, BLACK, WHITE, radius, last_pos, draw_on, color
    global mode, firsttap, path, first_pos
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen2 = screen.copy()
    pygame.display.set_caption('Paint')
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    
    eraser = pygame.image.load("week8\paint\eraser.png")
    eraser = pygame.transform.scale(eraser, (50, 50))
    
    pen = pygame.image.load("week8\paint\pen.png")
    pen = pygame.transform.scale(pen, (50, 50))

    globalrect = pygame.Rect(895, -5, 150, 410)

    eraserrect = pygame.Rect(950, 0, 50, 50)

    circlerect = pygame.Rect(950, 50, 50, 50)

    rectrect = pygame.Rect(900, 50, 50, 50)

    penrect = pygame.Rect(900, 0, 50, 50)

    redrect = pygame.Rect(950, 150, 50, 50)

    greenrect = pygame.Rect(900, 150, 50, 50)

    bluerect = pygame.Rect(950, 200, 50, 50)

    blackrect = pygame.Rect(900, 200, 50, 50)

    squarerect = pygame.Rect(900, 300, 50, 50)

    equitrirect = pygame.Rect(950, 300, 50, 50)

    righttrirect = pygame.Rect(900, 350, 50, 50)

    rombrect = pygame.Rect(950, 350, 50, 50)

    while True:
        
        pygame.draw.rect(screen, BLACK, globalrect)
        pygame.draw.rect(screen, WHITE, (897, -3, 150, 404))
        
        screen.blit(eraser, (950, 0))
        screen.blit(pen, (900, 0))
       
        pygame.draw.circle(screen, color, (975, 75), 25)
        pygame.draw.circle(screen, WHITE, (975, 75), 22)
        
        pygame.draw.rect(screen, color, (900, 50, 47, 47))
        pygame.draw.rect(screen, WHITE, (903, 53, 41, 41))

        pygame.draw.rect(screen, color, (900, 300, 47, 47))
        pygame.draw.rect(screen, WHITE, (903, 303, 41, 41))

        pygame.draw.polygon(screen, color, ((900, 350), (900, 397), (947, 397)))
        pygame.draw.polygon(screen, WHITE, ((902, 354), (903, 394), (940, 393)))

        pygame.draw.polygon(screen, color, ((950, 347), (975, 300), (1000, 347)))
        pygame.draw.polygon(screen, WHITE, ((955, 342), (975, 305), (995, 342)))

        pygame.draw.polygon(screen, color, ((975, 350), (950, 374), (975, 400), (1000, 374)))
        pygame.draw.polygon(screen, WHITE, ((975, 354), (954, 374), (975, 396), (996, 374)))

        

        
        

        pygame.draw.rect(screen, RED, redrect)
        pygame.draw.rect(screen, GREEN, greenrect)
        pygame.draw.rect(screen, BLUE, bluerect)
        pygame.draw.rect(screen, BLACK, blackrect)
        
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return
                elif event.key == pygame.K_w and ctrl_held:
                    return
                elif event.key == pygame.K_ESCAPE:
                    return

                # to control radius
                elif event.key == pygame.K_UP:
                    radius = min(radius + 2.5, 20)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 2.5)
                
                # determine if a letter key was pressed
                elif event.key == pygame.K_r:
                    color = RED
                    last_color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                    last_color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                    last_color = BLUE

                # determine if a num was pressed to switch mode
                elif event.key == pygame.K_1:
                    mode = "draw"
                elif event.key == pygame.K_2:
                    mode = "erase"
                elif event.key == pygame.K_3:
                    mode = "draw_rect"
                elif event.key == pygame.K_4:
                    mode = "draw_circle"
                elif event.key == pygame.K_5:
                    mode = "draw_square"
                elif event.key == pygame.K_6:
                    mode = "draw_righttriangle"
                elif event.key == pygame.K_7:
                    mode = "draw_equitriangle"
                elif event.key == pygame.K_8:
                    mode = "draw_romb"
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:

            #if was clicked copy our screen to screen2
                screen2 = screen.copy()
                pos = pygame.mouse.get_pos()
                if eraserrect.collidepoint(pos):
                    mode = "erase"
                elif penrect.collidepoint(pos):
                    mode = "draw"
                elif rectrect.collidepoint(pos):
                    mode = "draw_rect"
                elif circlerect.collidepoint(pos):
                    mode = "draw_circle"
                elif squarerect.collidepoint(pos):
                    mode = "draw_square"
                elif equitrirect.collidepoint(pos):
                    mode = "draw_equitriangle"
                elif righttrirect.collidepoint(pos):
                    mode = "draw_righttriangle"
                elif rombrect.collidepoint(pos):
                    mode = "draw_romb"
                elif redrect.collidepoint(pos):
                    color = RED
                elif greenrect.collidepoint(pos):
                    color = GREEN
                elif blackrect.collidepoint(pos):
                    color = BLACK
                elif bluerect.collidepoint(pos):
                    color = BLUE
                

                if not firsttap:
                    firsttap = True
                    first_pos = event.pos
                draw_on = True
                

            elif event.type == pygame.MOUSEBUTTONUP:

            #stop drawing
                draw_on = False
                firsttap = False
                    
                
            elif event.type == pygame.MOUSEMOTION:

            #to know that we are moving our mouse
                pos = pygame.mouse.get_pos()
                if not globalrect.collidepoint(pos) and draw_on == True:
                    if mode == "draw":
                        drawLineBetween(screen, event.pos, last_pos)
                    if mode == "erase":
                        erase(screen, event.pos, last_pos)
                    if mode == "draw_rect":
                        drawRect(screen, screen2, first_pos, event.pos)
                    if mode == "draw_circle":
                        drawCircle(screen, screen2, first_pos, event.pos)
                    if mode == "draw_square":
                        drawSquare(screen, screen2, first_pos, event.pos)
                    if mode == "draw_righttriangle":
                        drawRightTriangle(screen, screen2, first_pos, event.pos)
                    if mode == "draw_equitriangle":
                        drawEquiTriangle(screen, screen2, first_pos, event.pos)
                    if mode == "draw_romb":
                        drawRomb(screen, screen2, first_pos, event.pos)
                        
                last_pos = event.pos                    
                

        
        pygame.display.update()
        clock.tick(10000)

###
        
def drawLineBetween(screen, start, end):

    pygame.draw.circle(screen, color, start, radius)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    dist = max(abs(dx), abs(dy))

    for i in range(dist):
        x = int(start[0] + float(i) / dist * dx)
        y = int(start[1] + float(i) / dist * dy)
        pygame.draw.circle(screen, color, (x, y), radius)
###

def erase(screen, start, end):

    color = WHITE
    pygame.draw.circle(screen, color, start, radius)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    dist = max(abs(dx), abs(dy))

    for i in range(dist):
        x = int(start[0] + float(i) / dist * dx)
        y = int(start[1] + float(i) / dist * dy)
        pygame.draw.circle(screen, color, (x, y), radius)

    color = last_color
###

def drawRect(screen, screen2, start, end):

    lx = min(end[0], start[0])
    rx = max(end[0], start[0])
    ly = min(end[1], start[1])
    ry = max(end[1], start[1])
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(lx, ly, rx - lx, ry - ly))
    
###

def drawSquare(screen, screen2, start, end):

    lx = min(end[0], start[0])
    rx = max(end[0], start[0])
    ly = min(end[1], start[1])
    ry = max(end[1], start[1])
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    #a equals to lenght of one side
    a = min(rx - lx, ry - ly)
    pygame.draw.rect(screen, color, pygame.Rect(lx, ly, a, a))
    
###

def drawRightTriangle(screen, screen2, start, end):

    lx = start[0]
    rx = end[0]
    ly = start[1]
    ry = end[1]
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    #pygame.draw.polygon(screen, (0, 255, 255), ((25,75),(320,125),(250,375)))
    pygame.draw.polygon(screen, color, ((lx, ly), (lx, ry), (rx, ry)))
    
###

def drawEquiTriangle(screen, screen2, start, end):

    lx = start[0]
    rx = end[0]
    ly = start[1]
    ry = end[1]
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    #a equal to size of one side
    a = rx - lx
    y = ry - ly
    while(abs(y) > 0.001 and abs(y) < abs(math.sqrt(3) * a / 2)):
        if a > 0: a -= 0.001
        else: a += 0.001
    z = 0
    if a > 0:
        if y > 0: z = math.sqrt(3) * a / 2
        elif y < 0: z = -1 * math.sqrt(3) * a / 2
    elif a < 0:
        if y > 0: z = abs(math.sqrt(3) * a / 2)
        elif y < 0: z = math.sqrt(3) * a / 2
    pygame.draw.polygon(screen, color, ((lx + a/2, ly), (lx, ly + z), (lx + a, ly + z)))
    
###

def drawRomb(screen, screen2, start, end):

    lx = min(end[0], start[0])
    rx = max(end[0], start[0])
    ly = min(end[1], start[1])
    ry = max(end[1], start[1])
    x = (rx - lx) / 2
    y = (ry - ly) / 2
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    pygame.draw.polygon(screen, color, ((lx + x, ly), (lx, ly + y), (rx - x, ry), (rx, ry - y)))

###

def drawCircle(screen, screen2, start, end):

    x1 = min(end[0], start[0])
    x2 = max(end[0], start[0])
    y1 = min(end[1], start[1])
    y2 = max(end[1], start[1])
    #(x1, y1) = start
    #(x2, y2) = end 
    r = min((x2 - x1) / 2, (y2 - y1) / 2)
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    pygame.draw.circle(screen, color, (x1 + r, y1 + r), r)
###


main()
pygame.quit()