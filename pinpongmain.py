from random import randint
from pygame import *
font.init()
clock = time.Clock()
FPS = 120
speed = 10
win_height = 500
win_width = 700
finish = False
window = display.set_mode((win_width,win_height))
display.set_caption('please close this game, it sucks')
bg_color = (255, 227, 145)
window.fill(bg_color)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()