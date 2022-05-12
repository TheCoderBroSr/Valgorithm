import pygame
from func import *

pygame.font.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 360

TITLE = pygame.font.SysFont('cooper black', 80)
PARA = pygame.font.SysFont('courier new', 40)

BLACK = (0,0,0)
BLUE = (5, 23, 61)
WHITE = (255, 255, 255)
GREEN = (20, 150, 40)

pygame.display.set_caption("VAlgorithm")
clock = pygame.time.Clock()

bar_region = pygame.Rect(125, 125, WIDTH, HEIGHT)
bar_region.width -= bar_region.left*2
bar_region.height -= bar_region.top*1.75

bar_number = 30
bar_range = (40, bar_region.height - bar_region.top)
bar_data = rand_arr(bar_number, bar_range)
bar_color = BLUE
frame_delay = 50

if bar_number > 20 and bar_number < 50:
    frame_delay = 10

if bar_number > 50:
    frame_delay = 0

stages = []
stage_index = 0

title = TITLE.render('VAlgorithm', 1, WHITE)
instruction = PARA.render('Press s to sort, r to reset bars', 1, WHITE)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: #Quit
                end()

            if event.key == pygame.K_s: #Initiate Sorting
                stages = my_sort(bar_data, 'bubble')

            if event.key == pygame.K_r: #Generate new bars
                stage_index = 0
                stages = []

                bar_data = rand_arr(bar_number, bar_range)
                bar_color = BLUE

    WIN.fill(BLACK)
    WIN.blit(title, ((WIDTH - title.get_width())//2, 20))
    WIN.blit(instruction, ((WIDTH - instruction.get_width())//2, HEIGHT - 40 - instruction.get_height()))

    draw_bars(bar_data, bar_region, bar_color, WIN)

    if stages:
        bar_data = stages[stage_index]

        if stage_index < len(stages)-1:
            stage_index += 1

        pygame.time.delay(frame_delay)

        if bar_data == stages[-1]:
            pygame.time.delay(100)
            bar_color = GREEN

    pygame.display.update()