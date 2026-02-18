import pygame
import random

WIDTH = 600
HEIGHT = 600

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 5
running = True

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

x = 300
y = 300
x_change = 0
y_change = 0

# board
board = []
BLOCK_SIZE = 50
rows = HEIGHT // BLOCK_SIZE
cols = HEIGHT // BLOCK_SIZE
for i in range(rows):
    current_row = []
    for j in range(cols):
        pos_x = j * BLOCK_SIZE
        pos_y = i * BLOCK_SIZE
        block_data = [pos_x, pos_y, 0, "black"]
        current_row.append(block_data)
    board.append(current_row)

rb_row = 0
rb_col = 0
def gen_red_block():
    rb_row = random.randrange(rows)
    rb_col = random.randrange(cols)
    pos_x = rb_col * BLOCK_SIZE
    pos_y = rb_row * BLOCK_SIZE
    board[rb_row][rb_col] = [pos_x, pos_y, 2, RED]

# start_row = rows // 2
# start_col = cols // 2
# snake_length = 2
# for i in range(snake_length):
#     current_row = start_row - i
#     current_col = start_col
#     x = current_col * BLOCK_SIZE
#     y = current_row * BLOCK_SIZE
#     board[current_row][current_col] = [x, y, 1, GREEN]
def draw_board():
    screen.fill("black")
    for i in range(rows):
        for j in range(cols):
            block = board[i][j]
            x = block[0]
            y = block[1]
            color = block[3]
            pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, "gray", (x, y, BLOCK_SIZE, BLOCK_SIZE), 1)

gen_red_block()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # generate the red point random on the table
    # row = random.randrange(rows)
    # col = random.randrange(cols)
    # pos_x = col * BLOCK_SIZE
    # pos_y = row * BLOCK_SIZE
    # board[row][col] = [pos_x, pos_y, 2, RED]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x_change != BLOCK_SIZE or y_change != 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
            elif event.key == pygame.K_d:
                if x_change != -BLOCK_SIZE or y_change != 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
            elif event.key == pygame.K_s:
                if x_change != 0 or y_change != -BLOCK_SIZE:
                    x_change = 0
                    y_change = BLOCK_SIZE
            elif event.key == pygame.K_w:
                if x_change != 0 or y_change != BLOCK_SIZE:
                    x_change = 0
                    y_change = -BLOCK_SIZE
    
    x += x_change
    y += y_change

    red_block = board[rb_row][rb_col]
    if x == red_block[0] and y == red_block[1]:
        red_block[3] = "black"
        gen_red_block()

    
    draw_board()
    pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))
    # flip() the display to put your work on screen
    # pygame.display.flip()
    clock.tick(FPS)  # limits FPS to 60
     
    pygame.display.update()

pygame.quit()