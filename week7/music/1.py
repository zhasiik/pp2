import pygame
import os

pygame.init()


screen = pygame.display.set_mode((550, 350))


dirr = "week10\music\muzz"
music = os.listdir(dirr)

font = pygame.font.SysFont("impact", 48)


done = False
cur_song = 0
pause_pos = 0
old_song_time = 0
playing = False

pygame.mixer.music.load(os.path.join(dirr, music[cur_song]))
clock = pygame.time.Clock()

def play():
    global playing
    pygame.mixer.music.play(start = pause_pos)
    playing = True

def pause():
    global playing, pause_pos, old_song_time
    pygame.mixer.music.pause()
    pause_pos = pygame.mixer.music.get_pos() / 1000 + old_song_time
    old_song_time += pygame.mixer.music.get_pos() / 1000
    playing = False

def nextt():
    global cur_song, playing, pause_pos, old_song_time
    old_song_time = 0
    pause_pos = 0
    cur_song += 1
    if cur_song >= len(music):
        cur_song = 0
    pygame.mixer.music.load(os.path.join(dirr, music[cur_song]))
    if playing:
        pygame.mixer.music.play()

def prev():
    global cur_song, playing, pause_pos, old_song_time
    old_song_time = 0
    pause_pos = 0
    cur_song -= 1
    if cur_song < 0:
        cur_song = len(music) - 1
    pygame.mixer.music.load(os.path.join(dirr, music[cur_song]))
    if playing:
        pygame.mixer.music.play()

while not done:

    pygame.display.flip()
    screen.fill((0, 0, 0))
    title = font.render(music[cur_song], True, (255, 0, 255))
    screen.blit(title, (150, 150))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pause()
                else:
                    play()

            elif event.key == pygame.K_LEFT:
                nextt()

            elif event.key == pygame.K_RIGHT:
                prev()

    clock.tick(60)
    
pygame.quit()