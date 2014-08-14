import pygame
from os import listdir
from os.path import isfile, join
import requests

def get_sound_file_paths(mypath):
    return [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

def main():
    pygame.init()
    mixer = pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=1024)

    song = pygame.mixer.Sound('music/basketball.wav')
    # song = pygame.mixer.Sound('music/song1.mp3')

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

def isRaining():
    r = requests.get("http://apis.is/weather/observations/en?stations=1,422&time=1h&anytime=0")
    
    # get JSONObject
    jsonResult = r.json()
    results = jsonResult['results']
    reykjavik = results[0]
    
    ## now we can get what information what we want
    weatherNow = reykjavik['W']
    rain = "Rain"
    lightRain = "Light rain"
    isRaining = weatherNow == rain or weatherNow == lightRain

    #print isRaining
    return isRaining

isRaining = isRaining()
print isRaining