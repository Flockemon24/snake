import pygame
import random
import os

# Init pygame
pygame.init()

HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    """Loads the highscore from the file"""
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r") as file:
                return int(file.read().strip())
        except ValueError:
            return 0
    return 0

def save_highscore(new_highscore):
    """Saves highscore in the file"""
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(new_highscore))

def draw_square(column, row, color):
    screen_x = column * SQUARE_SIZE
    screen_y = row * SQUARE_SIZE
    pygame.draw.rect(screen, color, (screen_x, screen_y, SQUARE_SIZE, SQUARE_SIZE))

def draw_game_over():
    """Draws Game Over Screen"""
    screen.fill(BLACK)
    title_text = font_large.render("GAME OVER", True, RED)
    title_rect = title_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 80))

    # Score & Highscore anzeigen
    score_text = font_small.render(f"Your Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 10))

    highscore_text = font_small.render(f"Highscore: {highscore}", True, (255, 215, 0)) # Goldene Farbe
    highscore_rect = highscore_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 30))

    restart_text = font_small.render("Press SPACE to try again or M for menu", True, (180, 180, 180))
    restart_rect = restart_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 100))

    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(highscore_text, highscore_rect)
    screen.blit(restart_text, restart_rect)

def draw_menu():
    """Draws Menu Screen"""
    screen.fill(BLACK)
    title_text = font_large.render("SNAKE", True, WHITE)
    title_rect = title_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 100))

    # Highscore im Menü anzeigen
    menu_hs_text = font_small.render(f"Current Highscore: {highscore}", True, (255, 215, 0))
    menu_hs_rect = menu_hs_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 30))

    start_text = font_small.render("Press SPACE to start", True, WHITE)
    start_rect = start_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 30))

    settings_text = font_small.render("Press S for Settings (Level Select)", True, (150, 150, 150))
    settings_rect = settings_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 80))

    screen.blit(title_text, title_rect)
    screen.blit(menu_hs_text, menu_hs_rect)
    screen.blit(start_text, start_rect)
    screen.blit(settings_text, settings_rect)

def draw_settings():
    """Draws Settings / Level Selection Screen"""
    screen.fill(BLACK)
    title_text = font_large.render("SETTINGS", True, WHITE)
    title_rect = title_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 120))

    # Text für die Level-Optionen
    lvl1_text = font_small.render("Press 1: Level 1 (Slow)", True, (0, 255, 0) if DELAY == 160 else WHITE)
    lvl2_text = font_small.render("Press 2: Level 2 (Normal)", True, (0, 255, 0) if DELAY == 100 else WHITE)
    lvl3_text = font_small.render("Press 3: Level 3 (Fast)", True, (0, 255, 0) if DELAY == 50 else WHITE)
    back_text = font_small.render("Press M to return to Menu", True, (200, 200, 200))

    # Aktuelle Geschwindigkeit anzeigen
    speed_name = "Normal" if DELAY == 100 else ("Slow" if DELAY == 160 else "Fast")
    current_text = font_small.render(f"Current Level: {speed_name}", True, (255, 215, 0))

    screen.blit(title_text, title_rect)
    screen.blit(lvl1_text, lvl1_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 30)))
    screen.blit(lvl2_text, lvl2_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 20)))
    screen.blit(lvl3_text, lvl3_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 70)))
    screen.blit(current_text, current_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 140)))
    screen.blit(back_text, back_text.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 + 200)))


def reset_game():
    """Resets the variables to default"""
    global game_state, head_column, head_row, snake_length, body_parts, step_x, step_y, score, apple_row, apple_column
    game_state = "PLAYING"
    head_column = SQUARE_COUNT // 2
    head_row = SQUARE_COUNT //  2
    snake_length = START_LENGTH
    body_parts = []
    step_x = 0
    step_y = 0
    score = 0
    apple_row = random.randint(0, SQUARE_COUNT-1)
    apple_column = random.randint(0, SQUARE_COUNT-1)

WIN_SIZE = 800
SQUARE_COUNT = 20
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT
DELAY = 100
START_LENGTH = 5

# Colors und Fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
font_large = pygame.font.SysFont("Arial", 64)
font_small = pygame.font.SysFont("Arial", 32)

# Highscore
highscore = load_highscore()
score = 0

# Game States: "PLAYING", "GAMEOVER", "MENU", "SETTINGS"
game_state = "MENU"

# Screen
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("Snake")

head_column = SQUARE_COUNT // 2
head_row = SQUARE_COUNT //  2
snake_length = START_LENGTH
body_parts = []
step_x = 0
step_y = 0
apple_row = random.randint(0, SQUARE_COUNT-1)
apple_column = random.randint(0, SQUARE_COUNT-1)

run = True
while run:
    pygame.time.delay(DELAY)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if game_state == "GAMEOVER": 
                if event.key == pygame.K_SPACE:
                    reset_game()
                elif event.key == pygame.K_m:
                    game_state = "MENU"

            elif game_state == "MENU":
                if event.key == pygame.K_SPACE:
                    reset_game()
                elif event.key == pygame.K_s:
                    game_state = "SETTINGS"

            elif game_state == "SETTINGS":
                if event.key == pygame.K_1:
                    DELAY = 160 
                elif event.key == pygame.K_2:
                    DELAY = 100
                elif event.key == pygame.K_3:
                    DELAY = 50
                elif event.key == pygame.K_m:
                    game_state = "MENU"

    if game_state == "PLAYING":
        # User-Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if step_x != -1:
                step_x = 1
                step_y = 0
        elif keys[pygame.K_LEFT]:
            if step_x != 1:
                step_x = -1
                step_y = 0
        elif keys[pygame.K_DOWN]:
            if step_y != -1:
                step_x = 0
                step_y = 1
        elif keys[pygame.K_UP]:
            if step_y != 1:
                step_x = 0
                step_y = -1

        if step_x != 0 or step_y != 0:
            body_parts.append((head_column, head_row))
            if len(body_parts) >= snake_length:
                body_parts.pop(0)

        head_column += step_x
        head_row += step_y

        if head_column == apple_column and head_row == apple_row:
            snake_length += 1
            score += 1
            if score > highscore:
                highscore = score
                save_highscore(highscore)
            apple_row = random.randint(0, SQUARE_COUNT-1)
            apple_column = random.randint(0, SQUARE_COUNT-1)

        # Checking lose
        vertical_border_hit = head_column < 0 or head_column >= SQUARE_COUNT
        horizontal_border_hit = head_row < 0 or head_row >= SQUARE_COUNT
        self_hit = (head_column, head_row) in body_parts

        if vertical_border_hit or horizontal_border_hit or self_hit:
            game_state = "GAMEOVER"

        screen.fill((0, 0, 0))

        # Draw Snake
        draw_square(head_column, head_row, (0, 255, 0))

        for part in body_parts:
            part_column = part[0]
            part_row = part[1]
            draw_square(part_column, part_row, (0, 255, 0))

        # Draw Apple
        draw_square(apple_column, apple_row, (255, 0, 0))

        for i in range(SQUARE_COUNT):
            line_pos = SQUARE_SIZE * i
            pygame.draw.line(screen, (255, 255, 255), (line_pos, 0), (line_pos, WIN_SIZE), 2)
            pygame.draw.line(screen, (255, 255, 255), (0, line_pos), (WIN_SIZE, line_pos), 2)
            
        # Live Score
        live_score_text = font_small.render(f"Score: {score}  Best: {highscore}", True, (255, 215, 0))
        screen.blit(live_score_text, (15, 15))

    elif game_state == "GAMEOVER":
        draw_game_over()

    elif game_state == "MENU":
        draw_menu()

    elif game_state == "SETTINGS":
        draw_settings()

    pygame.display.update()

pygame.display.quit()
