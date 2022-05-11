from matplotlib.pyplot import draw
import pygame, sys
from func import *

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 24

BLACK = (0,0,0)
BLUE = (5, 23, 61)
WHITE = (255, 255, 255)

pygame.display.set_caption("VAlgorithm")
clock = pygame.time.Clock()

bar_region = pygame.Rect(125, 100, WIDTH, HEIGHT)
bar_region.width -= bar_region.left*2
bar_region.height -= bar_region.top*1.75

bar_length = 50
bar_range = (40, bar_region.height - bar_region.top)
bar_data = rand_arr(bar_length, bar_range)

def draw_bars(arr, bar_region):
    gap = (bar_region.width)//len(arr)
    i = 0

    for e in arr:
        bar = pygame.Rect(bar_region.left + gap*i, bar_region.top, gap/1.5, e)
        pygame.draw.rect(WIN, BLUE, bar)        
        i += 1

def end():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

            if event.key == pygame.K_s:
                for stage in my_sort(bar_data, 'bubble'):
                    bar_data = stage

            if event.key == pygame.K_r:
                bar_data = rand_arr(bar_length, bar_range)

    WIN.fill(BLACK)
    draw_bars(bar_data, bar_region)

    pygame.display.update()