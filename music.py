import pygame
from os import listdir
from os.path import isfile, join

def get_sound_file_paths(mypath):
    return [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

def main():
    pygame.init()
    mixer = pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=1024)

    song = pygame.mixer.Sound('music/basketball.wav')

    song.play()

    running = True

# Just for testing
    print get_sound_file_paths('music')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                print(event.type)
    pygame.quit()
main()