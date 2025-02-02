# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 1000
timer = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Mastermind')
font = pygame.font.Font('freesansbold.ttf', 20)
# game variables
bg = 'black'
white = 'white'
gray = 'gray'
black = 'black'
red = 'red'
orange = 'coral3'
yellow = 'gold'
green = 'green'
blue = 'blue'
purple = 'purple'
pink = 'pink'
aqua = 'aqua'
# game lists
choice_colors = [red, orange, yellow, green, blue, purple]
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
selected = 0
turn = 0
selected_color = white
solved_color = black
solved = True
check = False

# class for Buttons
class Button:
    def __init__(self, text, cords, size):
        self.text = text
        self.cords = cords
        self.size = size
        self.rect = pygame.rect.Rect(self.cords, self.size)

    def draw(self):
        if self.rect.collidepoint(mouse_cords) and mouse_buttons[0]:
            color = 'light blue'
        elif self.rect.collidepoint(mouse_cords):
            color = 'light gray'
        else:
            color = 'dark gray'
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, black, self.rect, 1)
        screen.blit(font.render(self.text, True, black),
                    (self.cords[0] + self.size[0] / 4, self.cords[1] + self.size[1] / 3))

# draw the screen components
def draw_screen():
    # active turn rectangle
    pygame.draw.rect(screen, 'gray38', [0, 10 * HEIGHT / 13 - turn * HEIGHT / 13, WIDTH, HEIGHT / 13])
    # guess squares
    for i in range(10):
        for j in range(4):
            x = WIDTH / 5 * (j + 1.5) - HEIGHT / 30
            y = (11 * HEIGHT / 13) - (HEIGHT / 13 * i) - HEIGHT / 26 - HEIGHT / 30
            pygame.draw.rect(screen, guess_colors[i][j], (x, y, HEIGHT / 15, HEIGHT / 15))
    # feedback squares
    for i in range(10):
        for j in range(4):
            row = j // 2
            col = j % 2
            x = 25 + (col * WIDTH / 12) - HEIGHT / 60
            y = (11 * HEIGHT / 13) - (HEIGHT / 13 * i) - (HEIGHT / 26 * (row + 0.5)) - HEIGHT / 60
            pygame.draw.rect(screen, fb_colors[i][j], (x, y, HEIGHT / 30, HEIGHT / 30))
    # answer squares
    for i in range(4):
        x = WIDTH / 5 * (i + 1.5) - HEIGHT / 30
        y = HEIGHT / 26 - HEIGHT / 30
        pygame.draw.rect(screen, answer_colors[i], (x, y, HEIGHT / 15, HEIGHT / 15))
    # answer cover rectangle
    if not solved:
        pygame.draw.rect(screen, solved_color, [WIDTH / 5, 0, 4 * WIDTH / 5, HEIGHT / 13])
    # options colors to select and selected square
    x = WIDTH / 7 * (selected + 1) - HEIGHT / 26
    y = 11.5 * HEIGHT / 13 - HEIGHT / 26
    pygame.draw.rect(screen, selected_color, (x, y, HEIGHT / 13, HEIGHT / 13))
    for i in range(6):
        x = WIDTH / 7 * (i + 1) - HEIGHT / 30
        y = 11.5 * HEIGHT / 13 - HEIGHT / 30
        pygame.draw.rect(screen, choice_colors[i], (x, y, HEIGHT / 15, HEIGHT / 15))
    # buttons
    submit_btn.draw()
    restart_btn.draw()
    # horizontal lines
    for i in range(14):
        pygame.draw.line(screen, white, (0, HEIGHT / 13 * i), (WIDTH, HEIGHT / 13 * i), 3)
    # vertical lines
    pygame.draw.line(screen, white, (WIDTH / 5, 0), (WIDTH / 5, 11 * HEIGHT / 13), 3)
    pygame.draw.line(screen, white, (0, 0), (0, HEIGHT), 3)
    pygame.draw.line(screen, white, (WIDTH - 1, 0), (WIDTH - 1, HEIGHT), 3)

# display winning message
def draw_winning_message():
    pygame.draw.rect(screen, white, [WIDTH / 4, HEIGHT / 2 - 50, WIDTH / 2, 100])
    text = font.render("Congratulations! You Win!", True, black)
    screen.blit(text, (WIDTH / 4 + 10, HEIGHT / 2 - 10))

def check_guess():
    global solved
    check_turn = guess_colors[turn]
    responses = [gray, gray, gray, gray]
    response_index = 0
    for i in range(4):
        if check_turn[i] == answer_colors[i]:
            responses[response_index] = green
            response_index += 1
            print(f'{check_turn[i]} is in the right spot')
        elif check_turn[i] in answer_colors:
            guess_count = check_turn.count(check_turn[i])
            answer_count = answer_colors.count(check_turn[i])
            only_input = (guess_count == 1) # true or false if this guess only appears once
            several_outputs = (answer_count >= guess_count) # t or f if more in ans than guess
            these_indexes = []
            answer_indexes = []
            for j in range(4):
                if check_turn[j] == check_turn[i] and check_turn[j] != answer_colors[j]:
                    these_indexes.append(j)
                if answer_colors[j] == check_turn[i] and check_turn[j] != answer_colors[j]:
                    answer_indexes.append(j)
            count_this = these_indexes.index(i) < len(answer_indexes)
            if only_input or several_outputs or count_this:
                responses[response_index] = red
                response_index += 1
                print(f'{check_turn[i]} is in the answer but wrong spot')
    random.shuffle(responses)
    print(responses)
    fb_colors[turn] = responses
    if responses.count(green) == 4:
        solved = True

run = True
submit_btn = Button('Submit guess', (0, 12 * HEIGHT / 13), (WIDTH / 2, HEIGHT / 13))
restart_btn = Button('Replay', (WIDTH / 2, 12 * HEIGHT / 13), (WIDTH / 2, HEIGHT / 13))
while run:
    timer.tick(fps)
    screen.fill(bg)
    mouse_cords = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    draw_screen()

    if solved:
        draw_winning_message()

    if check:
        check_guess()
        turn += 1
        for i in range(4):
            guess_colors[turn][i] = white
        check = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_btn.rect.collidepoint(event.pos):
                turn = 0
                solved = False
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
            if WIDTH / 14 < event.pos[0] < 13 * WIDTH / 14 \
                    and 11 * HEIGHT / 13 < event.pos[1] < 12 * HEIGHT / 13:
                x_pos = event.pos[0] // (WIDTH / 14)
                selected = int((x_pos - 1) // 2)
            elif WIDTH / 5 < event.pos[0] \
                    and (10 - turn) * HEIGHT / 13 < event.pos[1] < (11 - turn) * HEIGHT / 13:
                x_pos = int(event.pos[0] // (WIDTH / 5))
                guess_colors[turn][x_pos - 1] = choice_colors[selected]
            elif submit_btn.rect.collidepoint(event.pos):
                if white not in guess_colors[turn]:
                    check = True

    pygame.display.flip()
pygame.quit()



