import pygame

# Init pygame
pygame.init()

WIN_SIZE = 800
SQUARE_COUNT = 20
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT

# Screen
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("Snake")

head_column = 10
head_row = 5

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    head_x = head_column * SQUARE_SIZE
    head_y = head_row * SQUARE_SIZE
    pygame.draw.rect(screen, (0, 255, 0), (head_x, head_y, SQUARE_SIZE, SQUARE_SIZE))

    for i in range(SQUARE_COUNT):
        line_pos = SQUARE_SIZE * i
        pygame.draw.line(screen, (255, 255, 255), (line_pos, 0), (line_pos, WIN_SIZE), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, line_pos), (Win_Size, line_pos), 2)

    pygame.display.update()

pygame.display.quit()
