import pygame
import random
import time

screen = pygame.display.set_mode((500, 500))
screen.fill("white")


# initializing sound
pygame.mixer.init()
sound = "beep.mp3"
beep = pygame.mixer.Sound("beep.mp3")


def draw(x, y, height):
    pygame.draw.rect(screen, "black", pygame.Rect(x, y, 10, height))
    
    
rand = random.sample(range(0, 50), 50)   
 
 
delay = 0.004
running  = True
n = 0
 
while running:
    for event in pygame.event.get():
         running = False
    screen.fill("white")
    for i in range(50):
        h = (rand[i] * 8) + 10
        y_cord = 500 - h
        draw(10 * i, y_cord, h)
    if n >= len(rand) - 1:
        n =0
    if rand[n] > rand[n + 1]:
        rand[n], rand[n + 1] = rand[n + 1], rand[n]
        pygame.mixer.Sound.play(beep)
    pygame.display.flip()
    time.sleep(delay)
    n += 1