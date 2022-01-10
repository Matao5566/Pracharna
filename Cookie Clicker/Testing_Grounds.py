import pygame
from pygame import mixer
file = 'OST3.wav'
pygame.init()
mixer.music.load(file)
mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.