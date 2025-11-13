import pygame, time

screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Bars Visualization")
screen.fill((0, 0, 0))

def visualise(n, array, delay=0.05, highlight=None):
    screen.fill((0, 0, 0))
    if highlight is None:
        highlight = ()
    for i in range(n):
        if i in highlight:
            color = (0, 255, 0)
        else:
            color = (255, 255, 255)
        pygame.draw.rect(
            screen,
            color,
            ((screen_width / 2 - n * 10 / 2) + i * 10, screen_height / 2 - array[i] * 5, 5, array[i] * 5)
        )
    
    pygame.display.flip()

def bubble_sort(array, visual_fn=False, delay=0.05):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
            if visual_fn:
                time.sleep(delay)
                visual_fn(len(array), array, highlight=(j, j + 1))   

def insert_sort(array, visualise=False, delay=0.05):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if visualise:
            visualise(len(array), array, highlight=(j + 1,))
            time.sleep(delay)

def radix_sort(array, visual_fn=False, delay=0.05):
    max1 = max(array)
    exp = 1
    while max1 // exp > 0:
        counting_sort(array, exp, visual_fn=visual_fn, delay=delay)
        exp *= 10

def counting_sort(array, exp, visual_fn=False, delay=0.05):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    for i in range(n):
        array[i] = output[i]
        print(array)
        if visual_fn:
            visual_fn(n, array, highlight=(i,))
            time.sleep(delay)
