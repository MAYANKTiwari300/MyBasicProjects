import random
import pygame

# --- Constants ---
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
DARK_GREEN = (22, 115, 61)
RED = (231, 76, 60)
BLUE = (52, 152, 219)
YELLOW = (241, 196, 15)
BACKGROUND = (14, 22, 33)
PANEL = (25, 41, 55)

# --- Setup ---
pygame.init()
pygame.display.set_caption("Snake Deluxe")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
font_title = pygame.font.SysFont(None, 72)
font_ui = pygame.font.SysFont(None, 38)
font_small = pygame.font.SysFont(None, 26)

# --- Game State ---
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
direction = (1, 0)
next_direction = (1, 0)
food = None
score = 0
high_score = 0
running = True
start_screen = True
paused = False
game_over = False
move_delay = 120
last_move = pygame.time.get_ticks()

# --- Helpers ---

def load_high_score():
    try:
        with open("snake_high_score.txt", "r", encoding="utf-8") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(value):
    with open("snake_high_score.txt", "w", encoding="utf-8") as file:
        file.write(str(value))


high_score = load_high_score()


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (30, 44, 61), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (30, 44, 61), (0, y), (WINDOW_WIDTH, y))


def draw_panel():
    pygame.draw.rect(screen, PANEL, (0, 0, WINDOW_WIDTH, 70))
    pygame.draw.rect(screen, PANEL, (0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50))

    title = font_title.render("Snake Deluxe", True, GREEN)
    screen.blit(title, (20, 12))

    score_text = font_ui.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (560, 18))

    high_score_text = font_ui.render(f"Best: {high_score}", True, YELLOW)
    screen.blit(high_score_text, (560, 50))

    instructions = font_small.render("Arrows/WASD Move • Space Pause • Enter Restart", True, WHITE)
    screen.blit(instructions, (20, WINDOW_HEIGHT - 35))


def place_food():
    global food
    food = random.choice([(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)])
    while food in snake:
        food = random.choice([(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)])


def reset_game():
    global snake, direction, next_direction, score, last_move, paused, game_over, start_screen, move_delay
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
    direction = (1, 0)
    next_direction = (1, 0)
    score = 0
    paused = False
    game_over = False
    start_screen = False
    move_delay = 120
    last_move = pygame.time.get_ticks()
    place_food()


def draw_snake():
    for index, segment in enumerate(snake):
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE + 70, CELL_SIZE, CELL_SIZE)
        color = GREEN if index == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, rect, border_radius=5)
        pygame.draw.rect(screen, WHITE, rect, 1, border_radius=5)


def draw_food():
    if food:
        x, y = food
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + 70, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect, border_radius=4)
        pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + 70 + CELL_SIZE // 2), 4)


def draw_start_screen():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    title = font_title.render("Snake Deluxe", True, GREEN)
    screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 150))

    subtitle = font_ui.render("Press Enter to Start", True, WHITE)
    screen.blit(subtitle, (WINDOW_WIDTH // 2 - subtitle.get_width() // 2, 260))

    help_text = font_small.render("Use arrow keys or WASD to steer the snake.", True, WHITE)
    screen.blit(help_text, (WINDOW_WIDTH // 2 - help_text.get_width() // 2, 320))


def draw_pause_screen():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    pause_text = font_title.render("Paused", True, YELLOW)
    screen.blit(pause_text, (WINDOW_WIDTH // 2 - pause_text.get_width() // 2, 220))

    resume_text = font_ui.render("Press Space to Resume", True, WHITE)
    screen.blit(resume_text, (WINDOW_WIDTH // 2 - resume_text.get_width() // 2, 300))


def draw_game_over_screen():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    game_over_text = font_title.render("Game Over", True, RED)
    screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 180))

    score_text = font_ui.render(f"Final Score: {score}", True, WHITE)
    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 260))

    restart_text = font_ui.render("Press Enter to Play Again", True, WHITE)
    screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 320))


place_food()

# --- Main Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                next_direction = (1, 0)
            elif event.key == pygame.K_SPACE and not start_screen and not game_over:
                paused = not paused
            elif event.key == pygame.K_RETURN and (start_screen or game_over):
                reset_game()

    if start_screen:
        screen.fill(BACKGROUND)
        draw_panel()
        draw_grid()
        draw_snake()
        draw_food()
        draw_start_screen()
        pygame.display.flip()
        clock.tick(60)
        continue

    if not paused and not game_over:
        now = pygame.time.get_ticks()
        if now - last_move >= move_delay:
            direction = next_direction
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or new_head in snake):
                game_over = True
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
            else:
                snake = [new_head] + snake
                if food and new_head == food:
                    score += 10
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    if score % 50 == 0:
                        move_delay = max(55, move_delay - 5)
                    place_food()
                else:
                    snake.pop()

            last_move = now

    screen.fill(BACKGROUND)
    draw_panel()
    draw_grid()
    draw_snake()
    draw_food()

    if paused:
        draw_pause_screen()
    elif game_over:
        draw_game_over_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
