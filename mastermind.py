import pygame
import random

pygame.init()

W = 450
H = 800
timer = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('Master Mind')
font = pygame.font.Font('freesansbold.ttf' , 19)

bg = int(.125*255) , int(.165*255), int(.267*255) #you can change these for diffrent clours .
white = 'white'
gray = 'gray'
black = 'black'
red = 'red'
orange = 'orange'
yellow = 'yellow'
green = 'green'
blue = 'blue'
purple = 'purple'
# doing this so their stored as variables and not strings
#game list
choice_colors = [red, orange, yellow, green, blue, purple]  # change this up
answer_colors = [random.choice(choice_colors), random.choice(choice_colors),
                 random.choice(choice_colors), random.choice(choice_colors)]
guess_colors = [[white, white, white, white],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray],
                [gray, gray, gray, gray]]
fb_colors = [[gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray],
             [gray, gray, gray, gray]]




# drawing screen static images
def draw_screen():
    #horiz lines
    for i in range(14):
        pygame.draw.line(screen , white , (0 , H/13 * i), (W, H/13 * i), 3)
    #vert lines
    pygame.draw.line(screen, white, (W / 5, 0), (W / 5, H), 3)
    pygame.draw.line(screen, white, (0, 0), (0, H), 3)
    pygame.draw.line(screen, white, (W - 1, 0), (W - 1, H), 3)

    for i in range (10):
        for j in range (4):
            pygame.draw.circle(screen , guess_colors[i][j]),
            (W / 5 * j + 1.5), ())

    for i in range(4):
        pygame.draw.circle(screen, answer_colors[i], (W / 5 * (i + 1.5), H / 26), H / 30)






run = True
while run:
    timer.tick(fps)
    screen.fill(bg)
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()



