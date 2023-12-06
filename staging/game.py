import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.Rect(350, 550, 40, 40)
obstacles = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 40: 
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += 5

    if random.randint(0,100) < 10:
        new_car = pygame.Rect(random.randint(0, 760), 0, 40, 40)
        obstacles.append(new_car)
    
    for car in obstacles:
        car.y += 5
        if car.y > 600:
            obstacles.remove(car) 
              
        if player.colliderect(car):
            running = False
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,255,0), player) 
    for car in obstacles:
        pygame.draw.rect(screen, (255,0,0), car)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
