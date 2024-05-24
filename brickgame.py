import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Ball properties
BALL_RADIUS = 8
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

# Brick properties
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_PADDING = 10
BRICK_OFFSET_TOP = 30
BRICK_OFFSET_LEFT = 30
ROW_COUNT = 5
COLUMN_COUNT = 10

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PADDLE_SPEED
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_RADIUS * 2, BALL_RADIUS * 2])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - BALL_RADIUS
        self.rect.y = SCREEN_HEIGHT // 2 - BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_RADIUS * 2:
            self.speed_x *= -1
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= SCREEN_HEIGHT:
            self.speed_y = 0
            self.speed_x = 0
            game_over()

# Brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Initialize paddle, ball, and bricks
def initialize_game():
    global paddle, ball, all_sprites, bricks

    paddle = Paddle()
    ball = Ball()

    all_sprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()

    all_sprites.add(paddle)
    all_sprites.add(ball)

    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            brick = Brick(
                BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING),
                BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
            )
            all_sprites.add(brick)
            bricks.add(brick)

# Display restart button
def game_over():
    global running
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    SCREEN.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))

    pygame.draw.rect(SCREEN, GRAY, [SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 50, 200, 50])
    restart_text = font.render("Restart", True, BLACK)
    SCREEN.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 55))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if SCREEN_WIDTH//2 - 100 < mouse_x < SCREEN_WIDTH//2 + 100 and SCREEN_HEIGHT//2 + 50 < mouse_y < SCREEN_HEIGHT//2 + 100:
                    waiting = False
                    initialize_game()

# Initialize the game for the first time
initialize_game()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update paddle and ball
    all_sprites.update()

    # Ball and paddle collision
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y *= -1

    # Ball and brick collision
    brick_collisions = pygame.sprite.spritecollide(ball, bricks, True)
    if brick_collisions:
        ball.speed_y *= -1

    # Drawing everything
    SCREEN.fill(BLACK)
    all_sprites.draw(SCREEN)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
