import pygame

def main():
	pygame.init()
	mixer = pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)

	song = pygame.mixer.Sound('music/basketball.wav')

	song.play()

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break

	pygame.quit()

main()