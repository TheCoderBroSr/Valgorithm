import random, pygame, sys

def rand_arr(length, range):
    data = []
    start, end = range

    while len(data) != length:
        data.append(random.randint(start, end))

    return data

def my_sort(arr, type): #Sorting is ascending by default
    state = []

    if type == "bubble":
        for _ in range(len(arr)):
            for i in range(len(arr)-1):
                state.append(arr.copy())

                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return state

def draw_bars(arr, bar_region, color, surface):
    gap = (bar_region.width)//len(arr)
    i = 0

    for e in arr:
        bar = pygame.Rect(bar_region.left + gap*i, bar_region.top, gap/1.5, e)
        pygame.draw.rect(surface, color, bar)        
        i += 1

def end():
    pygame.display.quit()
    pygame.quit()
    sys.exit()