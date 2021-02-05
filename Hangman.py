import pygame
import math
import random

pygame.init()

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)

# Setup display
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game!")

# Button variable
RADIUS = 20
GAP = 15
letters = [] 
startx = round((width - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i), True])

# Fonts
LETTERS_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("Hangman" + str(i) + ".png")
    images.append(image)

print(images)

# Game variables
hangamn_status = 0
words = ["HANGMAN", "DYNAMO", "ELON", "MICROSOFT", "GOOGLE", "INCEPTION", "CODING"]
word = random.choice(words)
guessed = []

# Setup gameloop
fps = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (width/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))


    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3 )
            text = LETTERS_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))


    win.blit(images[hangamn_status],(150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(fps)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangamn_status += 1
    won = True
    for letter in word:
        if letter not in guessed:
            won  = False
            break
    if won:
        display_message("YOU WON!")
        break

    if hangamn_status == 6:
        display_message("YOU LOST!")
        break

pygame.quit()
