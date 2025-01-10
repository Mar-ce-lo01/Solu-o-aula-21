import pygame

pygame.mixer.init()

pygame.mixer.music.load('C:/Users/Marcelo/Downloads/musica.mp3.mp3')
pygame.mixer.music.play()

x = input('Digite "sair" para encerrar a música: ')
if x.lower() == 'sair':
    pygame.mixer.music.stop()
    print('Música encerrada.')