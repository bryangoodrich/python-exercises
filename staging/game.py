import pygame
import sys
import random

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, PLAYER_SIZE, PLAYER_SIZE))

def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, CAR_WIDTH, CAR_HEIGHT))

WIDTH, HEIGHT = 400, 300
LANE_HEIGHT = HEIGHT // 5
PLAYER_SIZE = 30
CAR_WIDTH = 30
CAR_HEIGHT = LANE_HEIGHT - 10
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - LANE_HEIGHT - PLAYER_SIZE
car_speed = 5
cars = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += 5
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= LANE_HEIGHT
    if keys[pygame.K_DOWN] and player_y < HEIGHT - LANE_HEIGHT - PLAYER_SIZE:
        player_y += LANE_HEIGHT

    for car in cars:
        car[1] += car_speed
        if car[1] > HEIGHT:
            car[1] = -CAR_HEIGHT
            car[0] = random.randint(0, WIDTH - CAR_WIDTH)

    for car in cars:
        if (
            player_x < car[0] + CAR_WIDTH
            and player_x + PLAYER_SIZE > car[0]
            and player_y < car[1] + CAR_HEIGHT
            and player_y + PLAYER_SIZE > car[1]
        ):
            player_x = WIDTH // 2 - PLAYER_SIZE // 2
            player_y = HEIGHT - LANE_HEIGHT - PLAYER_SIZE

    if random.randint(0, 100) <= 10:
        cars.append([random.randint(0, WIDTH - CAR_WIDTH), -CAR_HEIGHT])

    screen.fill(BLACK)
    for i in range(1, 5):
        pygame.draw.rect(screen, WHITE, (0, i * LANE_HEIGHT, WIDTH, 2))

    for car in cars:
        draw_car(car[0], car[1])

    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(FPS)
