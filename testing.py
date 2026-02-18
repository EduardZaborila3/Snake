import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 50
FPS = 8

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
text_font = pygame.font.SysFont(None, 48)
secondary_text_font = pygame.font.SysFont(None, 30)

class Board:
    def __init__(self, width, height, size, text_color):
        self.width = width
        self.height = height
        self.block_size = size
        self.text_color = text_color
        self.rows = height // size
        self.cols = width // size

    def draw(self, surface):
        surface.fill(BLACK)
        for x in range(0, self.width, self.block_size):
            for y in range(0, self.height, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)

    def draw_text(self, text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        rect = img.get_rect(center=(x, y))
        screen.blit(img, rect)

class Food:
    def __init__(self, board, snake_body):
        self.board = board
        self.color = RED
        self.randomize_pos(snake_body)
        
    def randomize_pos(self, snake_body):
        rows = HEIGHT // BLOCK_SIZE
        cols = WIDTH // BLOCK_SIZE
        self.pos_x = random.randrange(cols) * BLOCK_SIZE
        self.pos_y = random.randrange(rows) * BLOCK_SIZE
        while [self.pos_x, self.pos_y] in snake_body:
            self.pos_x = random.randrange(cols) * BLOCK_SIZE
            self.pos_y = random.randrange(rows) * BLOCK_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.board.block_size, self.board.block_size))

class Snake:
    def __init__(self, start_x, start_y):
        self.body = [[start_x, start_y]]
        self.x_change = 0
        self.y_change = 0
        self.color = GREEN
        self.grow = False

    def change_direction(self, dx, dy):
        if (dx != 0 and self.x_change == -dx) or (dy != 0 and self.y_change == -dy):
            return
        
        self.x_change = dx
        self.y_change = dy

    def move(self):
        if self.x_change == 0 and self.y_change == 0:
            return
        
        head_x, head_y = self.body[0]
        new_x = head_x + self.x_change
        new_y = head_y + self.y_change

        if new_x >= WIDTH:
            new_x = 0
        elif new_x < 0:
            new_x = WIDTH - BLOCK_SIZE
        elif new_y >= HEIGHT:
            new_y = 0
        elif new_y < 0:
            new_y = HEIGHT - BLOCK_SIZE

        new_head = [new_x, new_y]

        self.body.insert(0, new_head)
        if self.grow:
            self.grow = False
        else:
            self.body.pop()

    def eat(self):
        self.grow = True

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        return False
    
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, BLACK, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE), 1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

game_board = Board(WIDTH, HEIGHT, BLOCK_SIZE, WHITE)
# snake init
start_x = (game_board.cols // 2) * BLOCK_SIZE
start_y = (game_board.rows // 2) * BLOCK_SIZE
snake = Snake(start_x, start_y)

food = Food(game_board, snake.body)

running = True
game_over = False
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  snake.change_direction(-BLOCK_SIZE, 0)
            elif event.key == pygame.K_d: snake.change_direction(BLOCK_SIZE, 0)
            elif event.key == pygame.K_w:    snake.change_direction(0, -BLOCK_SIZE)
            elif event.key == pygame.K_s:  snake.change_direction(0, BLOCK_SIZE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    screen.fill(BLACK)
                    start_x = (game_board.cols // 2) * BLOCK_SIZE
                    start_y = (game_board.rows // 2) * BLOCK_SIZE
                    snake.body = [[start_x, start_y]]
                    score = 0

    if not game_over:
        snake.move()
        snake_head_x = snake.body[0][0]
        snake_head_y = snake.body[0][1]

        if snake_head_x == food.pos_x and snake_head_y == food.pos_y:
            snake.eat()
            score += 1
            food.randomize_pos(snake.body)

        if snake.check_collision():
            game_over = True
            print("Game Over - You bit yourself")

    game_board.draw(screen) 
    food.draw(screen)
    snake.draw(screen)

    if game_over:
        game_board.draw_text("GAME OVER!", text_font, WHITE, WIDTH / 2, HEIGHT / 2)
        game_board.draw_text("Press 'R' to start a new game", secondary_text_font, WHITE, WIDTH / 2, HEIGHT / 2 + 30)
        game_board.draw_text(f"Score: {score}", secondary_text_font, WHITE, WIDTH / 2, HEIGHT / 2 + 60)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()




    