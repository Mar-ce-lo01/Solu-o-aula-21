import pygame #Baixe a biblioteca pip install pygame

pygame.mixer.init()

pygame.mixer.music.load('Coloque o local do arquivo aqui')
pygame.mixer.music.play()

x = input('Digite "sair" para encerrar a música: ')
if x.lower() == 'sair':
    pygame.mixer.music.stop()
    print('Música encerrada.')
