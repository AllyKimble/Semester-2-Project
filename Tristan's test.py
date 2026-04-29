import pygame
import random
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Game Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPEED = 7
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 3. Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Red Blocks")
clock = pygame.time.Clock()


def run_game():
    player_pos = [WIDTH // 2, HEIGHT - 2 * PLAYER_SIZE]
    enemy_list = []
    score = 0
    game_over = False

    while not game_over:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
            player_pos[0] += 10

        # Create Enemies (Spawn logic)
        if len(enemy_list) < 10 and random.random() < 0.1:
            enemy_list.append([random.randint(0, WIDTH - ENEMY_SIZE), 0])

        # Update Enemy Positions
        for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                enemy_pos[1] += ENEMY_SPEED
            else:
                enemy_list.pop(idx)
                score += 1

        # Collision Detection
        player_rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)
        for enemy_pos in enemy_list:
            enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE)
            if player_rect.colliderect(enemy_rect):
                game_over = True

        # Drawing Everything
        screen.fill(BLACK)

        # Draw Player
        pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

        # Draw Enemies
        for enemy_pos in enemy_list:
            pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

        # Draw Score
        font = pygame.font.SysFont("monospace", 35)
        score_label = font.render(f"Score: {score}", 1, WHITE)
        screen.blit(score_label, (WIDTH - 200, HEIGHT - 40))

        pygame.display.update()
        clock.tick(FPS)

    print(f"Game Over! Your Final Score: {score}")


if __name__ == "__main__":
    run_game()
